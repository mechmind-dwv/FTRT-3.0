#!/usr/bin/env python3
# EXP100 - Lag Cluster Analysis

from pathlib import Path
import pandas as pd

print("=" * 72)
print("EXP100 LAG CLUSTER ANALYSIS")
print("=" * 72)

df = pd.read_csv(
    "experiments/EXP097_crosslag_180/results/rolling_crosslag_180.csv"
)

targets = {
    "Carrington (~27)": (24, 30),
    "2x Carrington (~54)": (51, 57),
    "3x Carrington (~81)": (78, 84),
    "4x Carrington (~108)": (105, 111),
    "5x Carrington (~135)": (132, 138),
    "Semiannual (~182)": (175, 180),
}

rows = []

for name, (a, b) in targets.items():

    sub = df[df["best_lag"].abs().between(a, b)]

    print(f"{name:24s} windows={len(sub):5d}")

    rows.append([
        name,
        a,
        b,
        len(sub),
        round(sub["pearson"].mean(), 6) if len(sub) else 0.0,
        round(sub["pearson"].max(), 6) if len(sub) else 0.0,
    ])

out = Path("experiments/EXP100_lag_clusters/results")
out.mkdir(parents=True, exist_ok=True)

pd.DataFrame(
    rows,
    columns=[
        "cluster",
        "lag_min",
        "lag_max",
        "windows",
        "mean_r",
        "max_r",
    ],
).to_csv(out / "lag_clusters.csv", index=False)

print("-" * 72)
print("Archivo:", out / "lag_clusters.csv")
print("=" * 72)
