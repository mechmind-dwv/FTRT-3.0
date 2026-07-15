#!/usr/bin/env python3
# EXP096 - Extended Cross Lag (-180..180)

from pathlib import Path
from datetime import datetime, UTC
import pandas as pd
import numpy as np

print("="*72)
print("EXP096 EXTENDED CROSS LAG")
print("="*72)

df = pd.read_csv(
    "experiments/EXP094_rolling_correlation/results/rolling_correlation.csv"
)

rows = []

for lag in range(-180,181):
    sub = df[df["best_lag"] == lag]

    if len(sub) == 0:
        continue

    rows.append([
        datetime.now(UTC).isoformat(),
        lag,
        len(sub),
        round(sub["pearson"].mean(),6),
        round(sub["pearson"].max(),6),
        round(sub["pearson"].min(),6)
    ])

    print(
        f"Lag {lag:>4}: "
        f"windows={len(sub):4d} "
        f"mean={sub['pearson'].mean():7.4f}"
    )

out = Path("experiments/EXP096_extended_crosslag/results")
out.mkdir(parents=True, exist_ok=True)

pd.DataFrame(
    rows,
    columns=[
        "timestamp",
        "lag",
        "windows",
        "mean_pearson",
        "max_pearson",
        "min_pearson"
    ]
).to_csv(out/"extended_crosslag.csv", index=False)

print("-"*72)
print("Archivo:", out/"extended_crosslag.csv")
print("="*72)
