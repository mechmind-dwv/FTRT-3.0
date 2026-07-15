#!/usr/bin/env python3
# EXP081 - Risk Index Validation Against GOES Classes

import csv
from pathlib import Path
from datetime import datetime, timezone


RISK_FILE = Path(
    "experiments/EXP080_composite_risk_index/results/composite_risk_index.csv"
)

REGION_FILE = Path(
    "experiments/EXP066_active_regions/results/active_regions.csv"
)

OUTPUT = Path(
    "experiments/EXP081_risk_validation/results/risk_validation.csv"
)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)


def flare_weight(cls):

    if not cls:
        return 0

    if cls.startswith("X"):
        return 100

    if cls.startswith("M"):
        return 10

    if cls.startswith("C"):
        return 1

    return 0


risk = {}

with open(RISK_FILE, newline="") as f:

    reader = csv.DictReader(f)

    for r in reader:

        risk[r["region"]] = float(
            r["risk_index"]
        )


results = []


with open(REGION_FILE, newline="") as f:

    reader = csv.DictReader(f)

    for r in reader:

        region = r["region_activa"]

        classes = (
            r["classes"]
            .split(";")
            if r["classes"]
            else []
        )

        max_energy = max(
            [
                flare_weight(c)
                for c in classes
            ],
            default=0
        )


        results.append(
            {
                "region": region,
                "risk_index": risk.get(region,0),
                "events": r["events"],
                "max_goes_weight": max_energy,
                "classes": ";".join(classes)
            }
        )


results.sort(
    key=lambda x:x["risk_index"],
    reverse=True
)


with open(OUTPUT,"w",newline="") as f:

    writer = csv.writer(f)

    writer.writerow([
        "timestamp",
        "region",
        "risk_index",
        "events",
        "max_goes_weight",
        "classes"
    ])


    for r in results:

        writer.writerow([
            datetime.now(timezone.utc).isoformat(),
            r["region"],
            r["risk_index"],
            r["events"],
            r["max_goes_weight"],
            r["classes"]
        ])


print("="*72)
print("EXP081 RISK INDEX VALIDATION")
print("="*72)

for r in results:

    print(
        r["region"],
        "risk=",
        r["risk_index"],
        "GOES=",
        r["max_goes_weight"]
    )


print("-"*72)
print("Archivo:", OUTPUT)
print("="*72)

