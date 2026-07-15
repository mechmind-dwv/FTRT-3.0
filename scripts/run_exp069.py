#!/usr/bin/env python3
# EXP069 - Final Scientific Report

from pathlib import Path
import csv
from datetime import datetime, timezone


BASE = Path(__file__).resolve().parent.parent

OUT = BASE / "experiments/EXP069_final_report/results"

FILES = {

    "catalog":
    BASE / "experiments/EXP064_master_catalog/results/master_catalog_v2.csv",

    "statistics":
    BASE / "experiments/EXP065_global_statistics/results/global_statistics.csv",

    "regions":
    BASE / "experiments/EXP066_active_regions/results/active_regions.csv",

    "history":
    BASE / "experiments/EXP067_prediction_history/results/prediction_history.csv",

    "metrics":
    BASE / "experiments/EXP068_global_metrics/results/global_metrics.csv"

}


def count_csv(path):

    with open(path,newline="") as f:
        return len(list(csv.DictReader(f)))



def main():

    print("="*72)
    print("EXP069 FINAL SCIENTIFIC REPORT")
    print("="*72)

    OUT.mkdir(parents=True,exist_ok=True)

    report = OUT / "FTRT_scientific_report.md"


    lines=[]

    lines.append("# FTRT-3.0 Scientific Report\n")

    lines.append(
        "Generated: "
        + datetime.now(timezone.utc).isoformat()
        + "\n"
    )


    lines.append("\n## Pipeline Status\n")

    for name,path in FILES.items():

        exists=path.exists()

        lines.append(
            f"- {name}: "
            f"{'OK' if exists else 'MISSING'}\n"
        )



    lines.append("\n## Dataset Summary\n")

    lines.append(
        f"- Master catalog events: "
        f"{count_csv(FILES['catalog'])}\n"
    )

    lines.append(
        f"- Prediction history rows: "
        f"{count_csv(FILES['history'])}\n"
    )

    lines.append(
        f"- Active regions: "
        f"{count_csv(FILES['regions'])}\n"
    )



    lines.append("\n## Experiments Completed\n")

    experiments=[
        "EXP061 JOIN EXPANSION",
        "EXP062 DONKI UPDATE",
        "EXP063 FTRT UPDATE",
        "EXP064 MASTER CATALOG",
        "EXP065 GLOBAL STATISTICS",
        "EXP066 ACTIVE REGION ANALYSIS",
        "EXP067 PREDICTION HISTORY",
        "EXP068 GLOBAL METRICS"
    ]


    for e in experiments:
        lines.append(f"- {e}\n")



    lines.append(
        "\n## Reproducibility\n"
    )

    lines.append(
        "- Data generated automatically\n"
    )

    lines.append(
        "- Results stored under experiments/\n"
    )

    lines.append(
        "- Git checkpoints available\n"
    )



    with open(report,"w") as f:

        f.writelines(lines)



    print("-"*72)

    print("Report generated:")

    print(report)

    print("="*72)



if __name__=="__main__":
    main()

