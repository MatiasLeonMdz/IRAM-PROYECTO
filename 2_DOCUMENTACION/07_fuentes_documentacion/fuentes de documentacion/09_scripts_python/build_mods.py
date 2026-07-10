#!/usr/bin/env python3
"""
build_mods.py — Generador de zips del ecosistema Drago Mod Pack para Imperator Roma
Uso: python build_mods.py
Salida: mod.zip en el mismo directorio que este script

Validación BOM:
  .txt y .yml  → deben tener BOM (UTF-8 sig)
  .mod         → no deben tener BOM
"""

import os
import sys
import zipfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_ZIP = os.path.join(SCRIPT_DIR, "mod.zip")

ROOT_MOD_FILES = [
    "exodos.mod",
    "by_other_means.mod",
    "the_last_vote.mod",
    "the_great_leap.mod",
]

MOD_FOLDERS = [
    "exodos",
    "by_other_means",
    "the_last_vote",
    "the_great_leap",
]

BOM_EXTENSIONS    = {".txt", ".yml"}   # deben tener BOM
NO_BOM_EXTENSIONS = {".mod"}           # no deben tener BOM
BOM = b"\xef\xbb\xbf"


def check_bom(path):
    with open(path, "rb") as f:
        return f.read(3) == BOM


def validate_file(path):
    """
    Retorna lista de errores BOM para el archivo dado.
    """
    ext = os.path.splitext(path)[1].lower()
    errors = []
    if ext in BOM_EXTENSIONS:
        if not check_bom(path):
            errors.append(f"MISSING BOM: {path}")
    elif ext in NO_BOM_EXTENSIONS:
        if check_bom(path):
            errors.append(f"BOM PRESENT (should not be): {path}")
    return errors


def collect_files():
    files = []
    for fn in ROOT_MOD_FILES:
        fp = os.path.join(SCRIPT_DIR, fn)
        if not os.path.exists(fp):
            print(f"WARNING: {fn} not found — skipping")
            continue
        files.append(fp)
    for folder in MOD_FOLDERS:
        folder_path = os.path.join(SCRIPT_DIR, folder)
        if not os.path.exists(folder_path):
            print(f"WARNING: folder {folder}/ not found — skipping")
            continue
        for root, dirs, filenames in os.walk(folder_path):
            for fn in filenames:
                files.append(os.path.join(root, fn))
    return files


def validate_all(files):
    """Validate all files BEFORE writing any zip. Returns errors list."""
    errors = []
    for fp in files:
        errors.extend(validate_file(fp))
    return errors


def build_zip(files):
    included = []
    with zipfile.ZipFile(OUTPUT_ZIP, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for fp in files:
            arcname = os.path.relpath(fp, SCRIPT_DIR)
            zf.write(fp, arcname)
            included.append(arcname)
    return included


def main():
    print("build_mods.py — Drago Mod Pack — Imperator Roma")
    print(f"Output: {OUTPUT_ZIP}")
    print()
    files = collect_files()
    if not files:
        print("ERROR: No files found. Run this script from the mod root directory.")
        sys.exit(1)

    # Validate first — abort before creating zip if errors found
    errors = validate_all(files)
    if errors:
        print(f"BOM ERRORS ({len(errors)}) — zip NOT generated:")
        for e in errors:
            print(f"  {e}")
        sys.exit(1)

    # All clear — now build the zip
    included = build_zip(files)
    print(f"Files included ({len(included)}):")
    for f in sorted(included):
        print(f"  {f}")
    print()
    print(f"BOM validation: OK — {len(included)} archivos validados")
    print("Done: mod.zip generated successfully")


if __name__ == "__main__":
    main()
