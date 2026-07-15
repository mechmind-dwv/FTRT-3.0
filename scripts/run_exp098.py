#!/usr/bin/env python3
# EXP098 - Lag Timeline

from pathlib import Path
import pandas as pd

print("=" * 72)
print("EXP098 LAG TIMELINE")
print("=" * 72)

df = pd.read_csv(
    "experiments/EXP097_crosslag_180/results/rolling_crosslag_180.csv"
)

date_col = df.columns[0]

summary = (
    df.groupby("best_lag")
      .agg(
          windows=("best_lag", "count"),
          mean_r=("pearson", "mean"),
          first_date=(date_col, "min"),
          last_date=(date_col, "max"),
      )
      .reset_index()
      .sort_values("windows", ascending=False)
)

for _, row in summary.head(20).iterrows():
    print(
        f"Lag {int(row.best_lag):>4}: "
        f"windows={int(row.windows):4d} "
        f"mean_r={row.mean_r:7.4f} "
        f"{row.first_date} -> {row.last_date}"
    )

out = Path("experiments/EXP098_lag_timeline/results")
out.mkdir(parents=True, exist_ok=True)

summary.to_csv(out / "lag_timeline.csv", index=False)

print("-" * 72)
print("Total lags :", len(summary))
print("Archivo:", out / "lag_timeline.csv")
print("=" * 72)
