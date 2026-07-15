#!/usr/bin/env python3

import csv
import random
import numpy as np

INPUT = "data/catalog/master_catalog.csv"
NBOOT = 10000

rows = list(csv.DictReader(open(INPUT, encoding="utf-8")))

con = []
sin = []

for r in rows:
    try:
        f = float(r["ftrt"])
    except:
        continue

    cme = int(r.get("cme_asociada") or 0)

    if cme > 0:
        con.append(f)
    else:
        sin.append(f)

print("="*72)
print("EXP053 BOOTSTRAP")
print("="*72)

print("Con CME :", len(con))
print("Sin CME :", len(sin))

if len(con) < 2 or len(sin) < 2:
    print("\nMuestra insuficiente.")
    raise SystemExit

diff = []

for _ in range(NBOOT):

    a = random.choices(con, k=len(con))
    b = random.choices(sin, k=len(sin))

    diff.append(np.mean(a) - np.mean(b))

diff = np.array(diff)

print()
print("Diferencia observada :", round(np.mean(con)-np.mean(sin),6))
print("Bootstrap media      :", round(diff.mean(),6))
print("Bootstrap STD        :", round(diff.std(),6))
print("IC95 inferior        :", round(np.percentile(diff,2.5),6))
print("IC95 superior        :", round(np.percentile(diff,97.5),6))

print("="*72)
