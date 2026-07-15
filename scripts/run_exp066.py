#!/usr/bin/env python3
# EXP066 - Active Region Analysis

from pathlib import Path
import csv
import statistics
from datetime import datetime, timezone


BASE = Path(__file__).resolve().parent.parent

INPUT = BASE / "experiments/EXP064_master_catalog/results/master_catalog_v2.csv"

OUT = BASE / "experiments/EXP066_active_regions/results"


def main():

    print("="*72)
    print("EXP066 ACTIVE REGION ANALYSIS")
    print("="*72)


    OUT.mkdir(parents=True, exist_ok=True)


    with open(INPUT,newline="") as f:
        rows=list(csv.DictReader(f))


    regions={}


    for r in rows:

        ar=r.get("region_activa","")

        if not ar:
            ar="UNKNOWN"


        if ar not in regions:

            regions[ar]={
                "events":0,
                "ftrt":[],
                "classes":[]
            }


        regions[ar]["events"]+=1

        regions[ar]["classes"].append(r["clase"])


        if r.get("ftrt"):

            regions[ar]["ftrt"].append(
                float(r["ftrt"])
            )



    output=[]


    for ar,data in regions.items():

        values=data["ftrt"]


        output.append({

            "region_activa":ar,

            "events":data["events"],

            "ftrt_events":len(values),

            "mean_ftrt":
                statistics.mean(values)
                if values else "",

            "max_ftrt":
                max(values)
                if values else "",

            "classes":
                ";".join(data["classes"])

        })



    output.sort(
        key=lambda x:
        float(x["max_ftrt"])
        if x["max_ftrt"] else 0,
        reverse=True
    )


    file=OUT/"active_regions.csv"


    with open(file,"w",newline="") as f:

        writer=csv.DictWriter(
            f,
            fieldnames=output[0].keys()
        )

        writer.writeheader()
        writer.writerows(output)



    print("-"*72)
    print(f"Eventos analizados : {len(rows)}")
    print(f"Regiones detectadas: {len(regions)}")
    print("-"*72)

    print("TOP REGIONES FTRT")

    for r in output[:10]:

        print(
            r["region_activa"],
            "eventos=",r["events"],
            "maxFTRT=",r["max_ftrt"]
        )


    print("="*72)

    print("Archivo:",file)



if __name__=="__main__":
    main()

