#!/usr/bin/env python3

import csv
import math
import os

INPUT="results/csv/ftrt_silso.csv"
OUT="experiments/EXP002_lag_analysis/results/lag_results.csv"

VARIABLES=[
    "lambda_max",
    "lambda_min",
    "energia_resonancia",
    "coherencia_espectral",
    "entropia_espectral",
    "estados_fase",
    "entropia_fase",
    "concentracion_fase"
]

def pearson(x,y):
    n=len(x)
    if n<3:
        return 0.0

    mx=sum(x)/n
    my=sum(y)/n

    num=0.0
    dx=0.0
    dy=0.0

    for a,b in zip(x,y):
        xa=a-mx
        yb=b-my
        num+=xa*yb
        dx+=xa*xa
        dy+=yb*yb

    if dx==0 or dy==0:
        return 0.0

    return num/math.sqrt(dx*dy)


rows=[]

with open(INPUT,newline="") as f:
    for r in csv.DictReader(f):
        rows.append(r)

os.makedirs(os.path.dirname(OUT),exist_ok=True)

with open(OUT,"w",newline="") as f:

    writer=csv.writer(f)
    writer.writerow(["variable","lag","pearson"])

    print("="*72)
    print("EXP002 LAG ANALYSIS")
    print("="*72)

    for var in VARIABLES:

        mejor_r=0.0
        mejor_lag=0

        for lag in range(-90,91):

            xs=[]
            ys=[]

            for i in range(len(rows)):

                j=i+lag

                if j<0 or j>=len(rows):
                    continue

                xs.append(float(rows[i][var]))
                ys.append(float(rows[j]["ssn"]))

            r=pearson(xs,ys)

            writer.writerow([var,lag,r])

            if abs(r)>abs(mejor_r):
                mejor_r=r
                mejor_lag=lag

        print(f"{var:25s} lag={mejor_lag:4d}  r={mejor_r: .5f}")

print("="*72)
print("Resultados:",OUT)
