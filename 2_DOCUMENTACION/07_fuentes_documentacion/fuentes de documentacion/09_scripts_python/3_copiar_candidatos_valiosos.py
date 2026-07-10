#!/usr/bin/env python3
"""
3_copiar_candidatos_valiosos.py

Lee el reporte.csv generado por 2_buscar_contenido_unico.py y copia a una
carpeta nueva SOLO los archivos que valen la pena revisar a mano: texto
(.md, .txt, .json, .py, .html, .csv y similares) que no sea ruido conocido
de Git interno ni archivos del mod de juego (localization, mod_pack,
by_other_means, exodos).

NO borra ni modifica los originales. Solo copia (de solo lectura sobre
el origen).

Cada hash único se copia UNA sola vez (aunque aparezca en varias copias
de seguridad), con un nombre que evita colisiones y conserva de dónde
salió, para que sea fácil comprimir esta carpeta chica y subirla.

USO:
    python 3_copiar_candidatos_valiosos.py <reporte.csv> <carpeta_destino>

Genera además:
    - <carpeta_destino>/_indice_copiados.csv : hash, nombre original,
      ruta original completa, nombre final en la carpeta destino,
      tamaño en bytes.
    - Imprime en pantalla un resumen de cuántos se copiaron, cuántos se
      excluyeron por ruido, y el total de tamaño copiado.

Extensiones consideradas "valiosas" por defecto (se pueden agregar más
con --ext): .md .txt .json .py .html .csv

Filtros de ruido aplicados (rutas que contengan, insensible a
mayúsculas):
    - "\\.git\\" o "/.git/"      -> objetos internos de Git
    - "localization"             -> archivos de idioma del mod de juego
    - "mod_pack"                 -> paquetes del mod de juego
    - "by_other_means"           -> carpeta del mod de juego
    - "exodos"                   -> carpeta del mod de juego

Si querés incluir igual algo que el filtro excluye, o excluir algo más,
usá --incluir-todo (desactiva todos los filtros) o --excluir-tambien
"palabra" (podés repetirlo) para sumar más términos a la lista negra.
"""

import sys
import csv
import shutil
import argparse
from pathlib import Path
from collections import defaultdict

EXTENSIONES_VALIOSAS_DEFAULT = {".md", ".txt", ".json", ".py", ".html", ".csv"}

FILTROS_RUIDO_DEFAULT = [
    ".git" + "\\",   # objetos internos de git (windows)
    ".git/",          # objetos internos de git (unix, por si acaso)
    "localization",
    "mod_pack",
    "by_other_means",
    "exodos",
]


def es_ruido(ruta: str, filtros: list[str]) -> bool:
    ruta_l = ruta.lower()
    return any(f.lower() in ruta_l for f in filtros)


def sanitize_name(name: str, max_len: int = 60) -> str:
    limpio = "".join(c if c.isalnum() or c in "._- " else "_" for c in name)
    limpio = limpio.strip("_ ")
    return limpio[:max_len] if limpio else "archivo"


