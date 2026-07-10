#!/usr/bin/env python3
"""
Compara N copias de un proyecto por hash MD5 de contenido.
Acepta tanto CARPETAS descomprimidas como archivos .ZIP directamente
(no hace falta extraer los zips a mano).

USO:
    python comparar_copias_iram.py "IRAM PROYECTOv1.zip" "IRAM PROYECTOv2.zip" "IRAM PROYECTOv3.zip" "IRAM_PROYECTO_REORGANIZADO.zip" "IRAM_PROYECTO_REORGANIZADO2.zip"

    (también podés mezclar carpetas sueltas en la misma llamada, ej. "IRAM PROYECTO")

El nombre de cada copia en el reporte es el nombre del archivo/carpeta
(sin extensión .zip).

SALIDA (en la misma carpeta donde corras el script):
    reporte_comparacion.json   -> reporte completo estructurado
    reporte_resumen.txt        -> resumen legible para vos
    conflictos.csv             -> SOLO los archivos con mismo nombre/ruta
                                   relativa pero contenido distinto entre copias
                                   (los que hay que mirar a mano)

Subí SOLO esos 3 archivos de vuelta a Claude para el análisis siguiente.
No hace falta subir los 400 MB de archivos originales.
"""

import hashlib
import json
import os
import sys
import csv
import zipfile
from collections import defaultdict, Counter
from pathlib import Path

# Extensiones/carpetas a ignorar (metadata de sistema, no contenido real)
IGNORE_NAMES = {".DS_Store", "Thumbs.db", "__pycache__", ".git"}
IGNORE_EXTS = {".pyc"}

def to_long_path(path_str):
    """En Windows, antepone el prefijo \\\\?\\ para poder leer rutas de más de 260 caracteres."""
    if os.name == "nt":
        p = os.path.abspath(str(path_str))
        if not p.startswith("\\\\?\\"):
            p = "\\\\?\\" + p
        return p
    return str(path_str)

def hash_file(path, block_size=1 << 20):
    h = hashlib.md5()
    try:
        with open(to_long_path(path), "rb") as f:
            while chunk := f.read(block_size):
                h.update(chunk)
        return h.hexdigest()
    except (OSError, PermissionError) as e:
        return f"ERROR:{e}"

def hash_bytes_stream(fileobj, block_size=1 << 20):
    h = hashlib.md5()
    while chunk := fileobj.read(block_size):
        h.update(chunk)
    return h.hexdigest()

def scan_folder(root):
    """Devuelve dict: ruta_relativa (minúsculas) -> {hash, rel_path, size_bytes}"""
    root_orig = Path(root)
    root_long = Path(to_long_path(root))
    out = {}
    for dirpath, dirnames, filenames in os.walk(root_long):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_NAMES]
        for fname in filenames:
            if fname in IGNORE_NAMES:
                continue
            if Path(fname).suffix in IGNORE_EXTS:
                continue
            full = Path(dirpath) / fname
            try:
                rel = full.relative_to(root_long)
            except ValueError:
                # Fallback improbable: si por algún motivo no matchea el prefijo
                rel = Path(str(full)[len(str(root_long)):].lstrip("\\/"))
            rel_str = rel.as_posix()
            key = rel_str.lower()
            try:
                size = full.stat().st_size
            except OSError:
                size = 0
            out[key] = {
                "hash": hash_file(full),
                "rel_path": rel_str,
                "size_bytes": size,
            }
    return out

def scan_zip(zip_path):
    """Devuelve dict: ruta_relativa (minúsculas) -> {hash, rel_path, size_bytes}, leyendo directo del zip."""
    out = {}
    try:
        zf = zipfile.ZipFile(zip_path, "r")
    except Exception as e:
        print(f"  ERROR abriendo '{zip_path}' como zip: {type(e).__name__}: {e}")
        return out

    with zf:
        try:
            infolist = zf.infolist()
        except Exception as e:
            print(f"  ERROR leyendo el índice de '{zip_path}': {type(e).__name__}: {e}")
            return out

        total_entries = len(infolist)
        dir_entries = sum(1 for i in infolist if i.is_dir())
        print(f"  [debug] entradas totales en el zip: {total_entries} (de las cuales carpetas: {dir_entries})")

        for info in infolist:
            if info.is_dir():
                continue
            name = info.filename
            base = Path(name).name
            if base in IGNORE_NAMES or Path(base).suffix in IGNORE_EXTS:
                continue
            rel_str = name.replace("\\", "/")
            key = rel_str.lower()
            try:
                with zf.open(info, "r") as f:
                    h = hash_bytes_stream(f)
            except (zipfile.BadZipFile, RuntimeError, OSError) as e:
                h = f"ERROR:{e}"
            out[key] = {
                "hash": h,
                "rel_path": rel_str,
                "size_bytes": info.file_size,
            }
    return out

