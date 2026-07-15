#!/usr/bin/env python3

import csv
import os

INPUT="data/catalog/master_catalog.csv"
OUTDIR="experiments/EXP055_roc_pr/results"
OUTFILE=os.path.join(OUTDIR,"roc_thresholds.csv")

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

        clase=r["clase"] or ""

        positiva=0
        if clase.startswith("X"):
            positiva=1
        elif clase.startswith("M"):
            try:
                positiva=int(float(clase[1:])>=5)
            except:
                positiva=0

        rows.append((ftrt,positiva))

print("="*72)
print("EXP055 ROC PREPARATION")
print("="*72)

print("Eventos válidos :",len(rows))

if len(rows)<10:
    print("Muestra insuficiente para ROC robusta.")
    print("Se genera únicamente la tabla de umbrales.")

thresholds=[0,1,2,3,4,5,6,7,8]

with open(OUTFILE,"w",newline="") as f:

    w=csv.writer(f)
    w.writerow(["threshold","TP","FP","TN","FN"])

    for t in thresholds:

        tp=fp=tn=fn=0

        for value,label in rows:

            pred=value>=t

            if pred and label:
                tp+=1
            elif pred and not label:
                fp+=1
            elif (not pred) and label:
                fn+=1
            else:
                tn+=1

        w.writerow([t,tp,fp,tn,fn])

print("Archivo:",OUTFILE)
print("="*72)
