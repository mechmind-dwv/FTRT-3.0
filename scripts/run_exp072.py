#!/usr/bin/env python3
# EXP072 - Monte Carlo Temporal Null Model

from pathlib import Path
from datetime import datetime, timezone
import csv
import random
import statistics


BASE = Path(__file__).resolve().parent.parent


FTRT_FILE = BASE / "results/csv/ftrt_index_v2.csv"

EVENT_FILE = BASE / "data/catalog/master_catalog.csv"


RESULT = BASE / "experiments/EXP072_monte_carlo_null/results"


N_SIM = 10000

THRESHOLD = 1.5


def load_ftrt():

    days=[]

    with open(FTRT_FILE) as f:

        reader=csv.DictReader(f)

        for r in reader:

            days.append(
                {
                    "fecha": r["fecha"],
                    "ftrt": float(r["ftrt_index_v2"])
                }
            )

    return days



def load_events():

    events=[]

    with open(EVENT_FILE) as f:

        reader=csv.DictReader(f)

        for r in reader:

            events.append(
                r["fecha"]
            )

    return events



def count_hits(selected_dates, ftrt_map):

    hits=0

    for d in selected_dates:

        if d in ftrt_map and ftrt_map[d] > THRESHOLD:

            hits+=1

    return hits



def main():

    RESULT.mkdir(
        parents=True,
        exist_ok=True
    )


    print("="*72)
    print("EXP072 MONTE CARLO TEMPORAL NULL MODEL")
    print("="*72)


    ftrt_days=load_ftrt()

    events=load_events()


    ftrt_map={
        x["fecha"]:x["ftrt"]
        for x in ftrt_days
    }


    observed=count_hits(
        events,
        ftrt_map
    )


    print("Días FTRT:",len(ftrt_days))
    print("Eventos:",len(events))
    print("Umbral:",THRESHOLD)
    print("Hits observados:",observed)


    all_dates=list(ftrt_map.keys())


    null=[]


    for i in range(N_SIM):

        random_dates=random.sample(
            all_dates,
            len(events)
        )


        hits=count_hits(
            random_dates,
            ftrt_map
        )


        null.append(hits)



    mean_null=statistics.mean(null)

    std_null=statistics.stdev(null)


    z=(observed-mean_null)/std_null if std_null else 0


    p=sum(
        x>=observed
        for x in null
    )/N_SIM


    outfile=RESULT/"monte_carlo_results.csv"


    with open(outfile,"w",newline="") as f:

        writer=csv.writer(f)

        writer.writerow(
            [
                "timestamp",
                "events",
                "observed_hits",
                "null_mean",
                "null_std",
                "z_score",
                "p_value"
            ]
        )


        writer.writerow(
            [
                datetime.now(timezone.utc).isoformat(),
                len(events),
                observed,
                mean_null,
                std_null,
                z,
                p
            ]
        )


    print("-"*72)
    print("Simulaciones:",N_SIM)
    print("Media nula:",mean_null)
    print("STD nula:",std_null)
    print("Z:",z)
    print("p-value:",p)
    print("-"*72)
    print("Archivo:",outfile)
    print("="*72)



if __name__=="__main__":
    main()

