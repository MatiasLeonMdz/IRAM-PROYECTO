#!/usr/bin/env python3
"""
1_descomprimir_copias.py

Descomprime todas las copias de seguridad (zip/rar/7z) encontradas DENTRO
de una carpeta de origen, buscando en TODOS los subniveles (los .zip
pueden estar 1, 2 o más carpetas adentro — el script los encuentra igual,
no hace falta que estén sueltos en el primer nivel).

Cada comprimido se extrae a una carpeta de destino con nombre CORTO y
NUMERADO (ej. "0001_datos", "0002_documentacion_claude_1"), para evitar
el límite de ruta de Windows (260 caracteres). La versión anterior de
este script nombraba las carpetas con la ruta relativa completa, lo cual
funciona en Linux/Mac pero en Windows con muchos niveles de carpetas
anidadas ("IRAM_PROYECTO_REORGANIZADO_v4/documentacion iram.../fuentes de
documentacion/...") hacía que la ruta final superara los 260 caracteres
y Windows tirara error (WinError 206, WinError 3, o FileNotFoundError al
crear la carpeta o escribir un archivo adentro).

La trazabilidad de "de dónde salió cada zip" no se pierde: se guarda en
un archivo `_mapa_carpetas.csv` (número <-> ruta original completa del
zip) y en el log de siempre.

Además, en Windows se le agrega automáticamente el prefijo especial
"\\\\?\\" a las rutas al crear carpetas/extraer archivos, que le pide a
Windows que ignore el límite de 260 caracteres (soportado desde Windows
10). Esto es una ayuda extra, no un reemplazo de los nombres cortos: con
muchas carpetas de nombres largos anidadas, ambas cosas juntas son más
seguras que confiar en una sola.

USO:
    python 1_descomprimir_copias.py /ruta/a/las/copias /ruta/de/salida

No borra ni modifica los .zip/.rar/.7z originales. Solo extrae copias.

Requiere para .rar: la herramienta `unrar` o `7z` instalada en el sistema.
Requiere para .7z:  la herramienta `7z` (p7zip) instalada en el sistema.
Los .zip los maneja con la librería estándar de Python (zipfile), sin
dependencias extra.
"""

import sys
import csv
import shutil
import subprocess
import zipfile
import platform
from pathlib import Path

ARCHIVE_EXTENSIONS = {".zip", ".rar", ".7z"}


def con_prefijo_largo(path: Path) -> str:
    """
    En Windows, antepone el prefijo \\\\?\\ a una ruta absoluta para que
    Windows ignore el límite de 260 caracteres. En otros sistemas
    operativos, devuelve la ruta tal cual (el prefijo no aplica ahí).
    """
    if platform.system() != "Windows":
        return str(path)
    ruta_str = str(path.resolve())
    if ruta_str.startswith("\\\\?\\"):
        return ruta_str
    return "\\\\?\\" + ruta_str


def sanitize_name(name: str, max_len: int = 40) -> str:
    """Convierte un nombre en algo corto y seguro para carpeta, sin barras."""
    limpio = "".join(c if c.isalnum() or c in "._- " else "_" for c in name)
    limpio = limpio.strip("_ ")
    return limpio[:max_len] if limpio else "archivo"


def extract_zip(archive_path: Path, dest_dir: Path) -> tuple[bool, str]:
    try:
        dest_str = con_prefijo_largo(dest_dir)
        with zipfile.ZipFile(archive_path, "r") as zf:
            for member in zf.infolist():
                zf.extract(member, dest_str)
        return True, ""
    except zipfile.BadZipFile as e:
        return False, f"ZIP corrupto o inválido: {e}"
    except Exception as e:
        return False, str(e)


