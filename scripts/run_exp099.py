#!/usr/bin/env python3
# EXP099 - Lag Persistence

from pathlib import Path
import pandas as pd

print("=" * 72)
print("EXP099 LAG PERSISTENCE")
print("=" * 72)

df = pd.read_csv(
    "experiments/EXP097_crosslag_180/results/rolling_crosslag_180.csv"
)

lags = df["best_lag"].tolist()

runs = []
start = 0

for i in range(1, len(lags)):
    if lags[i] != lags[start]:
        runs.append([
            lags[start],
            start,
            i - 1,
            i - start
        ])
        start = i

runs.append([
    lags[start],
    start,
    len(lags) - 1,
    len(lags) - start
])

out = pd.DataFrame(
    runs,
    columns=[
        "lag",
        "start_window",
        "end_window",
        "duration"
    ]
)

out = out.sort_values(
    "duration",
    ascending=False
)

for _, r in out.head(20).iterrows():
    print(
        f"Lag {int(r.lag):>4} "
        f"dur={int(r.duration):4d} "
        f"windows {int(r.start_window)}-{int(r.end_window)}"
    )

dest = Path(
    "experiments/EXP099_lag_persistence/results"
)

dest.mkdir(parents=True, exist_ok=True)

out.to_csv(
    dest / "lag_persistence.csv",
    index=False
)

print("-" * 72)
print("Persistencias:", len(out))
print("Archivo:", dest / "lag_persistence.csv")
print("=" * 72)
