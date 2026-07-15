#!/usr/bin/env python3
# EXP094 - Rolling Correlation (90-day windows)

from datetime import datetime, UTC
from pathlib import Path
import pandas as pd
import numpy as np

print("="*72)
print("EXP094 ROLLING FTRT-SSN CORRELATION")
print("="*72)

df = pd.read_csv("results/csv/ftrt_index_v2.csv")
df["fecha"] = pd.to_datetime(df["fecha"])
df = df.sort_values("fecha").reset_index(drop=True)

WINDOW = 90
MAX_LAG = 30

rows = []

for start in range(0, len(df)-WINDOW+1):

    block = df.iloc[start:start+WINDOW]

    best_lag = None
    best_r = None

    for lag in range(-MAX_LAG, MAX_LAG+1):

        if lag < 0:
            x = block["ftrt_index_v2"].iloc[-lag:].to_numpy()
            y = block["ssn"].iloc[:len(x)].to_numpy()
        elif lag > 0:
            x = block["ftrt_index_v2"].iloc[:-lag].to_numpy()
            y = block["ssn"].iloc[lag:].to_numpy()
        else:
            x = block["ftrt_index_v2"].to_numpy()
            y = block["ssn"].to_numpy()

        if len(x) < 30:
            continue

        if np.std(x) == 0 or np.std(y) == 0:
            continue

        r = float(np.corrcoef(x, y)[0,1])

        if np.isnan(r):
            continue

        if best_r is None or abs(r) > abs(best_r):
            best_r = r
            best_lag = lag

    rows.append([
        datetime.now(UTC).isoformat(),
        block.iloc[0]["fecha"].date(),
        block.iloc[-1]["fecha"].date(),
        best_lag,
        round(best_r,6) if best_r is not None else None
    ])

    print(
        f"{block.iloc[0]['fecha'].date()} -> "
        f"{block.iloc[-1]['fecha'].date()} | "
        f"Lag={best_lag:>3} | "
        f"r={best_r:.4f}"
    )

out = Path("experiments/EXP094_rolling_correlation/results")
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
).to_csv(out/"rolling_correlation.csv", index=False)

print("-"*72)
print("Ventanas analizadas:", len(rows))
print("Archivo:", out/"rolling_correlation.csv")
print("="*72)
