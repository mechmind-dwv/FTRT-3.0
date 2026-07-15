#!/usr/bin/env python3

import csv
import math

INPUT="results/csv/ftrt_silso.csv"

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

PERIODOS=[
    ("2020","2021"),
    ("2022","2023"),
    ("2024","2026"),
]

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

rows=[]

with open(INPUT,newline="") as f:
    rows=list(csv.DictReader(f))

print("="*72)
print("EXP003 TEMPORAL VALIDATION")
print("="*72)

for inicio,fin in PERIODOS:

    datos=[
        r for r in rows
        if inicio <= r["fecha"][:4] <= fin
    ]

    print()
    print(f"Periodo {inicio}-{fin}")
    print("-"*72)

    for var in VARIABLES:

        mejor_r=0.0
        mejor_lag=0

        for lag in range(-90,91):

            xs=[]
            ys=[]

            for i in range(len(datos)):
                j=i+lag
                if j<0 or j>=len(datos):
                    continue

                xs.append(float(datos[i][var]))
                ys.append(float(datos[j]["ssn"]))

            r=pearson(xs,ys)

            if abs(r)>abs(mejor_r):
                mejor_r=r
                mejor_lag=lag

        print(f"{var:24s} lag={mejor_lag:4d} r={mejor_r: .5f}")

print()
print("="*72)
print("EXP003 FINALIZADO")
print("="*72)
