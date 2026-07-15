#!/usr/bin/env python3
# EXP068 - Global Metrics Dashboard

from pathlib import Path
import csv
from collections import Counter
from datetime import datetime, timezone


BASE = Path(__file__).resolve().parent.parent

INPUT = BASE / "experiments/EXP067_prediction_history/results/prediction_history.csv"

OUT = BASE / "experiments/EXP068_global_metrics/results"



def main():

    print("="*72)
    print("EXP068 GLOBAL METRICS DASHBOARD")
    print("="*72)


    OUT.mkdir(parents=True, exist_ok=True)


    with open(INPUT,newline="") as f:
        rows=list(csv.DictReader(f))


    total=len(rows)


    with_ftrt=[
        r for r in rows
        if r["ftrt"] != ""
    ]


    risks=Counter(
        r["risk_level"]
        for r in rows
    )


    regions=Counter(
        r["region_activa"]
        for r in rows
    )


    metrics={

        "timestamp":
            datetime.now(timezone.utc).isoformat(),

        "events_total":
            total,

        "events_with_ftrt":
            len(with_ftrt),

        "ftrt_coverage_percent":
            round(
                len(with_ftrt)/total*100,
                3
            ),

        "LOW":
            risks["LOW"],

        "MODERATE":
            risks["MODERATE"],

        "HIGH":
            risks["HIGH"],

        "EXTREME":
            risks["EXTREME"],

        "UNKNOWN":
            risks["UNKNOWN"],

        "regions":
            len(regions),

        "top_region":
            regions.most_common(1)[0][0]

    }


    output=OUT/"global_metrics.csv"


    with open(output,"w",newline="") as f:

        writer=csv.writer(f)

        writer.writerow(
            ["metric","value"]
        )

        for k,v in metrics.items():

            writer.writerow(
                [k,v]
            )



    print("-"*72)

    for k,v in metrics.items():

        print(
            f"{k:30}: {v}"
        )


    print("-"*72)

    print("Archivo:")
    print(output)

    print("="*72)



if __name__=="__main__":
    main()

