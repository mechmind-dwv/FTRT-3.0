#!/usr/bin/env python3
# EXP091 - FTRT vs GOES Cross Lag Correlation

from datetime import datetime, UTC
import pandas as pd
import numpy as np
from pathlib import Path

print("=" * 72)
print("EXP091 FTRT vs GOES CROSS LAG")
print("=" * 72)

ftrt = pd.read_csv("results/csv/ftrt_index_v2.csv")
events = pd.read_csv("data/catalog/master_catalog.csv")

ftrt["fecha"] = pd.to_datetime(ftrt["fecha"])
events["fecha"] = pd.to_datetime(events["fecha"])

goes = (
    events.groupby("fecha")["clase"]
    .count()
    .reset_index(name="goes_events")
)

df = pd.merge(ftrt, goes, on="fecha", how="left").fillna(0)

best_lag = 0
best_r = 0.0
rows = []

for lag in range(-30, 31):

    if lag < 0:
        x = df["ftrt_index_v2"].iloc[-lag:].to_numpy()
        y = df["goes_events"].iloc[:len(x)].to_numpy()
    elif lag > 0:
        x = df["ftrt_index_v2"].iloc[:-lag].to_numpy()
        y = df["goes_events"].iloc[lag:].to_numpy()
    else:
        x = df["ftrt_index_v2"].to_numpy()
        y = df["goes_events"].to_numpy()

    if len(x) < 10:
        continue

    r = np.corrcoef(x, y)[0, 1]
    if np.isnan(r):
        r = 0.0

    rows.append([
        datetime.now(UTC).isoformat(),
        lag,
        round(float(r), 6),
        len(x)
    ])

    print(f"Lag {lag:>3}: Pearson={r:7.4f} n={len(x)}")

    if abs(r) > abs(best_r):
        best_r = r
        best_lag = lag

out = Path("experiments/EXP091_ftrt_goes_crosslag/results")
out.mkdir(parents=True, exist_ok=True)

pd.DataFrame(
    rows,
    columns=["timestamp","lag_days","pearson","samples"]
).to_csv(out/"cross_lag_goes.csv", index=False)

print("-" * 72)
print("MEJOR LAG:", best_lag)
print("PEARSON :", round(best_r,4))
print("Archivo:", out/"cross_lag_goes.csv")
print("=" * 72)
