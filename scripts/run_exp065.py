#!/usr/bin/env python3
# EXP065 - Global Statistics

from pathlib import Path
import csv
import statistics
from datetime import datetime, timezone


BASE = Path(__file__).resolve().parent.parent

INPUT = BASE / "experiments/EXP064_master_catalog/results/master_catalog_v2.csv"

OUT = BASE / "experiments/EXP065_global_statistics/results"


def percentile(data, p):

    if not data:
        return None

    data = sorted(data)

    k = (len(data)-1) * p
    f = int(k)
    c = min(f+1, len(data)-1)

    if f == c:
        return data[int(k)]

    return data[f] + (data[c]-data[f])*(k-f)



def main():

    print("="*72)
    print("EXP065 GLOBAL STATISTICS")
    print("="*72)


    OUT.mkdir(parents=True, exist_ok=True)


    with open(INPUT,newline="") as f:
        rows=list(csv.DictReader(f))


    ftrt=[]

    classes={}

    class_values={}


    for r in rows:

        clase=r["clase"]

        classes[clase]=classes.get(clase,0)+1

        class_values.setdefault(clase,[])


        if r["ftrt"]:

            value=float(r["ftrt"])

            ftrt.append(value)
            class_values[clase].append(value)



    stats={

        "timestamp":datetime.now(timezone.utc).isoformat(),

        "events_total":len(rows),

        "events_with_ftrt":len(ftrt),

        "ftrt_mean":statistics.mean(ftrt) if ftrt else None,

        "ftrt_std":statistics.stdev(ftrt) if len(ftrt)>1 else None,

        "ftrt_min":min(ftrt) if ftrt else None,

        "ftrt_max":max(ftrt) if ftrt else None,

        "ftrt_median":statistics.median(ftrt) if ftrt else None,

        "p25":percentile(ftrt,0.25),

        "p75":percentile(ftrt,0.75),

    }


    with open(OUT/"global_statistics.csv","w",newline="") as f:

        writer=csv.writer(f)

        writer.writerow(["metric","value"])

        for k,v in stats.items():

            writer.writerow([k,v])


    with open(OUT/"class_statistics.csv","w",newline="") as f:

        writer=csv.writer(f)

        writer.writerow([
            "class",
            "events",
            "ftrt_events",
            "mean_ftrt"
        ])

        for c,n in classes.items():

            vals=class_values[c]

            writer.writerow([
                c,
                n,
                len(vals),
                statistics.mean(vals) if vals else ""
            ])



    print("-"*72)
    print(f"Eventos totales : {len(rows)}")
    print(f"Con FTRT        : {len(ftrt)}")

    if ftrt:

        print(f"Media FTRT      : {statistics.mean(ftrt):.6f}")
        print(f"STD FTRT        : {statistics.stdev(ftrt):.6f}")
        print(f"Min FTRT        : {min(ftrt):.6f}")
        print(f"Max FTRT        : {max(ftrt):.6f}")
        print(f"Mediana         : {statistics.median(ftrt):.6f}")

    print("-"*72)
    print("Clases GOES")

    for c,n in classes.items():

        print(f"{c}: {n}")

    print("="*72)

    print(
        "Archivo:",
        OUT/"global_statistics.csv"
    )


if __name__=="__main__":
    main()

