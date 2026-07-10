#!/usr/bin/env python3
"""
2_buscar_contenido_unico.py

Compara, por hash de contenido (SHA-256), el repositorio IRAM-PROYECTO
(fuente de verdad) contra las 15 copias de seguridad ya descomprimidas.

NO borra ni mueve nada. Es 100% de solo lectura. Solo genera un reporte.

El reporte lista los archivos que aparecen en las copias de seguridad pero
cuyo CONTENIDO (por hash) no existe en ningún lado del repo actual — es
decir, contenido que se podría estar escapando y vale la pena revisar a
mano antes de decidir si se agrega al repo o se descarta.

La comparación es puramente por hash: si dos archivos tienen distinto
nombre pero mismo contenido, se consideran "el mismo archivo" (no aparece
en el reporte de faltantes). Si tienen el mismo nombre pero distinto
contenido, se consideran archivos DISTINTOS y el que no está en el repo
sí aparece en el reporte.

USO:
    python 2_buscar_contenido_unico.py /ruta/al/repo /ruta/copias_descomprimidas /ruta/reporte.csv

Genera:
    - reporte.csv   : listado de archivos únicos no encontrados en el repo
    - reporte.md     : mismo contenido en formato legible (mismo nombre base + .md)
"""

import sys
import csv
import hashlib
from pathlib import Path
from collections import defaultdict

CHUNK_SIZE = 1024 * 1024  # 1 MB


def sha256_de_archivo(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def escanear_carpeta(carpeta: Path, etiqueta: str):
    """
    Devuelve un dict: hash -> lista de (path, etiqueta_origen)
    Se salta archivos que no se puedan leer (permisos, symlinks rotos, etc.)
    """
    resultado = defaultdict(list)
    archivos = [p for p in carpeta.rglob("*") if p.is_file()]
    total = len(archivos)
    print(f"[{etiqueta}] Escaneando {total} archivos en {carpeta} ...")

    for i, path in enumerate(archivos, 1):
        if i % 200 == 0 or i == total:
            print(f"    ... {i}/{total}")
        try:
            h = sha256_de_archivo(path)
        except (PermissionError, OSError) as e:
            print(f"    (omitido, no se pudo leer: {path} — {e})")
            continue
        resultado[h].append((path, etiqueta))

    return resultado


def main():
    if len(sys.argv) != 4:
        print(
            "USO: python 2_buscar_contenido_unico.py "
            "<carpeta_repo> <carpeta_copias_descomprimidas> <ruta_reporte.csv>"
        )
        sys.exit(1)

    carpeta_repo = Path(sys.argv[1]).expanduser().resolve()
    carpeta_copias = Path(sys.argv[2]).expanduser().resolve()
    ruta_reporte_csv = Path(sys.argv[3]).expanduser().resolve()
    ruta_reporte_md = ruta_reporte_csv.with_suffix(".md")

    if not carpeta_repo.is_dir():
        print(f"ERROR: no existe la carpeta del repo: {carpeta_repo}")
        sys.exit(1)
    if not carpeta_copias.is_dir():
        print(f"ERROR: no existe la carpeta de copias descomprimidas: {carpeta_copias}")
        sys.exit(1)

    # 1. Hashear el repo (fuente de verdad)
    hashes_repo = escanear_carpeta(carpeta_repo, "REPO")
    hashes_repo_set = set(hashes_repo.keys())
    print(f"\nRepo: {len(hashes_repo_set)} hashes únicos encontrados.\n")

    # 2. Hashear cada subcarpeta de copias por separado (para saber de qué
    #    copia de seguridad viene cada hallazgo)
    faltantes = []  # lista de dicts para el CSV
    vistos_en_copias = defaultdict(list)  # hash -> lista de (path, copia_origen)

    subcarpetas_copias = sorted(p for p in carpeta_copias.iterdir() if p.is_dir())
    if not subcarpetas_copias:
        print(f"ADVERTENCIA: no hay subcarpetas dentro de {carpeta_copias}.")
        print("¿Corriste primero 1_descomprimir_copias.py?")
        sys.exit(1)

    for subcarpeta in subcarpetas_copias:
        hashes_copia = escanear_carpeta(subcarpeta, subcarpeta.name)
        for h, lista_paths in hashes_copia.items():
            for path, origen in lista_paths:
                vistos_en_copias[h].append((path, origen))

    print(f"\nCopias: {len(vistos_en_copias)} hashes únicos encontrados en total.\n")

    # 3. Determinar qué hashes de las copias NO están en el repo
    for h, ocurrencias in vistos_en_copias.items():
        if h in hashes_repo_set:
            continue  # ya está resguardado en el repo, no es "faltante"
        # Este contenido no existe en el repo -> posible hallazgo
        for path, origen in ocurrencias:
            faltantes.append({
                "hash_sha256": h,
                "copia_origen": origen,
                "ruta_completa": str(path),
                "nombre_archivo": path.name,
                "tamaño_bytes": path.stat().st_size,
            })

    # 4. Escribir CSV
    with open(ruta_reporte_csv, "w", newline="", encoding="utf-8") as f:
        campos = ["hash_sha256", "copia_origen", "nombre_archivo", "tamaño_bytes", "ruta_completa"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for fila in sorted(faltantes, key=lambda x: (x["hash_sha256"], x["copia_origen"])):
            writer.writerow(fila)

    # 5. Escribir Markdown legible, agrupando por hash (para ver duplicados
    #    entre copias de un mismo archivo "nuevo" de un vistazo)
    agrupado_por_hash = defaultdict(list)
    for fila in faltantes:
        agrupado_por_hash[fila["hash_sha256"]].append(fila)

    with open(ruta_reporte_md, "w", encoding="utf-8") as f:
        f.write("# Reporte: contenido en copias de seguridad no encontrado en el repo\n\n")
        f.write(f"Repo comparado: `{carpeta_repo}`\n\n")
        f.write(f"Copias comparadas: `{carpeta_copias}`\n\n")
        f.write(f"Total de archivos únicos (por hash) no encontrados en el repo: "
                f"**{len(agrupado_por_hash)}**\n\n")
        f.write("Nada fue movido ni borrado. Esto es solo un reporte para revisar a mano.\n\n")
        f.write("---\n\n")

        for h, filas in sorted(agrupado_por_hash.items(), key=lambda x: x[1][0]["nombre_archivo"]):
            nombres = sorted(set(fila["nombre_archivo"] for fila in filas))
            tam = filas[0]["tamaño_bytes"]
            f.write(f"## `{nombres[0]}` ({tam} bytes)\n\n")
            f.write(f"- Hash: `{h}`\n")
            f.write(f"- Aparece en {len(filas)} lugar(es):\n")
            for fila in filas:
                f.write(f"  - Copia **{fila['copia_origen']}**: `{fila['ruta_completa']}`\n")
            f.write("\n")

    print("=" * 60)
    print(f"Listo. {len(agrupado_por_hash)} contenidos únicos no encontrados en el repo.")
    print(f"CSV:      {ruta_reporte_csv}")
    print(f"Markdown: {ruta_reporte_md}")


if __name__ == "__main__":
    main()
