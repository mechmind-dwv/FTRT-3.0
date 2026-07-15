#!/usr/bin/env python3
# EXP078 - Region Temporal Memory Analysis

import csv
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict
from datetime import date

INPUT = Path(
    "experiments/EXP064_master_catalog/results/master_catalog_v2.csv"
)

OUTPUT = Path(
    "experiments/EXP078_region_temporal_memory/results/region_temporal_memory.csv"
)

THRESHOLD = 1.5


def parse_date(x):
    return date.fromisoformat(x)


regions = defaultdict(list)


with open(INPUT, newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        region = row["region_activa"]

        if region == "":
            region = "UNKNOWN"

        regions[region].append(row)


OUTPUT.parent.mkdir(parents=True, exist_ok=True)


with open(OUTPUT, "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow([
        "timestamp",
        "region",
        "duration_days",
        "events",
        "events_per_day",
        "ftrt_days",
        "high_ftrt_days",
        "persistence_index",
        "mean_ftrt",
        "max_ftrt"
    ])


    for region, events in regions.items():

        dates = [
            parse_date(e["fecha"])
            for e in events
        ]

        duration = (
            max(dates)-min(dates)
        ).days + 1


        ftrt_values=[]

        for e in events:
            try:
                ftrt=float(e["ftrt"])
                ftrt_values.append(ftrt)
            except:
                pass


        ftrt_days=len(ftrt_values)

        high_days=len(
            [
                x for x in ftrt_values
                if x > THRESHOLD
            ]
        )


        persistence=0

        if duration>0:
            persistence=round(
                high_days/duration,
                4
            )


        mean_ftrt=""

        max_ftrt=""

        if ftrt_values:
            mean_ftrt=round(
                sum(ftrt_values)/len(ftrt_values),
                6
            )

            max_ftrt=max(ftrt_values)


        writer.writerow([
            datetime.now(timezone.utc).isoformat(),
            region,
            duration,
            len(events),
            round(len(events)/duration,4),
            ftrt_days,
            high_days,
            persistence,
            mean_ftrt,
            max_ftrt
        ])


print("="*72)
print("EXP078 REGION TEMPORAL MEMORY")
print("="*72)

for region, events in regions.items():
    print(
        region,
        "events=",len(events)
    )

print("-"*72)
print("Archivo:", OUTPUT)
print("="*72)
