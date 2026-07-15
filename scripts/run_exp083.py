#!/usr/bin/env python3
# EXP083.1 - Precursor Window Risk Analysis FIX

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
    return datetime.strptime(
        x,
        "%Y-%m-%d"
    ).date()


ftrt = {}

with open(FTRT_FILE,newline="") as f:

    reader = csv.DictReader(f)

    for r in reader:

        try:
            ftrt[
                parse_date(r["fecha"])
            ] = float(
                r["ftrt_index_v2"]
            )

        except:
            pass



events=[]

with open(EVENT_FILE,newline="") as f:

    reader=csv.DictReader(f)

    for r in reader:

        events.append(r)



windows=[-7,-3,-1,0]


results=[]


for e in events:

    event_date=parse_date(
        e["fecha"]
    )

    region=e["region_activa"]


    for lag in windows:

        target=event_date + timedelta(
            days=lag
        )

        value=ftrt.get(
            target,
            0
        )


        results.append(
            {
                "event_date":str(event_date),
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
print("EXP083.1 PRECURSOR WINDOW ANALYSIS FIX")
print("="*72)


for lag in windows:

    values=[
        r["ftrt"]
        for r in results
        if r["lag_days"]==lag
    ]

    hits=sum(
        1 for x in values if x>1.5
    )

    print(
        "Lag",
        lag,
        "days:",
        "events=",
        len(values),
        "hits=",
        hits
    )


print("-"*72)
print("Archivo:",OUTPUT)
print("="*72)

