#!/usr/bin/env python3

import csv
import os

INPUT="data/catalog/master_catalog.csv"
OUTDIR="experiments/EXP057_probabilistic/results"
OUTFILE=os.path.join(OUTDIR,"probability_table.csv")

os.makedirs(OUTDIR,exist_ok=True)

rows=[]

with open(INPUT,newline="") as f:
    for r in csv.DictReader(f):

        if not r["ftrt"]:
            continue

        try:
            f=float(r["ftrt"])
        except:
            continue

        clase=r["clase"]

        severe=0
        if clase.startswith("X"):
            severe=1
        elif clase.startswith("M"):
            try:
                if float(clase[1:])>=5:
                    severe=1
            except:
                pass

        rows.append((f,severe))

rows.sort()

print("="*72)
print("EXP057 PROBABILISTIC MODEL")
print("="*72)

with open(OUTFILE,"w",newline="") as f:

    w=csv.writer(f)
    w.writerow(["threshold","events","severe","probability"])

    for t in range(-5,13):

        subset=[x for x in rows if x[0]>=t]

        if len(subset)==0:
            continue

        sev=sum(x[1] for x in subset)

        p=sev/len(subset)

        w.writerow([t,len(subset),sev,round(p,4)])

        print(
            f"FTRT>={t:2d}   "
            f"N={len(subset):2d}   "
            f"Severos={sev:2d}   "
            f"P={p:.3f}"
        )

print("="*72)
print("Archivo:",OUTFILE)
print("="*72)
