#!/usr/bin/env python3
# EXP097 - Rolling Cross-Lag Search (-180..180 days)

from pathlib import Path
from datetime import datetime, UTC
import pandas as pd
import numpy as np

print("=" * 72)
print("EXP097 ROLLING CROSS-LAG (-180..180 DAYS)")
print("=" * 72)

WINDOW = 180
MAX_LAG = 180

df = pd.read_csv("results/csv/ftrt_index_v2.csv")
df["fecha"] = pd.to_datetime(df["fecha"])
df = df.sort_values("fecha").reset_index(drop=True)

rows = []

for start in range(0, len(df) - WINDOW):

    sub = df.iloc[start:start + WINDOW].copy()

    best_lag = 0
    best_r = 0.0

    for lag in range(-MAX_LAG, MAX_LAG + 1):

        if lag < 0:
            x = sub["ftrt_index_v2"].iloc[-lag:].to_numpy()
            y = sub["ssn"].iloc[:len(x)].to_numpy()
        elif lag > 0:
            x = sub["ftrt_index_v2"].iloc[:-lag].to_numpy()
            y = sub["ssn"].iloc[lag:].to_numpy()
        else:
            x = sub["ftrt_index_v2"].to_numpy()
            y = sub["ssn"].to_numpy()

        if len(x) < 30:
            continue

        r = np.corrcoef(x, y)[0, 1]

        if np.isnan(r):
            continue

        if best_lag == 0 && best_r == 0.0 or abs(r) > abs(best_r):
            best_r = float(r)
            best_lag = lag

    rows.append([
        datetime.now(UTC).isoformat(),
        sub.iloc[0]["fecha"].date(),
        sub.iloc[-1]["fecha"].date(),
        best_lag,
        round(best_r,6)
    ])

    print(
        f"{sub.iloc[0]['fecha'].date()} -> "
        f"{sub.iloc[-1]['fecha'].date()} | "
        f"Lag={best_lag:>4} | r={best_r:7.4f}"
    )

out = Path("experiments/EXP097_crosslag_180/results")
out.mkdir(parents=True, exist_ok=True)

pd.DataFrame(
    rows,
    columns=[
        "timestamp",
        "window_start",
        "window_end",
        "best_lag",
        "pearson"
    ]
).to_csv(out/"rolling_crosslag_180.csv", index=False)

print("-"*72)
print("Ventanas analizadas:", len(rows))
print("Archivo:", out/"rolling_crosslag_180.csv")
print("="*72)
