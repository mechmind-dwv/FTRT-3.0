#!/usr/bin/env python3

import csv
import os
from statistics import mean

INPUT="data/catalog/master_catalog.csv"
OUTDIR="experiments/EXP056_walk_forward/results"
OUTFILE=os.path.join(OUTDIR,"walk_forward.csv")

os.makedirs(OUTDIR,exist_ok=True)

rows=[]

with open(INPUT,newline="") as f:
    for r in csv.DictReader(f):

        if not r["ftrt"]:
            continue

        try:
            ftrt=float(r["ftrt"])
        except:
            continue

        rows.append({
            "fecha":r["fecha"],
            "clase":r["clase"],
            "ftrt":ftrt
        })

rows.sort(key=lambda x:x["fecha"])

print("="*72)
print("EXP056 WALK FORWARD")
print("="*72)

if len(rows)<6:
    print("Eventos insuficientes.")
    raise SystemExit

with open(OUTFILE,"w",newline="") as f:

    w=csv.writer(f)
    w.writerow(["fecha","observado","prediccion"])

    errores=[]

    for i in range(3,len(rows)):

        train=[x["ftrt"] for x in rows[:i]]

        pred=mean(train)

        obs=rows[i]["ftrt"]

        errores.append(abs(obs-pred))

        w.writerow([
            rows[i]["fecha"],
            round(obs,6),
            round(pred,6)
        ])

print("Eventos usados :",len(rows))
print("Predicciones   :",len(errores))
print("MAE            :",round(mean(errores),6))
print("Archivo        :",OUTFILE)
print("="*72)
