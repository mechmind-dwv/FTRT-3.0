#!/usr/bin/env python3

import subprocess
import sys

PASOS = [
    (
        "Estado geométrico JPL",
        "PYTHONPATH=src python scripts/test_jpl_state.py"
    ),
    (
        "Validación dataset",
        "python scripts/validate_geometry_dataset.py"
    ),
    (
        "Control de calidad",
        "python scripts/qc_geometry_dataset.py"
    ),
    (
        "Manifest",
        "python scripts/experiment_manifest.py"
    ),
    (
        "Run report",
        "python scripts/run_report.py"
    ),
]

print("=" * 72)
print("FTRT COMPLETE VALIDATION")
print("=" * 72)

for titulo, comando in PASOS:

    print(f"\n>>> {titulo}")

    r = subprocess.run(comando, shell=True)

    if r.returncode != 0:
        print(f"\nERROR en: {titulo}")
        sys.exit(r.returncode)

print("\n" + "=" * 72)
print("VALIDACIÓN COMPLETA SUPERADA")
print("=" * 72)
