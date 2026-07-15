#!/usr/bin/env python3
# EXP092 - FTRT vs GOES Energy Cross Lag

from datetime import datetime, UTC
from pathlib import Path
import pandas as pd
import numpy as np

print("=" * 72)
print("EXP092 FTRT vs GOES ENERGY CROSS LAG")
print("=" * 72)

ftrt = pd.read_csv("results/csv/ftrt_index_v2.csv")
events = pd.read_csv("data/catalog/master_catalog.csv")

ftrt["fecha"] = pd.to_datetime(ftrt["fecha"])
events["fecha"] = pd.to_datetime(events["fecha"])

def goes_weight(clase):
    if pd.isna(clase):
        return 0.0
    clase = str(clase).strip().upper()
    if len(clase) < 2:
        return 0.0
    try:
        mag = float(clase[1:])
    except Exception:
        return 0.0

    if clase.startswith("X"):
        return mag * 100.0
    if clase.startswith("M"):
        return mag * 10.0
    if clase.startswith("C"):
        return mag
    return 0.0

events["energy"] = events["clase"].apply(goes_weight)

energy = (
    events.groupby("fecha")["energy"]
    .sum()
    .reset_index()
)

df = pd.merge(ftrt, energy, on="fecha", how="left").fillna(0)

rows = []
best_lag = 0
best_r = -999.0

for lag in range(-30, 31):

    if lag < 0:
        x = df["ftrt_index_v2"].iloc[-lag:].to_numpy()
        y = df["energy"].iloc[:len(x)].to_numpy()
    elif lag > 0:
        x = df["ftrt_index_v2"].iloc[:-lag].to_numpy()
        y = df["energy"].iloc[lag:].to_numpy()
    else:
        x = df["ftrt_index_v2"].to_numpy()
        y = df["energy"].to_numpy()

    if len(x) < 10:
        continue

    if np.std(x) == 0 or np.std(y) == 0:
        r = 0.0
    else:
        r = float(np.corrcoef(x, y)[0,1])

    if np.isnan(r):
        r = 0.0

    rows.append([
        datetime.now(UTC).isoformat(),
        lag,
        round(r,6),
        len(x)
    ])

    print(f"Lag {lag:>3}: Pearson={r:7.4f} n={len(x)}")

    if abs(r) > abs(best_r):
        best_r = r
        best_lag = lag

out = Path("experiments/EXP092_goes_energy_crosslag/results")
out.mkdir(parents=True, exist_ok=True)

pd.DataFrame(
    rows,
    columns=["timestamp","lag_days","pearson","samples"]
).to_csv(out/"cross_lag_goes_energy.csv", index=False)

print("-"*72)
print("MEJOR LAG:", best_lag)
print("PEARSON :", round(best_r,4))
print("Archivo :", out/"cross_lag_goes_energy.csv")
print("="*72)
