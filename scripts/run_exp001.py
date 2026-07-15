#!/usr/bin/env python3

import csv
import math

GEOM = "results/csv/ftrt_geometry_2020_2026.csv"
SILSO = "data/silso/silso_daily.csv"
OUT = "experiments/EXP001_geometry_vs_sunspots/results/merged_dataset.csv"


def leer_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


geom = leer_csv(GEOM)
silso = leer_csv(SILSO)

# Índice por fecha
silso_fecha = {}
for fila in silso:
    silso_fecha[fila["fecha"]] = fila

merged = []

for g in geom:
    if g["fecha"] in silso_fecha:
        fila = dict(g)
        fila.update(silso_fecha[g["fecha"]])
        merged.append(fila)

if not merged:
    raise SystemExit("No hay fechas comunes entre ambos datasets.")

# Buscar automáticamente la columna de manchas solares
sunspot = None
for c in merged[0]:
    n = c.lower()
    if "sun" in n or "spot" in n or "ssn" in n:
        sunspot = c
        break

if sunspot is None:
    raise SystemExit("No se encontró la columna de manchas solares.")

variables = [
    "lambda_max",
    "lambda_min",
    "energia_resonancia",
    "coherencia_espectral",
    "entropia_espectral",
    "estados_fase",
    "entropia_fase",
    "concentracion_fase",
]

def pearson(x, y):
    n = len(x)
    mx = sum(x)/n
    my = sum(y)/n

    num = sum((a-mx)*(b-my) for a,b in zip(x,y))

    denx = math.sqrt(sum((a-mx)**2 for a in x))
    deny = math.sqrt(sum((b-my)**2 for b in y))

    if denx == 0 or deny == 0:
        return float("nan")

    return num/(denx*deny)

print("="*72)
print("EXP001 GEOMETRY vs SUNSPOTS")
print("="*72)

y = [float(r[sunspot]) for r in merged]

for v in variables:
    x = [float(r[v]) for r in merged]
    print(f"{v:25s} {pearson(x,y): .5f}")

with open(OUT,"w",newline="",encoding="utf-8") as f:
    w = csv.DictWriter(f,fieldnames=merged[0].keys())
    w.writeheader()
    w.writerows(merged)

print("="*72)
print("Registros:",len(merged))
print("Resultado:",OUT)
