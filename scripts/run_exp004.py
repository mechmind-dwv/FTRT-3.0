#!/usr/bin/env python3

import csv
import math
import random

INPUT="results/csv/ftrt_silso.csv"

VARIABLES=[
    "lambda_max",
    "energia_resonancia",
    "coherencia_espectral",
    "entropia_espectral",
    "estados_fase",
    "entropia_fase",
    "concentracion_fase"
]

N_SIM=1000

def pearson(x,y):
    n=len(x)
    if n<3:
        return 0.0

    mx=sum(x)/n
    my=sum(y)/n

    num=dx=dy=0.0

    for a,b in zip(x,y):
        xa=a-mx
        yb=b-my
        num+=xa*yb
        dx+=xa*xa
        dy+=yb*yb

    if dx==0 or dy==0:
        return 0.0

    return num/math.sqrt(dx*dy)

rows=list(csv.DictReader(open(INPUT)))

print("="*72)
print("EXP004 MONTE CARLO")
print("="*72)

for var in VARIABLES:

    x=[float(r[var]) for r in rows]
    y=[float(r["ssn"]) for r in rows]

    r_obs=pearson(x,y)

    superiores=0

    for _ in range(N_SIM):

        ys=y[:]
        random.shuffle(ys)

        r=pearson(x,ys)

        if abs(r)>=abs(r_obs):
            superiores+=1

    p=(superiores+1)/(N_SIM+1)

    print(f"{var:24s} r={r_obs: .5f}   p={p:.4f}")

print("="*72)
print("Monte Carlo terminado")
print("="*72)
