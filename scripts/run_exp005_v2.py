#!/usr/bin/env python3

import csv
import math

INPUT = "results/csv/ftrt_silso.csv"

train = []
test = []

with open(INPUT, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        try:
            fila = {
                "fecha": r["fecha"],
                "x": float(r["entropia_fase"]),
                "y": float(r["ssn"])
            }
        except Exception:
            continue

        if fila["fecha"] < "2025-01-01":
            train.append(fila)
        else:
            test.append(fila)

n = len(train)

mx = sum(r["x"] for r in train) / n
my = sum(r["y"] for r in train) / n

num = sum((r["x"]-mx)*(r["y"]-my) for r in train)
den = sum((r["x"]-mx)**2 for r in train)

b = num / den if den != 0 else 0.0
a = my - b * mx

mae = 0.0
mse = 0.0

for r in test:
    pred = a + b * r["x"]
    err = pred - r["y"]
    mae += abs(err)
    mse += err * err

mae /= len(test)
rmse = math.sqrt(mse / len(test))

print("=" * 72)
print("EXP005 v2 - REGRESIÓN LINEAL")
print("=" * 72)
print(f"a = {a:.4f}")
print(f"b = {b:.4f}")
print(f"MAE  = {mae:.3f}")
print(f"RMSE = {rmse:.3f}")
print("=" * 72)
