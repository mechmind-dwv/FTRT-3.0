#!/usr/bin/env python3
# EXP088 - Solar Long Memory Analysis 1818-2026

import csv
from pathlib import Path
from datetime import datetime
from collections import defaultdict


SRC=Path("data/silso/silso_daily.csv")

OUT=Path(
"experiments/EXP088_solar_long_memory/results/solar_long_memory.csv"
)


def load():

    months=defaultdict(list)

    with open(SRC) as f:

        for r in csv.DictReader(f):

            try:
                ssn=float(r["ssn"])
            except:
                continue

            if ssn < 0:
                continue

            month=r["fecha"][:7]

            months[month].append(ssn)


    return months



def main():

    data=load()

    OUT.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    rows=[]

    for month,values in sorted(data.items()):

        mean=sum(values)/len(values)

        rows.append([
            month,
            len(values),
            round(mean,3),
            max(values)
        ])


    with open(OUT,"w") as f:

        w=csv.writer(f)

        w.writerow([
            "month",
            "days",
            "mean_ssn",
            "max_ssn"
        ])

        w.writerows(rows)



    print("="*72)
    print("EXP088 SOLAR LONG MEMORY")
    print("="*72)
    print("Months:",len(rows))
    print("First:",rows[0])
    print("Last:",rows[-1])
    print("Archivo:",OUT)



if __name__=="__main__":
    main()
