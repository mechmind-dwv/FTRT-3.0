#!/usr/bin/env python3
# EXP085 - Active Region Control Group Validation

import csv
from pathlib import Path
from datetime import datetime

CAT = Path("data/catalog/master_catalog.csv")
OUT = Path("experiments/EXP085_active_region_control/results/control_validation.csv")

def load():
    rows=[]
    with open(CAT) as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows

def main():

    rows=load()

    regions={}

    for r in rows:
        reg=r.get("region_activa","UNKNOWN")

        if reg not in regions:
            regions[reg]={
                "events":0,
                "ftrt":[],
                "classes":[]
            }

        regions[reg]["events"]+=1

        try:
            regions[reg]["ftrt"].append(float(r["ftrt"]))
        except:
            pass

        regions[reg]["classes"].append(r["clase"])

    OUT.parent.mkdir(parents=True,exist_ok=True)

    with open(OUT,"w") as f:

        w=csv.writer(f)

        w.writerow([
            "timestamp",
            "region",
            "events",
            "mean_ftrt",
            "max_ftrt",
            "eruption_score"
        ])

        for reg,data in regions.items():

            vals=data["ftrt"]

            mean=sum(vals)/len(vals) if vals else 0
            mx=max(vals) if vals else 0

            score=len(data["classes"])*mx

            w.writerow([
                datetime.now().isoformat(),
                reg,
                len(data["classes"]),
                round(mean,6),
                round(mx,6),
                round(score,6)
            ])

            print(
                reg,
                "events=",len(data["classes"]),
                "mean=",round(mean,3),
                "max=",round(mx,3),
                "score=",round(score,3)
            )


    print("-"*72)
    print("Archivo:",OUT)


if __name__=="__main__":
    main()
