#!/usr/bin/env python3
# EXP082 - Temporal Memory Risk Model v2

import csv
from pathlib import Path
from datetime import datetime, timezone


RISK_FILE = Path(
    "experiments/EXP080_composite_risk_index/results/composite_risk_index.csv"
)

GOES_FILE = Path(
    "experiments/EXP081_risk_validation/results/risk_validation.csv"
)

OUTPUT = Path(
    "experiments/EXP082_risk_memory_model/results/risk_memory_v2.csv"
)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)


def f(x):
    try:
        return float(x)
    except:
        return 0.0


def energy_memory(weight):

    # factor memoria energética
    if weight >= 100:
        return 2.0

    if weight >= 10:
        return 1.5

    if weight >= 1:
        return 1.1

    return 1.0


risk = {}

with open(RISK_FILE, newline="") as file:

    reader = csv.DictReader(file)

    for r in reader:

        risk[r["region"]] = {
            "risk": f(r["risk_index"]),
            "activity": f(r["activity_score"]),
            "persistence": f(r["persistence_index"]),
            "ftrt": f(r["max_ftrt"])
        }


results = []


with open(GOES_FILE, newline="") as file:

    reader = csv.DictReader(file)

    for r in reader:

        region = r["region"]

        base = risk.get(
            region,
            {
                "risk":0,
                "activity":0,
                "persistence":0,
                "ftrt":0
            }
        )


        memory = energy_memory(
            f(r["max_goes_weight"])
        )


        risk_v2 = round(
            base["risk"] * memory,
            5
        )


        results.append(
            {
                "region":region,
                "base_risk":base["risk"],
                "goes_memory":memory,
                "risk_v2":risk_v2,
                "max_goes":r["max_goes_weight"],
                "events":r["events"]
            }
        )


results.sort(
    key=lambda x:x["risk_v2"],
    reverse=True
)


with open(OUTPUT,"w",newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "timestamp",
        "region",
        "events",
        "base_risk",
        "goes_memory",
        "max_goes",
        "risk_v2"
    ])


    for r in results:

        writer.writerow([
            datetime.now(timezone.utc).isoformat(),
            r["region"],
            r["events"],
            r["base_risk"],
            r["goes_memory"],
            r["max_goes"],
            r["risk_v2"]
        ])


print("="*72)
print("EXP082 TEMPORAL MEMORY RISK MODEL v2")
print("="*72)


for r in results:

    print(
        r["region"],
        "risk_v2=",
        r["risk_v2"],
        "GOES=",
        r["max_goes"]
    )


print("-"*72)
print("Archivo:", OUTPUT)
print("="*72)