def scan_copy(path):
    """Despacha a scan_zip o scan_folder según el tipo de entrada."""
    p = Path(path)
    if p.is_file() and p.suffix.lower() == ".zip":
        return scan_zip(p)
    elif p.is_dir():
        return scan_folder(p)
    else:
        print(f"AVISO: '{path}' no es ni un .zip ni una carpeta válida, se omite.")
        return {}

def normalize_common_wrapper(out_dict, copy_name, dominance_threshold=0.8):
    """
    Si la GRAN MAYORÍA de los archivos de una copia comparten el mismo primer
    segmento de ruta (una carpeta "envoltorio" dominante), lo saca de esos
    archivos y repite. Los archivos sueltos que queden fuera de ese envoltorio
    (ej. un plan.md en la raíz real) se dejan intactos, sin forzar que el 100%
    coincida -- así no se bloquea la normalización por un puñado de archivos
    sueltos en la raíz real del proyecto.
    """
    stripped_layers = []
    while out_dict:
        seg_counts = Counter(k.split("/", 1)[0] for k in out_dict)
        dominant, count = seg_counts.most_common(1)[0]
        total = len(out_dict)
        if total == 0 or count / total < dominance_threshold or count < 2:
            break
        # Tiene que ser una carpeta real (con archivos anidados adentro), no un archivo suelto
        if not any(k.startswith(dominant + "/") for k in out_dict):
            break

        new_dict = {}
        changed = False
        for k, v in out_dict.items():
            if k.startswith(dominant + "/"):
                new_key = k.split("/", 1)[1]
                new_rel = v["rel_path"].split("/", 1)[1]
                new_dict[new_key] = {**v, "rel_path": new_rel}
                changed = True
            else:
                # archivo suelto fuera del envoltorio dominante: se deja igual
                new_dict[k] = v
        if not changed:
            break
        out_dict = new_dict
        stripped_layers.append(dominant)

    if stripped_layers:
        print(f"  [normalizado] '{copy_name}': se sacó envoltorio dominante -> {'/'.join(stripped_layers)}/")
    return out_dict

