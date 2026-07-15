"""
Inspección del dataset FTRT.
"""

import csv

archivo = "results/csv/ftrt_geometry_2020_2026.csv"

with open(archivo, newline="") as f:

    reader = csv.DictReader(f)
    filas = list(reader)

print("=" * 72)
print("FTRT GEOMETRY DATASET")
print("=" * 72)

print("Registros:", len(filas))
print()

print("Primer registro:")
print(filas[0])

print()

print("Último registro:")
print(filas[-1])

print()

columnas = [
    "lambda_max",
    "energia_resonancia",
    "coherencia_espectral",
    "entropia_espectral",
    "entropia_fase",
]

print("=" * 72)
print("ESTADÍSTICAS")
print("=" * 72)

for c in columnas:

    datos = [float(x[c]) for x in filas]

    print(
        f"{c:<24}"
        f"min={min(datos):8.4f} "
        f"max={max(datos):8.4f} "
        f"media={sum(datos)/len(datos):8.4f}"
    )
