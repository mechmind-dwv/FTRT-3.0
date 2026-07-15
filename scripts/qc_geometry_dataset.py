"""
Control de calidad del dataset FTRT.
"""

import csv
from math import isnan

archivo = "results/csv/ftrt_geometry_2020_2026.csv"

filas = list(csv.DictReader(open(archivo)))

print("=" * 72)
print("QUALITY CONTROL")
print("=" * 72)

print("Registros:", len(filas))

numericas = [
    "lambda_max",
    "lambda_min",
    "energia_resonancia",
    "entropia_espectral",
    "coherencia_espectral",
    "entropia_fase",
    "concentracion_fase",
]

for campo in numericas:

    errores = 0

    for fila in filas:

        try:
            x = float(fila[campo])

            if isnan(x):
                errores += 1

        except Exception:
            errores += 1

    print(f"{campo:<24}: {errores} errores")

print()

fechas = [f["fecha"] for f in filas]

if len(fechas) == len(set(fechas)):
    print("✓ No hay fechas duplicadas.")
else:
    print("✗ Existen fechas duplicadas.")

print("QC finalizado.")
