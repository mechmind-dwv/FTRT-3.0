#!/usr/bin/env python3

# EXP077 - Region Contribution Analysis

import csv
from pathlib import Path
from datetime import datetime

INPUT = Path(
"experiments/EXP075_region_persistence/results/region_persistence.csv"
)

OUT = Path(
"experiments/EXP077_region_contribution/results/region_contribution.csv"
)

OUT.parent.mkdir(parents=True, exist_ok=True)


rows=[]

with open(INPUT) as f:
    data=list(csv.DictReader(f))


total_ftrt=sum(
    float(x["mean_ftrt"])
    for x in data
    if x["mean_ftrt"]
)

for r in data:

    value=float(r["mean_ftrt"]) if r["mean_ftrt"] else 0

    contribution=(
        value/total_ftrt*100
        if total_ftrt else 0
    )

    rows.append({
        "timestamp":datetime.utcnow().isoformat()+"Z",
        "region":r["region"],
        "events":r["events"],
        "duration_days":r["duration_days"],
        "mean_ftrt":value,
        "contribution_percent":round(contribution,3)
    })


rows.sort(
    key=lambda x:x["contribution_percent"],
    reverse=True
)


with open(OUT,"w",newline="") as f:
    w=csv.DictWriter(
        f,
        fieldnames=rows[0].keys()
    )
    w.writeheader()
    w.writerows(rows)


print("="*72)
print("EXP077 REGION CONTRIBUTION ANALYSIS")
print("="*72)

for r in rows:
    print(
        f'{r["region"]}: '
        f'{r["contribution_percent"]}% '
        f'events={r["events"]}'
    )

print("-"*72)
print("Archivo:",OUT)
print("="*72)

