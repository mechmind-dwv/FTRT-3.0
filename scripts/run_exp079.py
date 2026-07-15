#!/usr/bin/env python3
# EXP079 - Region Activity FTRT Persistence Correlation

import csv
from pathlib import Path
from datetime import datetime, timezone


INPUT = Path(
    "experiments/EXP078_region_temporal_memory/results/region_temporal_memory.csv"
)

OUTPUT = Path(
    "experiments/EXP079_region_activity_correlation/results/region_activity_correlation.csv"
)


OUTPUT.parent.mkdir(parents=True, exist_ok=True)


rows = []


with open(INPUT, newline="") as f:
    reader = csv.DictReader(f)

    for r in reader:
        rows.append(r)


with open(OUTPUT, "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow([
        "timestamp",
        "region",
        "events",
        "duration_days",
        "events_per_day",
        "ftrt_days",
        "high_ftrt_days",
        "persistence_index",
        "mean_ftrt",
        "max_ftrt",
        "activity_score",
        "ftrt_activity_ratio"
    ])


    for r in rows:

        events = int(r["events"])
        duration = int(r["duration_days"])
        ftrt_days = int(r["ftrt_days"])
        high_days = int(r["high_ftrt_days"])

        mean_ftrt = r["mean_ftrt"]
        max_ftrt = r["max_ftrt"]


        activity_score = round(
            events / duration,
            4
        )


        ratio = 0

        if events > 0:
            ratio = round(
                high_days / events,
                4
            )


        writer.writerow([
            datetime.now(timezone.utc).isoformat(),
            r["region"],
            events,
            duration,
            r["events_per_day"],
            ftrt_days,
            high_days,
            r["persistence_index"],
            mean_ftrt,
            max_ftrt,
            activity_score,
            ratio
        ])


print("="*72)
print("EXP079 REGION ACTIVITY FTRT PERSISTENCE CORRELATION")
print("="*72)

for r in rows:

    print(
        r["region"],
        "events=", r["events"],
        "activity=", r["events_per_day"],
        "persistence=", r["persistence_index"]
    )

print("-"*72)
print("Archivo:", OUTPUT)
print("="*72)

