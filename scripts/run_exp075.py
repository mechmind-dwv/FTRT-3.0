#!/usr/bin/env python3
# EXP075 - Active Region Persistence Analysis

from pathlib import Path
from datetime import datetime, timezone
import csv


BASE = Path(__file__).resolve().parent.parent

CATALOG = BASE / "data/catalog/master_catalog.csv"
FTRT_FILE = BASE / "results/csv/ftrt_index_v2.csv"

OUT = BASE / "experiments/EXP075_region_persistence/results"



def load_ftrt():

    data={}

    with open(FTRT_FILE) as f:
        for r in csv.DictReader(f):
            data[r["fecha"]] = float(r["ftrt_index_v2"])

    return data



def load_catalog():

    rows=[]

    with open(CATALOG) as f:
        for r in csv.DictReader(f):
            rows.append(r)

    return rows



def date_diff(a,b):

    from datetime import datetime

    da=datetime.strptime(a,"%Y-%m-%d")
    db=datetime.strptime(b,"%Y-%m-%d")

    return abs((db-da).days)+1



def main():

    OUT.mkdir(
        parents=True,
        exist_ok=True
    )

    print("="*72)
    print("EXP075 ACTIVE REGION PERSISTENCE")
    print("="*72)


    ftrt=load_ftrt()
    rows=load_catalog()


    regions={}


    for r in rows:

        region=r.get(
            "region_activa",
            "UNKNOWN"
        )

        fecha=r["fecha"]


        if region not in regions:
            regions[region]=[]


        regions[region].append(
            fecha
        )


    outfile=OUT/"region_persistence.csv"


    with open(outfile,"w",newline="") as f:

        writer=csv.writer(f)

        writer.writerow([
            "timestamp",
            "region",
            "first_date",
            "last_date",
            "duration_days",
            "events",
            "events_per_day",
            "ftrt_count",
            "mean_ftrt",
            "max_ftrt"
        ])


        for region,dates in regions.items():

            first=min(dates)
            last=max(dates)

            duration=date_diff(
                first,
                last
            )

            values=[
                ftrt[d]
                for d in dates
                if d in ftrt
            ]


            mean=(
                sum(values)/len(values)
                if values else ""
            )

            maximum=(
                max(values)
                if values else ""
            )


            writer.writerow([
                datetime.now(timezone.utc).isoformat(),
                region,
                first,
                last,
                duration,
                len(dates),
                round(len(dates)/duration,4),
                len(values),
                mean,
                maximum
            ])


            print(
                f"{region}: "
                f"{len(dates)} eventos | "
                f"{duration} días | "
                f"FTRT max={maximum}"
            )


    print("-"*72)
    print("Archivo:",outfile)
    print("="*72)



if __name__=="__main__":
    main()

