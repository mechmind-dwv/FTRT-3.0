#!/usr/bin/env python3
# EXP074 - Temporal Lag Analysis

from pathlib import Path
from datetime import datetime, timezone
import csv


BASE = Path(__file__).resolve().parent.parent

FTRT_FILE = BASE / "results/csv/ftrt_index_v2.csv"
EVENT_FILE = BASE / "data/catalog/master_catalog.csv"

OUT = BASE / "experiments/EXP074_lag_analysis/results"


LAGS = [-7,-3,-1,0,1,3,7]


def load_ftrt():

    data={}

    with open(FTRT_FILE) as f:
        for r in csv.DictReader(f):
            data[r["fecha"]] = float(r["ftrt_index_v2"])

    return data



def load_events():

    events=[]

    with open(EVENT_FILE) as f:
        for r in csv.DictReader(f):
            events.append(r["fecha"])

    return events



def shift_date(date,days):

    from datetime import datetime,timedelta

    d=datetime.strptime(
        date,
        "%Y-%m-%d"
    )

    return (
        d + timedelta(days=days)
    ).strftime("%Y-%m-%d")



def main():

    OUT.mkdir(
        parents=True,
        exist_ok=True
    )

    print("="*72)
    print("EXP074 TEMPORAL LAG ANALYSIS")
    print("="*72)


    ftrt=load_ftrt()
    events=load_events()


    outfile=OUT/"lag_analysis.csv"


    with open(outfile,"w",newline="") as f:

        writer=csv.writer(f)

        writer.writerow([
            "timestamp",
            "lag_days",
            "events",
            "with_ftrt",
            "mean_ftrt",
            "max_ftrt"
        ])


        for lag in LAGS:

            values=[]


            for event in events:

                day=shift_date(
                    event,
                    lag
                )

                if day in ftrt:
                    values.append(
                        ftrt[day]
                    )


            mean = (
                sum(values)/len(values)
                if values else ""
            )

            maximum = (
                max(values)
                if values else ""
            )


            writer.writerow([
                datetime.now(timezone.utc).isoformat(),
                lag,
                len(events),
                len(values),
                mean,
                maximum
            ])


            print(
                f"Lag {lag:+d} días | "
                f"FTRT {len(values)} | "
                f"media {mean}"
            )


    print("-"*72)
    print("Archivo:",outfile)
    print("="*72)



if __name__=="__main__":
    main()

