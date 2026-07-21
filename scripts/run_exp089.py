#!/usr/bin/env python3
# EXP089 - Solar Cycle Memory Autocorrelation

import csv
from pathlib import Path
import numpy as np


SRC=Path(
"experiments/EXP088_solar_long_memory/results/solar_long_memory.csv"
)

OUT=Path(
"experiments/EXP089_solar_autocorrelation/results/autocorrelation.csv"
)


def main():

    values=[]

    with open(SRC) as f:
        for r in csv.DictReader(f):
            values.append(
                float(r["mean_ssn"])
            )


    rows=[]

    for lag in [1,3,6,12,24,60,132]:

        a=np.array(values[:-lag])
        b=np.array(values[lag:])

        corr=np.corrcoef(a,b)[0,1]

        rows.append([
            lag,
            corr
        ])


    OUT.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(OUT,"w") as f:

        w=csv.writer(f)

        w.writerow([
            "lag_months",
            "correlation"
        ])

        w.writerows(rows)


    print("="*72)
    print("EXP089 SOLAR MEMORY AUTOCORRELATION")
    print("="*72)

    for r in rows:
        print(
            "Lag",
            r[0],
            "months:",
            round(r[1],4)
        )

    print("Archivo:",OUT)



if __name__=="__main__":
    main()
