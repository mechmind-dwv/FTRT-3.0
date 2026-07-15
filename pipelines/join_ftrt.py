#!/usr/bin/env python3

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DONKI = ROOT/"data/catalog/donki_catalog.csv"
FTRT  = ROOT/"results/csv/ftrt_index_v2.csv"
OUT   = ROOT/"data/catalog/master_catalog.csv"

# -------------------------------------------------------
# Cargar FTRT
# -------------------------------------------------------

ftrt={}

with open(FTRT) as f:

    for r in csv.DictReader(f):

        ftrt[r["fecha"]] = r

# -------------------------------------------------------
# Unir
# -------------------------------------------------------

rows=[]

with open(DONKI) as f:

    for r in csv.DictReader(f):

        d=r["fecha"]

        idx=ftrt.get(d,{})

        r["ftrt"]=idx.get("ftrt_index_v2","")
        r["ssn"]=idx.get("ssn","")

        rows.append(r)

# -------------------------------------------------------
# Guardar
# -------------------------------------------------------

with open(OUT,"w",newline="") as f:

    w=csv.DictWriter(f,fieldnames=rows[0].keys())

    w.writeheader()

    w.writerows(rows)

print("="*72)
print("MASTER CATALOG")
print("="*72)
print("Eventos :",len(rows))
print("Archivo :",OUT)
print("="*72)
