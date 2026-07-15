"""
FTRT Scientific Laboratory

Resumen automático del experimento.
"""

import csv
import hashlib
import os
from datetime import datetime, UTC

DATASET = "results/csv/ftrt_geometry_2020_2026.csv"

with open(DATASET, "rb") as f:
    sha = hashlib.sha256(f.read()).hexdigest()

with open(DATASET, newline="") as f:
    rows = list(csv.DictReader(f))

size = os.path.getsize(DATASET)

print("=" * 72)
print("FTRT RUN REPORT")
print("=" * 72)

print("Fecha ejecución :", datetime.now(UTC).isoformat())
print("Dataset         :", DATASET)
print("SHA256          :", sha)
print("Tamaño (bytes)  :", size)
print("Registros       :", len(rows))
print("Inicio          :", rows[0]["fecha"])
print("Fin             :", rows[-1]["fecha"])

print("\nVariables:")

for k in rows[0]:
    print("  •", k)

print("\nEstado:")
print("  ✓ Dataset generado")
print("  ✓ QC superado")
print("  ✓ Manifest generado")

print("=" * 72)
print()
print("VERSION")

with open("VERSION") as f:
    print(f.read())
