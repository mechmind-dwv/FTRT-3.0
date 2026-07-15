"""
Genera un manifiesto del experimento FTRT.
"""

import csv
import hashlib

archivo = "results/csv/ftrt_geometry_2020_2026.csv"

with open(archivo, "rb") as f:
    sha = hashlib.sha256(f.read()).hexdigest()

with open(archivo, newline="") as f:
    filas = list(csv.DictReader(f))

print("=" * 72)
print("FTRT EXPERIMENT MANIFEST")
print("=" * 72)

print("Dataset :", archivo)
print("SHA256  :", sha)
print("Registros:", len(filas))
print("Inicio  :", filas[0]["fecha"])
print("Fin     :", filas[-1]["fecha"])

print("\nVariables:")

for c in filas[0].keys():
    print(" -", c)

print("\nManifest generado correctamente.")
