#!/usr/bin/env python3
# EXP093 - Solar Cycle Phase Cross Lag

from datetime import datetime, UTC
from pathlib import Path
import pandas as pd
import numpy as np

print("="*72)
print("EXP093 SOLAR CYCLE PHASE CROSS LAG")
print("="*72)

df = pd.read_csv("results/csv/ftrt_index_v2.csv")
df["fecha"] = pd.to_datetime(df["fecha"])

ssn = df["ssn"]

q1 = ssn.quantile(0.33)
q2 = ssn.quantile(0.66)

phases = {
    "LOW": df[df["ssn"] <= q1],
    "MID": df[(df["ssn"] > q1) & (df["ssn"] <= q2)],
    "HIGH": df[df["ssn"] > q2],
}

rows=[]

for phase,p in phases.items():

    best_lag=None
    best_r=None

    print("-"*72)
    print(phase)

    for lag in range(-30,31):

        if lag<0:
            x=p["ftrt_index_v2"].iloc[-lag:].to_numpy()
            y=p["ssn"].iloc[:len(x)].to_numpy()
        elif lag>0:
            x=p["ftrt_index_v2"].iloc[:-lag].to_numpy()
            y=p["ssn"].iloc[lag:].to_numpy()
        else:
            x=p["ftrt_index_v2"].to_numpy()
            y=p["ssn"].to_numpy()

        if len(x)<30:
            continue

        if np.std(x)==0 or np.std(y)==0:
            continue

        r=float(np.corrcoef(x,y)[0,1])

        if np.isnan(r):
            continue

        if best_r is None or abs(r)>abs(best_r):
            best_r=r
            best_lag=lag

    print("BEST LAG :",best_lag)
    print("PEARSON  :",round(best_r,4))

    rows.append([
        datetime.now(UTC).isoformat(),
        phase,
        best_lag,
        round(best_r,6),
        len(p)
    ])

out=Path("experiments/EXP093_cycle_phase_crosslag/results")
out.mkdir(parents=True,exist_ok=True)

pd.DataFrame(
    rows,
    columns=[
        "timestamp",
        "phase",
        "best_lag",
        "pearson",
        "samples"
    ]
).to_csv(out/"cycle_phase_crosslag.csv",index=False)

print("="*72)
print("Archivo:",out/"cycle_phase_crosslag.csv")
print("="*72)
