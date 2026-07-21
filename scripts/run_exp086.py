#!/usr/bin/env python3
# EXP086 - Solar Rotation Memory Linking

import csv
from pathlib import Path
from datetime import datetime
from datetime import date

CAT = Path("data/catalog/master_catalog.csv")

OUT = Path(
"experiments/EXP086_rotation_memory/results/rotation_memory_candidates.csv"
)

ROT_MIN = 20
ROT_MAX = 35


def parse_lat(value):

    try:
        if value.startswith("N"):
            return float(value[1:])
        if value.startswith("S"):
            return -float(value[1:])
    except:
        pass

    return None


def load():

    rows=[]

    with open(CAT) as f:

        for r in csv.DictReader(f):

            try:
                r["date_obj"] = date.fromisoformat(r["fecha"])
            except:
                continue

            r["lat"] = parse_lat(
                r.get("latitud_longitud","")
            )

            try:
                r["ftrt_val"] = float(r["ftrt"])
            except:
                r["ftrt_val"] = 0

            rows.append(r)

    return rows


def main():

    rows=load()

    candidates=[]


    for i,a in enumerate(rows):

        for b in rows[i+1:]:

            gap=(b["date_obj"]-a["date_obj"]).days


            if ROT_MIN <= gap <= ROT_MAX:


                lat_ok=False

                if a["lat"] is not None and b["lat"] is not None:
                    lat_ok=abs(a["lat"]-b["lat"]) <= 10


                if lat_ok:

                    memory=(
                        abs(a["ftrt_val"])
                        +
                        abs(b["ftrt_val"])
                    ) / 2


                    candidates.append([
                        datetime.now().isoformat(),
                        a["fecha"],
                        a["region_activa"],
                        b["fecha"],
                        b["region_activa"],
                        gap,
                        a["lat"],
                        b["lat"],
                        round(memory,6)
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
            "rotation_gap_days",
            "lat_a",
            "lat_b",
            "memory_score"
        ])

        w.writerows(candidates)


    print("="*72)
    print("EXP086 SOLAR ROTATION MEMORY LINKING")
    print("="*72)

    print("Eventos:",len(rows))
    print("Candidatos:",len(candidates))

    for c in candidates[:20]:

        print(
            c[2],
            "->",
            c[4],
            "gap=",
            c[5],
            "memory=",
            c[8]
        )

    print("-"*72)
    print("Archivo:",OUT)


if __name__=="__main__":
    main()
