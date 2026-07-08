#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verificar_iram.py — Herramienta de auditoría reutilizable para el proyecto IRAM.

Nace de la sesión de auditoría del 2026-07-05/06 (ver SESSION_LOG_AUDITORIA_ZIP_INVENTARIO_2026-07-05.md).
Reemplaza los one-liners de bash (find | xargs md5sum, comm -13, etc.) usados ad-hoc durante
varias sesiones por un único script parametrizable, para no reconstruir la lógica de comparación
cada vez que aparece un zip nuevo o se actualiza el inventario.

SUBCOMANDOS
-----------
manifest      Genera un manifest (ruta, tamaño, md5) de un zip o carpeta ya extraída.

comparar      Compara dos zips/carpetas por CONTENIDO (hash), en ambas direcciones.
              Responde: "¿A tiene algo que B no tiene, y viceversa?"

colisiones    Detecta archivos con el MISMO nombre base (ignorando sufijos "(2)", " 3", etc.)
              pero CONTENIDO DISTINTO. Esto es lo que reveló que los sufijos numéricos del
              proyecto IRAM no son duplicados de re-subida, sino colisiones de nombre por
              falta de hora local en el sistema de documentación (confirmado por el operador
              el 2026-07-05).

duplicados    Lo inverso: agrupa por HASH y lista archivos con contenido idéntico que viven
              en más de una ruta. Sirve para verificar de forma EXHAUSTIVA (no solo por conteo
              agregado) que una carpeta como _CUARENTENA_DUPLICADOS es realmente redundante,
              archivo por archivo — chequeo que quedó pendiente en la sesión de origen.

inventario    Cruza el contenido real de un zip/carpeta contra un inventario .md, listando qué
              archivos del zip no tienen ninguna mención (ni parcial) en el texto del inventario.
              Es una heurística de texto, NO semántica — revisar a mano antes de dar por buena
              cualquier ausencia (el inventario usa comodines y rangos tipo "s7 a s21" que esta
              heurística no siempre resuelve; en la sesión de origen, ~80 de 91 candidatos
              iniciales resultaron falsos positivos de este tipo).

EJEMPLOS
--------
  python3 verificar_iram.py manifest PROYECTO.zip -o manifest_base.csv
  python3 verificar_iram.py comparar PROYECTO_A.zip PROYECTO_B.zip
  python3 verificar_iram.py colisiones PROYECTO.zip
  python3 verificar_iram.py duplicados PROYECTO.zip --detalle
  python3 verificar_iram.py inventario PROYECTO.zip INVENTARIO.md -o cruce_inventario.md

