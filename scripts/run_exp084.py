#!/usr/bin/env python3
# EXP084 - Precursor Persistence Model

import csv
from pathlib import Path
from datetime import datetime

CATALOG="data/catalog/master_catalog.csv"
FTRT="results/csv/ftrt_index_v2.csv"

OUT="experiments/EXP084_precursor_persistence/results/precursor_persistence.csv"


def load_ftrt():

    data={}

    with open(FTRT) as f:
        r=csv.DictReader(f)

        for row in r:
            try:
                data[row["fecha"]] = float(row["ftrt_index_v2"])
            except:
                pass

    return data



def main():

    print("="*72)
    print("EXP084 PRECURSOR PERSISTENCE MODEL")
    print("="*72)


    ftrt=load_ftrt()


    events=[]

    with open(CATALOG) as f:

        r=csv.DictReader(f)

        for row in r:
            events.append(row)


    Path(OUT).parent.mkdir(
        parents=True,
        exist_ok=True
    )


    rows=[]


    for e in events:

        date=e["fecha"]
        region=e["region_activa"]

        values=[]

        for lag in range(-14,1):

            try:

                from datetime import timedelta

                d=datetime.strptime(
                    date,
                    "%Y-%m-%d"
                ) + timedelta(days=lag)

                key=d.strftime("%Y-%m-%d")

                if key in ftrt:
                    values.append(
                        ftrt[key]
                    )

            except:
                pass


        if values:

            mean=sum(values)/len(values)
            mx=max(values)

        else:

            mean=0
            mx=0


        rows.append({

            "timestamp":
            datetime.now().isoformat(),

            "date":
            date,

            "region":
            region,

            "days_window":
            len(values),

            "mean_pre14":
            round(mean,6),

            "max_pre14":
            round(mx,6)

        })


    with open(
        OUT,
        "w",
        newline=""
    ) as f:

        w=csv.DictWriter(
            f,
            fieldnames=rows[0].keys()
        )

        w.writeheader()
        w.writerows(rows)


    print("Eventos:",len(rows))

    for r in rows[:10]:

        print(
            r["region"],
            "mean=",
            r["mean_pre14"],
            "max=",
            r["max_pre14"]
        )


    print("-"*72)
    print("Archivo:",OUT)
    print("="*72)



if __name__=="__main__":
    main()
