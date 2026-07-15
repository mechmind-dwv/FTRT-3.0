#!/usr/bin/env python3

import csv
import os

INDEX="results/csv/ftrt_index_v2.csv"
PROB="experiments/EXP057_probabilistic/results/probability_table.csv"
OUT="experiments/EXP058_operational_prediction/results/daily_prediction.csv"

# Leer tabla de probabilidades
ptable={}
with open(PROB,newline="") as f:
    for r in csv.DictReader(f):
        ptable[int(r["threshold"])]=float(r["probability"])

os.makedirs(os.path.dirname(OUT),exist_ok=True)

def probability(value):
    keys=sorted(ptable.keys())
    p=0.0
    for k in keys:
        if value>=k:
            p=ptable[k]
    return p

with open(INDEX,newline="") as fin,\
     open(OUT,"w",newline="") as fout:

    reader=csv.DictReader(fin)
    writer=csv.writer(fout)

    writer.writerow([
        "fecha",
        "ftrt",
        "ssn",
        "probabilidad",
        "riesgo"
    ])

    total=0

    for r in reader:

        try:
            f=float(r["ftrt_index_v2"])
        except:
            continue

        p=probability(f)

        if p<0.20:
            riesgo="BAJO"
        elif p<0.40:
            riesgo="MODERADO"
        elif p<0.60:
            riesgo="ALTO"
        else:
            riesgo="EXTREMO"

        writer.writerow([
            r["fecha"],
            round(f,6),
            r["ssn"],
            round(p,3),
            riesgo
        ])

        total+=1

print("="*72)
print("EXP058 OPERATIONAL PREDICTION")
print("="*72)
print("Predicciones :",total)
print("Archivo      :",OUT)
print("="*72)