def main():
    parser = argparse.ArgumentParser(
        description="Copia a una carpeta chica los archivos de texto candidatos a revisar."
    )
    parser.add_argument("reporte_csv", help="Ruta al reporte.csv generado por el script 2")
    parser.add_argument("carpeta_destino", help="Carpeta donde se van a copiar los candidatos")
    parser.add_argument(
        "--ext", action="append", default=[],
        help="Extensión extra a incluir (ej. --ext .yml). Se puede repetir."
    )
    parser.add_argument(
        "--excluir-tambien", action="append", default=[],
        help="Palabra extra a filtrar como ruido (ej. --excluir-tambien node_modules). Se puede repetir."
    )
    parser.add_argument(
        "--incluir-todo", action="store_true",
        help="Desactiva los filtros de ruido (.git, mod de juego). Copia todo lo que matchee la extensión."
    )
    parser.add_argument(
        "--max-mb", type=float, default=50.0,
        help="Tamaño máximo por archivo individual, en MB, para copiar (default: 50). "
             "Los que superen esto se listan pero NO se copian, para no romper el zip que subas después."
    )
    args = parser.parse_args()

    ruta_reporte = Path(args.reporte_csv).expanduser().resolve()
    carpeta_destino = Path(args.carpeta_destino).expanduser().resolve()

    if not ruta_reporte.is_file():
        print(f"ERROR: no existe el reporte: {ruta_reporte}")
        sys.exit(1)

    carpeta_destino.mkdir(parents=True, exist_ok=True)

    extensiones = EXTENSIONES_VALIOSAS_DEFAULT | {e if e.startswith(".") else f".{e}" for e in args.ext}
    filtros = [] if args.incluir_todo else (FILTROS_RUIDO_DEFAULT + args.excluir_tambien)
    max_bytes = args.max_mb * 1024 * 1024

    with open(ruta_reporte, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        filas = list(reader)

    print(f"Filas leídas del reporte: {len(filas)}")

    # Agrupar por hash: cada hash único se copia una sola vez, aunque
    # aparezca repetido en varias copias de seguridad.
    por_hash = defaultdict(list)
    for fila in filas:
        por_hash[fila["hash_sha256"]].append(fila)

    print(f"Hashes únicos en el reporte: {len(por_hash)}\n")

    copiados = []
    excluidos_ruido = 0
    excluidos_ext = 0
    excluidos_tamano = []
    fallidos = []

    usados = set()  # para evitar colisión de nombres en destino

    for h, ocurrencias in por_hash.items():
        primera = ocurrencias[0]
        nombre_original = primera["nombre_archivo"]
        ruta_original = primera["ruta_completa"]
        ext = Path(nombre_original).suffix.lower()

        if ext not in extensiones:
            excluidos_ext += 1
            continue

        if filtros and any(es_ruido(oc["ruta_completa"], filtros) for oc in ocurrencias):
            # Si TODAS las ocurrencias de este hash son ruido, lo salteamos.
            # (si al menos una ocurrencia no es ruido, igual lo copiamos,
            # usando esa ocurrencia no-ruidosa como origen)
            no_ruidosas = [oc for oc in ocurrencias if not es_ruido(oc["ruta_completa"], filtros)]
            if not no_ruidosas:
                excluidos_ruido += 1
                continue
            primera = no_ruidosas[0]
            ruta_original = primera["ruta_completa"]

        try:
            tam = int(primera["tamaño_bytes"])
        except (KeyError, ValueError):
            tam = Path(ruta_original).stat().st_size if Path(ruta_original).exists() else 0

        if tam > max_bytes:
            excluidos_tamano.append((nombre_original, tam, ruta_original))
            continue

        origen_path = Path(ruta_original)
        if not origen_path.exists():
            fallidos.append((nombre_original, ruta_original, "no existe / no accesible desde este equipo"))
            continue

        # Armar nombre destino corto, único, con hash corto para trazabilidad
        stem = sanitize_name(origen_path.stem, max_len=50)
        hash_corto = h[:8]
        nombre_destino = f"{stem}__{hash_corto}{origen_path.suffix.lower()}"
        contador = 1
        while nombre_destino in usados:
            nombre_destino = f"{stem}__{hash_corto}__{contador}{origen_path.suffix.lower()}"
            contador += 1
        usados.add(nombre_destino)

        destino_path = carpeta_destino / nombre_destino
        try:
            shutil.copy2(origen_path, destino_path)
        except Exception as e:
            fallidos.append((nombre_original, ruta_original, str(e)))
            continue

        copiados.append({
            "hash_sha256": h,
            "nombre_original": nombre_original,
            "ruta_original_completa": ruta_original,
            "nombre_en_destino": nombre_destino,
            "tamaño_bytes": tam,
            "cantidad_lugares_donde_aparece": len(ocurrencias),
        })

    # Escribir índice
    indice_path = carpeta_destino / "_indice_copiados.csv"
    with open(indice_path, "w", newline="", encoding="utf-8") as f:
        campos = ["hash_sha256", "nombre_original", "ruta_original_completa",
                  "nombre_en_destino", "tamaño_bytes", "cantidad_lugares_donde_aparece"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(sorted(copiados, key=lambda x: -x["tamaño_bytes"]))

    total_bytes = sum(c["tamaño_bytes"] for c in copiados)

    print("=" * 60)
    print(f"Copiados:              {len(copiados)} archivos ({total_bytes / (1024*1024):.1f} MB)")
    print(f"Excluidos (ruido):     {excluidos_ruido}")
    print(f"Excluidos (extensión): {excluidos_ext}")
    print(f"Excluidos (muy grandes, > {args.max_mb} MB): {len(excluidos_tamano)}")
    print(f"Fallidos (no se pudo copiar): {len(fallidos)}")
    print(f"\nÍndice guardado en: {indice_path}")

    if excluidos_tamano:
        print(f"\nArchivos grandes NO copiados (revisalos aparte, uno por uno, si querés):")
        for nombre, tam, ruta in sorted(excluidos_tamano, key=lambda x: -x[1]):
            print(f"  {tam/(1024*1024):>7.1f} MB  {nombre}")
            print(f"           {ruta}")

    if fallidos:
        print(f"\nArchivos que fallaron al copiar:")
        for nombre, ruta, error in fallidos[:20]:
            print(f"  {nombre}: {error}")
        if len(fallidos) > 20:
            print(f"  ... y {len(fallidos) - 20} más (ver si son rutas muy largas de Windows)")

    print(f"\nSiguiente paso sugerido:")
    print(f"  1. Comprimí la carpeta '{carpeta_destino}' en un .zip")
    print(f"  2. Subí ese .zip a la conversación con Claude")


if __name__ == "__main__":
    main()
