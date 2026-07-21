#!/usr/bin/env python3
# EXP087 - Carrington Rotation Memory Search

import csv
from pathlib import Path
from datetime import datetime, date

CAT=Path("data/catalog/master_catalog.csv")

OUT=Path(
"experiments/EXP087_carrington_memory/results/carrington_memory.csv"
)

MIN_DAYS=20
MAX_DAYS=40


def lat(value):

    try:
        if value.startswith("N"):
            return float(value[1:])
        if value.startswith("S"):
            return -float(value[1:])
    except:
        return None


def load():

    data=[]

    with open(CAT) as f:

        for r in csv.DictReader(f):

            try:
                r["d"]=date.fromisoformat(r["fecha"])
            except:
                continue

            r["lat"]=lat(
                r["latitud_longitud"]
            )

            try:
                r["ftrt"]=float(r["ftrt"])
            except:
                r["ftrt"]=0

            data.append(r)

    return data


def main():

    rows=load()
    result=[]


    for i,a in enumerate(rows):

        for b in rows[i+1:]:

            days=(b["d"]-a["d"]).days


            if MIN_DAYS <= days <= MAX_DAYS:

                if a["lat"] is None or b["lat"] is None:
                    continue


                lat_diff=abs(
                    a["lat"]-b["lat"]
                )


                if lat_diff <= 15:

                    score=(
                        abs(a["ftrt"])
                        +
                        abs(b["ftrt"])
                    )/2


                    result.append([
                        datetime.now().isoformat(),
                        a["fecha"],
                        a["region_activa"],
                        b["fecha"],
                        b["region_activa"],
                        days,
                        lat_diff,
                        score
                    ])


    OUT.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    with open(OUT,"w") as f:

        w=csv.writer(f)

        w.writerow([
            "timestamp",
            "date_a",
            "region_a",
            "date_b",
            "region_b",
            "rotation_days",
            "lat_difference",
            "memory_score"
        ])

        w.writerows(result)


    print("="*72)
    print("EXP087 CARRINGTON ROTATION MEMORY")
    print("="*72)
    print("Eventos:",len(rows))
    print("Candidatos:",len(result))
    print("Archivo:",OUT)


if __name__=="__main__":
    main()
