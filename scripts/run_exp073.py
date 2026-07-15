#!/usr/bin/env python3
# EXP073 - FTRT Threshold Sweep

from pathlib import Path
from datetime import datetime, timezone
import csv
import random
import statistics


BASE = Path(__file__).resolve().parent.parent

FTRT_FILE = BASE / "results/csv/ftrt_index_v2.csv"
EVENT_FILE = BASE / "data/catalog/master_catalog.csv"

RESULT = BASE / "experiments/EXP073_threshold_sweep/results"

THRESHOLDS = [0,1,2,3,4,5,6,7]

N_SIM = 10000


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



def count_hits(dates, ftrt, threshold):

    return sum(
        1
        for d in dates
        if d in ftrt and ftrt[d] > threshold
    )



def main():

    RESULT.mkdir(
        parents=True,
        exist_ok=True
    )

    print("="*72)
    print("EXP073 FTRT THRESHOLD SWEEP")
    print("="*72)


    ftrt=load_ftrt()
    events=load_events()


    all_dates=list(ftrt.keys())


    outfile=RESULT/"threshold_sweep.csv"


    with open(outfile,"w",newline="") as f:

        writer=csv.writer(f)

        writer.writerow([
            "timestamp",
            "threshold",
            "observed",
            "null_mean",
            "null_std",
            "z_score",
            "p_value"
        ])


        for threshold in THRESHOLDS:

            observed=count_hits(
                events,
                ftrt,
                threshold
            )


            null=[]


            for i in range(N_SIM):

                sample=random.sample(
                    all_dates,
                    len(events)
                )

                null.append(
                    count_hits(
                        sample,
                        ftrt,
                        threshold
                    )
                )


            mean=statistics.mean(null)

            std=statistics.stdev(null)


            z=(observed-mean)/std if std else 0


            p=sum(
                x>=observed
                for x in null
            )/N_SIM


            writer.writerow([
                datetime.now(timezone.utc).isoformat(),
                threshold,
                observed,
                mean,
                std,
                z,
                p
            ])


            print(
                f"FTRT>{threshold}: "
                f"obs={observed} "
                f"null={mean:.2f} "
                f"z={z:.3f} "
                f"p={p:.4f}"
            )


    print("-"*72)
    print("Archivo:",outfile)
    print("="*72)



if __name__=="__main__":
    main()

