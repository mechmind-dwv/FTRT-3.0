#!/usr/bin/env python3
# EXP095 - Best Lag Distribution

from pathlib import Path
from datetime import datetime, UTC
import pandas as pd

print("=" * 72)
print("EXP095 BEST LAG DISTRIBUTION")
print("=" * 72)

df = pd.read_csv(
    "experiments/EXP094_rolling_correlation/results/rolling_correlation.csv"
)

counts = (
    df.groupby("best_lag")
      .agg(
          windows=("best_lag", "count"),
          mean_r=("pearson", "mean"),
          max_r=("pearson", "max"),
          min_r=("pearson", "min"),
      )
      .reset_index()
      .sort_values("best_lag")
)

counts["timestamp"] = datetime.now(UTC).isoformat()

for _, row in counts.iterrows():
    print(
        f"Lag {int(row.best_lag):>3}: "
        f"windows={int(row.windows):4d} "
        f"mean_r={row.mean_r:7.4f} "
        f"max_r={row.max_r:7.4f}"
    )

print("-" * 72)
print("Media lag   :", round(df["best_lag"].mean(), 3))
print("Mediana lag :", round(df["best_lag"].median(), 3))
print("Std lag     :", round(df["best_lag"].std(), 3))
print("Moda lag    :", int(df["best_lag"].mode().iloc[0]))

out = Path("experiments/EXP095_lag_distribution/results")
out.mkdir(parents=True, exist_ok=True)

counts.to_csv(out / "lag_distribution.csv", index=False)

print("Archivo:", out / "lag_distribution.csv")
print("=" * 72)
