"""
Validación básica del dataset FTRT.
"""

import csv

archivo = "results/csv/ftrt_geometry_2020_2026.csv"

with open(archivo, newline="") as f:
    filas = list(csv.DictReader(f))

print("=" * 72)
print("VALIDACIÓN DEL DATASET")
print("=" * 72)

print("Número de registros:", len(filas))
print("Primer día :", filas[0]["fecha"])
print("Último día :", filas[-1]["fecha"])

esperadas = [
    "fecha",
    "lambda_max",
    "lambda_min",
    "energia_resonancia",
    "rango",
    "entropia_espectral",
    "coherencia_espectral",
    "estados_fase",
    "entropia_fase",
    "concentracion_fase",
    "firma_fase",
]

print("\nColumnas presentes:")

for c in esperadas:
    print(f"{c:<24} {'OK' if c in filas[0] else 'FALTA'}")

print("\nDataset válido.")
