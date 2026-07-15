#!/usr/bin/env python3
# EXP083 - Precursor Window Risk Analysis

import csv
from pathlib import Path
from datetime import datetime, timezone, timedelta


FTRT_FILE = Path(
    "results/csv/ftrt_index_v2.csv"
)

EVENT_FILE = Path(
    "data/catalog/master_catalog.csv"
)

OUTPUT = Path(
    "experiments/EXP083_precursor_window/results/precursor_window.csv"
)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)


def parse_date(x):
    return datetime.fromisoformat(
        x[:10]
    ).date()


def get_ftrt(row):

    for key in ["ftrt","FTRT","ftrt_index"]:

        if key in row:

            try:
                return float(row[key])
            except:
                return 0

    return 0


# cargar serie FTRT

ftrt = {}

with open(FTRT_FILE,newline="") as f:

    reader = csv.DictReader(f)

    for r in reader:

        try:

            d = parse_date(
                r["date"]
            )

            ftrt[d] = get_ftrt(r)

        except:
            pass


results=[]


windows=[
    -7,
    -3,
    -1,
    0
]


with open(EVENT_FILE,newline="") as f:

    reader=csv.DictReader(f)


    for event in reader:

        try:

            date=parse_date(
                event["date"]
            )

        except:

            continue


        region = event.get(
            "region_activa",
            "UNKNOWN"
        )


        for lag in windows:

            target = date + timedelta(
                days=lag
            )

            value=ftrt.get(
                target,
                0
            )


            results.append(
                {
                    "event_date":str(date),
                    "region":region,
                    "lag_days":lag,
                    "ftrt":value
                }
            )


with open(OUTPUT,"w",newline="") as f:

    writer=csv.writer(f)

    writer.writerow(
        [
            "timestamp",
            "event_date",
            "region",
            "lag_days",
            "ftrt"
        ]
    )


    for r in results:

        writer.writerow(
            [
                datetime.now(timezone.utc).isoformat(),
                r["event_date"],
                r["region"],
                r["lag_days"],
                r["ftrt"]
            ]
        )


print("="*72)
print("EXP083 PRECURSOR WINDOW ANALYSIS")
print("="*72)


for lag in windows:

    values=[
        r["ftrt"]
        for r in results
        if r["lag_days"]==lag
    ]

    hits=sum(
        1 for v in values if v>1.5
    )

    print(
        "Lag",
        lag,
        "days:",
        "events=",
        len(values),
        "FTRT hits=",
        hits
    )


print("-"*72)
print("Archivo:",OUTPUT)
print("="*72)

