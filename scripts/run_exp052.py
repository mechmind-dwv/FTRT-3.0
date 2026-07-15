#!/usr/bin/env python3

import csv
import numpy as np

INPUT = "data/catalog/master_catalog.csv"

rows = list(csv.DictReader(open(INPUT, encoding="utf-8")))

con = []
sin = []

for r in rows:

    try:
        ftrt = float(r["ftrt"])
    except:
        continue

    try:
        cme = int(r["cme_asociada"])
    except:
        cme = 0

    if cme > 0:
        con.append(ftrt)
    else:
        sin.append(ftrt)

print("="*72)
print("EXP052 CME ASSOCIATION")
print("="*72)

print()

print("Eventos con CME :", len(con))

if len(con):
    print("FTRT medio :", round(np.mean(con),6))
    print("STD        :", round(np.std(con),6))
    print("Máximo     :", round(np.max(con),6))

print()

print("Eventos sin CME :", len(sin))

if len(sin):
    print("FTRT medio :", round(np.mean(sin),6))
    print("STD        :", round(np.std(sin),6))
    print("Máximo     :", round(np.max(sin),6))

print()

if len(con) and len(sin):

    print("Δ medias :", round(np.mean(con)-np.mean(sin),6))

print("="*72)
