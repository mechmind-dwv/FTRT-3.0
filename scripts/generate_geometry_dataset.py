"""
Generador del dataset geométrico FTRT
"""

from datetime import date, timedelta
import csv

from ftrt.ephemerides_skyfield import longitudes_sistema
from ftrt.geometry.system_state import construir_estado

INICIO = date(2020, 1, 1)
FIN    = date(2026, 12, 31)

salida = "results/csv/ftrt_geometry_2020_2026.csv"

campos = [
    "fecha",
    "planetas",
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

with open(salida, "w", newline="") as f:

    writer = csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()

    d = INICIO

    while d <= FIN:

        longitudes = longitudes_sistema(d)

        estado = construir_estado(longitudes)

        fila = {
            "fecha": d.isoformat(),
            **estado
        }

        fila["firma_fase"] = ",".join(
            map(str, estado["firma_fase"])
        )

        fila["planetas"] = ",".join(
            estado["planetas"]
        )

        writer.writerow({k: fila[k] for k in campos})

        if d.day == 1:
            print(d)

        d += timedelta(days=1)

print()
print("Dataset terminado.")
print(salida)