def extract_with_external_tool(archive_path: Path, dest_dir: Path) -> tuple[bool, str]:
    """Intenta extraer .rar o .7z usando herramientas externas del sistema."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_str = con_prefijo_largo(dest_dir)

    if shutil.which("7z"):
        result = subprocess.run(
            ["7z", "x", f"-o{dest_str}", "-y", str(archive_path)],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            return True, ""

    if archive_path.suffix.lower() == ".rar" and shutil.which("unrar"):
        result = subprocess.run(
            ["unrar", "x", "-y", str(archive_path), dest_str + "\\"],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            return True, ""

    return False, (
        "No se pudo extraer. Instalá '7z' (p7zip-full) o 'unrar' en el sistema. "
        "En Windows podés usar 7-Zip (https://www.7-zip.org/) y correr este "
        "script desde una terminal donde '7z' esté en el PATH."
    )


def main():
    if len(sys.argv) != 3:
        print("USO: python 1_descomprimir_copias.py <carpeta_con_copias> <carpeta_salida>")
        sys.exit(1)

    origen = Path(sys.argv[1]).expanduser().resolve()
    salida = Path(sys.argv[2]).expanduser().resolve()

    if not origen.is_dir():
        print(f"ERROR: no existe la carpeta de origen: {origen}")
        sys.exit(1)

    salida.mkdir(parents=True, exist_ok=True)

    archivos = sorted(
        p for p in origen.rglob("*")
        if p.is_file() and p.suffix.lower() in ARCHIVE_EXTENSIONS
    )

    if not archivos:
        print(f"No se encontraron archivos .zip/.rar/.7z en {origen}")
        sys.exit(0)

    print(f"Encontrados {len(archivos)} archivos comprimidos en {origen}\n")

    ok_count = 0
    fail_count = 0
    log_lines = []
    mapa_filas = []

    for i, archive_path in enumerate(archivos, 1):
        numero = f"{i:04d}"
        nombre_corto = sanitize_name(archive_path.stem)
        carpeta_nombre = f"{numero}_{nombre_corto}"
        dest_dir = salida / carpeta_nombre

        dest_dir.mkdir(parents=True, exist_ok=True)

        ruta_relativa_original = archive_path.relative_to(origen)

        print(f"[{numero}] Extrayendo: {archive_path.name}")
        print(f"         origen: {ruta_relativa_original}")
        print(f"         -> {dest_dir}")

        if archive_path.suffix.lower() == ".zip":
            success, error = extract_zip(archive_path, dest_dir)
        else:
            success, error = extract_with_external_tool(archive_path, dest_dir)

        mapa_filas.append({
            "numero": numero,
            "carpeta_destino": carpeta_nombre,
            "ruta_original_relativa": str(ruta_relativa_original),
            "ruta_original_completa": str(archive_path),
            "resultado": "OK" if success else "FALLO",
            "error": "" if success else error,
        })

        if success:
            ok_count += 1
            print("   OK\n")
            log_lines.append(f"OK    | [{numero}] {archive_path} -> {dest_dir}")
        else:
            fail_count += 1
            print(f"   FALLÓ: {error}\n")
            log_lines.append(f"FALLO | [{numero}] {archive_path} -> {error}")

    log_path = salida / "_log_descompresion.txt"
    log_path.write_text("\n".join(log_lines), encoding="utf-8")

    mapa_path = salida / "_mapa_carpetas.csv"
    with open(mapa_path, "w", newline="", encoding="utf-8") as f:
        campos = ["numero", "carpeta_destino", "ruta_original_relativa",
                  "ruta_original_completa", "resultado", "error"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(mapa_filas)

    print("=" * 60)
    print(f"Listo. {ok_count} extraídos OK, {fail_count} con error.")
    print(f"Detalle guardado en: {log_path}")
    print(f"Mapa carpeta <-> origen guardado en: {mapa_path}")
    if fail_count:
        print("\nRevisá los que fallaron arriba. Si el error menciona 'ruta demasiado")
        print("larga' o WinError 206/3, avisame — puede que el propio nombre interno")
        print("de algún archivo DENTRO del zip sea muy largo, no solo la carpeta.")


if __name__ == "__main__":
    main()