Requiere solo librería estándar (Python 3.8+). Acepta .zip o carpetas ya extraídas indistintamente.
"""
import argparse
import hashlib
import os
import re
import shutil
import sys
import tempfile
import zipfile
from collections import defaultdict
from pathlib import Path


def md5_file(path, block_size=1 << 20):
    h = hashlib.md5()
    with open(path, "rb") as f:
        while True:
            chunk = f.read(block_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def resolve_root(path):
    """
    Si `path` es un .zip, lo extrae a un directorio temporal y devuelve (raiz, tmpdir_a_borrar).
    Si ya es una carpeta, la devuelve tal cual (raiz, None).
    """
    p = Path(path)
    if p.is_dir():
        return p, None
    if p.is_file() and p.suffix.lower() == ".zip":
        tmpdir = tempfile.mkdtemp(prefix="iram_audit_")
        with zipfile.ZipFile(p) as z:
            z.extractall(tmpdir)
        return Path(tmpdir), tmpdir
    raise ValueError(f"No es un .zip ni una carpeta existente: {path}")


def build_manifest(root):
    """Devuelve {ruta_relativa_str: (tamano_bytes, md5)} para todos los archivos bajo `root`."""
    manifest = {}
    for dirpath, _dirnames, filenames in os.walk(root):
        for fn in filenames:
            full = Path(dirpath) / fn
            rel = full.relative_to(root)
            try:
                manifest[str(rel)] = (full.stat().st_size, md5_file(full))
            except (OSError, PermissionError) as e:
                print(f"  [aviso] no se pudo leer {rel}: {e}", file=sys.stderr)
    return manifest


def normalize_basename(name):
    """
    Quita sufijos de colisión de nombre al final del nombre (antes de la extensión):
    'archivo 2.md' -> 'archivo.md' ; 'archivo(2).md' -> 'archivo.md' ; 'archivo (3).md' -> 'archivo.md'
    """
    stem, ext = os.path.splitext(name)
    stem = re.sub(r"[\s_]?\(\d+\)$", "", stem)
    stem = re.sub(r"\s\d+$", "", stem)
    return stem + ext


def _cleanup(tmp):
    if tmp:
        shutil.rmtree(tmp, ignore_errors=True)


# ---------------------------------------------------------------- manifest

def cmd_manifest(args):
    root, tmp = resolve_root(args.path)
    try:
        manifest = build_manifest(root)
        lines = ["ruta,tamano_bytes,md5"]
        for rel, (size, h) in sorted(manifest.items()):
            rel_csv = rel.replace('"', '""')
            lines.append(f'"{rel_csv}",{size},{h}')
        out = "\n".join(lines)
        if args.output:
            Path(args.output).write_text(out, encoding="utf-8")
            print(f"Manifest de {len(manifest)} archivos guardado en {args.output}")
        else:
            print(out)
    finally:
        _cleanup(tmp)


# ---------------------------------------------------------------- comparar

def cmd_comparar(args):
    root_a, tmp_a = resolve_root(args.zip_a)
    root_b, tmp_b = resolve_root(args.zip_b)
    try:
        man_a = build_manifest(root_a)
        man_b = build_manifest(root_b)
        hashes_a = {h for (_, h) in man_a.values()}
        hashes_b = {h for (_, h) in man_b.values()}

        solo_en_a = hashes_a - hashes_b
        solo_en_b = hashes_b - hashes_a

        print(f"=== A: {args.zip_a} — {len(man_a)} archivos, {len(hashes_a)} contenidos únicos ===")
        print(f"=== B: {args.zip_b} — {len(man_b)} archivos, {len(hashes_b)} contenidos únicos ===\n")

        print(f"Contenido en A que NO está en B: {len(solo_en_a)} archivo(s)")
        for rel, (_sz, h) in sorted(man_a.items()):
            if h in solo_en_a:
                print(f"   - {rel}")
        print()

        print(f"Contenido en B que NO está en A: {len(solo_en_b)} archivo(s)")
        for rel, (_sz, h) in sorted(man_b.items()):
            if h in solo_en_b:
                print(f"   - {rel}")

        if not solo_en_a and not solo_en_b:
            print("\n✅ Mismo contenido en ambos lados (los hashes coinciden por completo).")
    finally:
        _cleanup(tmp_a)
        _cleanup(tmp_b)


# -------------------------------------------------------------- colisiones

def cmd_colisiones(args):
    root, tmp = resolve_root(args.path)
    try:
        manifest = build_manifest(root)
        grupos = defaultdict(list)
        for rel, (size, h) in manifest.items():
            carpeta = os.path.dirname(rel)
            base = normalize_basename(os.path.basename(rel))
            grupos[(carpeta, base)].append((rel, size, h))

        con_variantes = {k: v for k, v in grupos.items() if len(v) > 1}
        conflictivos = {k: v for k, v in con_variantes.items() if len({h for (_, _, h) in v}) > 1}

        print(f"Grupos con nombre base repetido en la misma carpeta: {len(con_variantes)}")
        print(f"De esos, con CONTENIDO DISTINTO pese al nombre similar: {len(conflictivos)}\n")
        print("(Esto no es necesariamente un error -- puede ser una colision de nomenclatura")
        print(" legitima, p.ej. por un sistema que no incluye la hora local en el nombre.")
        print(" Pero significa que NO son duplicados seguros de descartar sin revisar.)\n")

        for (carpeta, base), items in sorted(conflictivos.items()):
            print(f"--- carpeta: {carpeta or '.'} | nombre base: {base} ---")
            for rel, size, h in sorted(items):
                print(f"   {h}  {size:>9}B  {rel}")
            print()
    finally:
        _cleanup(tmp)


# -------------------------------------------------------------- duplicados

def cmd_duplicados(args):
    root, tmp = resolve_root(args.path)
    try:
        manifest = build_manifest(root)
        por_hash = defaultdict(list)
        for rel, (size, h) in manifest.items():
            por_hash[h].append((rel, size))

        dup_reales = {h: v for h, v in por_hash.items() if len(v) > 1}
        total_archivos_duplicados = sum(len(v) for v in dup_reales.values())

        print(f"Archivos totales: {len(manifest)}")
        print(f"Grupos de contenido idéntico (mismo hash, distinta ruta): {len(dup_reales)}")
        print(f"Archivos involucrados en alguna duplicación exacta: {total_archivos_duplicados}\n")

        if args.detalle:
            for h, items in sorted(dup_reales.items(), key=lambda kv: -len(kv[1])):
                print(f"--- hash {h} ({len(items)} copias) ---")
                for rel, size in sorted(items):
                    print(f"   {size:>9}B  {rel}")
                print()
    finally:
        _cleanup(tmp)


# -------------------------------------------------------------- inventario

def extraer_candidatos_inventario(inv_text):
    patron = r"[A-Za-zÀ-ÿ0-9_\-\.\(\) ]+?\.(?:md|json|py|txt|pdf|xlsx|zip)"
    return set(re.findall(patron, inv_text))


def _norm_texto(s):
    return re.sub(r"[_\-\.]", " ", s.lower())


def _norm_nombre(s):
    s = s.lower()
    s = re.sub(r"\.(md|json|py|txt|pdf|xlsx|zip)$", "", s)
    s = re.sub(r"[\s_\-\.]+", " ", s).strip()
    return s


def cmd_inventario(args):
    root, tmp = resolve_root(args.path)
    try:
        manifest = build_manifest(root)
        inv_text = Path(args.inventario).read_text(encoding="utf-8", errors="ignore")
        inv_norm = _norm_texto(inv_text)

        sin_referencia = []
        for rel in manifest:
            base = os.path.basename(rel)
            n = _norm_nombre(base)
            n_sin_sufijo = re.sub(r"\s\(?\d+\)?$", "", n).strip()
            if n in inv_norm or (n_sin_sufijo and n_sin_sufijo in inv_norm):
                continue
            sin_referencia.append(rel)

        candidatos = extraer_candidatos_inventario(inv_text)
        nombres_reales = {os.path.basename(r) for r in manifest}
        patrones_no_ubicados = []
        for c in candidatos:
            c_norm = _norm_nombre(c)
            if not any(_norm_nombre(nr) == c_norm or c_norm in _norm_nombre(nr) for nr in nombres_reales):
                patrones_no_ubicados.append(c)

        reporte = []
        reporte.append("# Reporte de cruce ZIP vs Inventario\n")
        reporte.append(f"- Archivos totales analizados: {len(manifest)}")
        reporte.append(f"- Nombres/patrones detectados en el texto del inventario: {len(candidatos)}")
        reporte.append(f"- Archivos del zip SIN referencia textual aparente en el inventario: {len(sin_referencia)}")
        reporte.append(f"- Nombres del inventario sin archivo real que los explique claramente: {len(patrones_no_ubicados)}\n")
        reporte.append(
            "**Metodología:** heurística de substring sobre el texto plano del inventario, "
            "normalizando guiones/espacios/guiones bajos. NO es semántica: el inventario usa "
            "comodines y rangos (\"s7 a s21\", \"v2 a v5\", \"1 a 5\") que esta heurística puede "
            "no resolver, generando falsos positivos en ambas listas. Revisar cada entrada a "
            "mano antes de tratarla como hallazgo real."
        )
        reporte.append("\n## Archivos del zip sin referencia aparente en el inventario\n")
        for r in sorted(sin_referencia):
            reporte.append(f"- {r}")
        reporte.append("\n## Nombres/patrones del inventario sin archivo real claro\n")
        for p in sorted(patrones_no_ubicados):
            reporte.append(f"- {p}")

        out = "\n".join(reporte)
        if args.output:
            Path(args.output).write_text(out, encoding="utf-8")
            print(f"Reporte guardado en {args.output} ({len(sin_referencia)} sin referencia, revisar a mano)")
        else:
            print(out)
    finally:
        _cleanup(tmp)


# ------------------------------------------------------------------- main

def main():
    parser = argparse.ArgumentParser(
        description="Herramienta de auditoría IRAM: manifest, comparación de zips, colisiones de nombre, duplicados exactos, y cruce contra inventario."
    )
    sub = parser.add_subparsers(dest="comando", required=True)

    p = sub.add_parser("manifest", help="Genera manifest (ruta,tamaño,md5) de un zip o carpeta")
    p.add_argument("path")
    p.add_argument("-o", "--output")
    p.set_defaults(func=cmd_manifest)

    p = sub.add_parser("comparar", help="Compara dos zips/carpetas por contenido (hash), bidireccional")
    p.add_argument("zip_a")
    p.add_argument("zip_b")
    p.set_defaults(func=cmd_comparar)

    p = sub.add_parser("colisiones", help="Archivos con mismo nombre base pero HASH distinto (falsos duplicados)")
    p.add_argument("path")
    p.set_defaults(func=cmd_colisiones)

    p = sub.add_parser("duplicados", help="Archivos con HASH idéntico en más de una ruta (duplicados reales)")
    p.add_argument("path")
    p.add_argument("--detalle", action="store_true", help="Lista cada grupo de duplicados con sus rutas")
    p.set_defaults(func=cmd_duplicados)

    p = sub.add_parser("inventario", help="Cruza contenido real del zip contra un inventario .md")
    p.add_argument("path")
    p.add_argument("inventario")
    p.add_argument("-o", "--output")
    p.set_defaults(func=cmd_inventario)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
