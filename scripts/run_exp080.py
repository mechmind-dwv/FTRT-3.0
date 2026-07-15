#!/usr/bin/env python3
# EXP080 - Composite Regional Risk Index

import csv
from pathlib import Path
from datetime import datetime, timezone


INPUT = Path(
    "experiments/EXP079_region_activity_correlation/results/region_activity_correlation.csv"
)

OUTPUT = Path(
    "experiments/EXP080_composite_risk_index/results/composite_risk_index.csv"
)


OUTPUT.parent.mkdir(parents=True, exist_ok=True)


rows = []

with open(INPUT, newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)


def safe_float(x):
    try:
        return float(x)
    except:
        return 0.0


max_activity = max(
    safe_float(r["activity_score"])
    for r in rows
)

max_ftrt = max(
    safe_float(r["max_ftrt"])
    for r in rows
)


results = []


for r in rows:

    activity = safe_float(r["activity_score"])
    persistence = safe_float(r["persistence_index"])
    intensity = safe_float(r["max_ftrt"])

    activity_norm = (
        activity / max_activity
        if max_activity else 0
    )

    intensity_norm = (
        intensity / max_ftrt
        if max_ftrt else 0
    )


    risk = round(
        activity_norm *
        persistence *
        intensity_norm,
        5
    )


    results.append(
        {
            "region": r["region"],
            "events": r["events"],
            "activity_score": activity,
            "persistence_index": persistence,
            "max_ftrt": intensity,
            "risk_index": risk
        }
    )


results.sort(
    key=lambda x: x["risk_index"],
    reverse=True
)


with open(OUTPUT, "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow([
        "timestamp",
        "region",
        "events",
        "activity_score",
        "persistence_index",
        "max_ftrt",
        "risk_index"
    ])

    for r in results:

        writer.writerow([
            datetime.now(timezone.utc).isoformat(),
            r["region"],
            r["events"],
            r["activity_score"],
            r["persistence_index"],
            r["max_ftrt"],
            r["risk_index"]
        ])


print("="*72)
print("EXP080 COMPOSITE REGIONAL RISK INDEX")
print("="*72)

for r in results:

    print(
        r["region"],
        "events=", r["events"],
        "risk=", r["risk_index"]
    )

print("-"*72)
print("Archivo:", OUTPUT)
print("="*72)