def main():
    if len(sys.argv) < 3:
        print("Uso: python comparar_copias_iram.py /ruta/copia1 /ruta/copia2 [...]")
        sys.exit(1)

    copy_paths = sys.argv[1:]
    copies = {}
    used_names = {}
    for p in copy_paths:
        resolved = Path(p).resolve()
        raw_name = resolved.name
        name = raw_name[:-4] if raw_name.lower().endswith(".zip") else raw_name

        # Si el nombre ya se usó (ej: zip y carpeta con el mismo nombre base),
        # lo desambiguamos agregando [zip] o [carpeta] para no pisar datos.
        if name in used_names:
            tag = "zip" if resolved.is_file() else "carpeta"
            prev_tag = used_names[name]
            print(f"AVISO: nombre repetido '{name}' — se renombra esta copia a '{name} [{tag}]' "
                  f"para no pisar la copia anterior '{name} [{prev_tag}]'.")
            name = f"{name} [{tag}]"
        else:
            used_names[name] = "zip" if resolved.is_file() else "carpeta"

        print(f"Escaneando '{name}' ({p}) ...")
        scanned = scan_copy(p)
        scanned = normalize_common_wrapper(scanned, name)
        copies[name] = scanned
        print(f"  -> {len(copies[name])} archivos")

    copy_names = list(copies.keys())

    # Universo de rutas relativas (case-insensitive) vistas en cualquier copia
    all_rel_keys = set()
    for c in copies.values():
        all_rel_keys.update(c.keys())

    identical_everywhere = []      # mismo rel_path, mismo hash en TODAS las copias que lo tienen, y está en todas
    partial_presence = []          # existe en algunas copias pero no en todas (independiente del hash)
    conflicts = []                 # mismo rel_path, pero hash distinto entre copias que lo tienen

    # Índice por hash real -> para detectar archivos movidos/renombrados con mismo contenido
    hash_to_locations = defaultdict(list)  # hash -> [(copy_name, rel_path)]

    for key in sorted(all_rel_keys):
        present_in = {c: copies[c][key] for c in copy_names if key in copies[c]}
        hashes = {v["hash"] for v in present_in.values()}

        for cname, v in present_in.items():
            hash_to_locations[v["hash"]].append((cname, v["rel_path"]))

        if len(present_in) < len(copy_names):
            partial_presence.append({
                "rel_path_key": key,
                "presente_en": sorted(present_in.keys()),
                "ausente_en": sorted(set(copy_names) - set(present_in.keys())),
                "ejemplo_rel_path": next(iter(present_in.values()))["rel_path"],
            })

        if len(hashes) > 1:
            conflicts.append({
                "rel_path_key": key,
                "detalle": {cname: v["hash"] for cname, v in present_in.items()},
                "ejemplo_rel_path": next(iter(present_in.values()))["rel_path"],
            })
        elif len(present_in) == len(copy_names) and len(hashes) == 1:
            identical_everywhere.append(key)

    # Archivos cuyo hash existe en más de una ubicación distinta (posibles duplicados/renombrados)
    duplicated_content_diff_name = {
        h: locs for h, locs in hash_to_locations.items()
        if len({l[1] for l in locs}) > 1  # mismo hash, rutas relativas distintas
    }

    report = {
        "copias_analizadas": copy_names,
        "totales": {c: len(copies[c]) for c in copy_names},
        "resumen": {
            "identicos_en_todas_las_copias": len(identical_everywhere),
            "presentes_parcialmente": len(partial_presence),
            "conflictos_mismo_nombre_distinto_contenido": len(conflicts),
        },
        "presencia_parcial": partial_presence,
        "conflictos": conflicts,
    }

    with open("reporte_comparacion.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    with open("conflictos.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ruta_relativa", "copias_en_conflicto", "hashes"])
        for c in conflicts:
            writer.writerow([
                c["ejemplo_rel_path"],
                ", ".join(c["detalle"].keys()),
                json.dumps(c["detalle"]),
            ])

    with open("reporte_resumen.txt", "w", encoding="utf-8") as f:
        f.write("COMPARACIÓN DE COPIAS — PROYECTO IRAM\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Copias analizadas: {', '.join(copy_names)}\n")
        for c in copy_names:
            f.write(f"  - {c}: {len(copies[c])} archivos\n")
        f.write("\n")
        f.write(f"Idénticos en TODAS las copias: {len(identical_everywhere)}\n")
        f.write(f"Presentes solo en ALGUNAS copias (faltan en otras): {len(partial_presence)}\n")
        f.write(f"CONFLICTOS reales (mismo nombre, contenido distinto): {len(conflicts)}\n\n")

        if partial_presence:
            f.write("--- ARCHIVOS QUE FALTAN EN ALGUNA COPIA ---\n")
            for p in partial_presence[:200]:
                f.write(f"  {p['ejemplo_rel_path']}\n")
                f.write(f"    presente en: {p['presente_en']}\n")
                f.write(f"    ausente en:  {p['ausente_en']}\n")
            if len(partial_presence) > 200:
                f.write(f"  ... y {len(partial_presence)-200} más (ver JSON completo)\n")
            f.write("\n")

        if conflicts:
            f.write("--- CONFLICTOS: MISMO ARCHIVO, CONTENIDO DISTINTO (revisar a mano) ---\n")
            for c in conflicts[:200]:
                f.write(f"  {c['ejemplo_rel_path']}\n")
                for cname, h in c["detalle"].items():
                    f.write(f"    {cname}: {h}\n")
            if len(conflicts) > 200:
                f.write(f"  ... y {len(conflicts)-200} más (ver JSON completo)\n")

    print("\nListo. Generé 3 archivos:")
    print("  - reporte_comparacion.json  (completo)")
    print("  - reporte_resumen.txt       (legible)")
    print("  - conflictos.csv            (solo los que necesitan revisión manual)")
    print("\nSubí esos 3 archivos (son livianos) para que sigamos el análisis.")

if __name__ == "__main__":
    main()
