#!/usr/bin/env python3

import json
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

INFILE = ROOT/"data/noaa/donki_flares.json"
OUTFILE = ROOT/"data/catalog/donki_catalog.csv"

with open(INFILE) as f:
    events=json.load(f)

rows=[]

for e in events:

    rows.append({

        "fecha":e["beginTime"][:10],
        "hora":e["beginTime"][11:16],
        "clase":e.get("classType",""),
        "latitud_longitud":e.get("sourceLocation",""),
        "region_activa":e.get("activeRegionNum",""),
        "cme_asociada":len(e.get("linkedEvents") or []),
        "id":e.get("flrID","")

    })

with open(OUTFILE,"w",newline="") as f:

    w=csv.DictWriter(f,fieldnames=rows[0].keys())

    w.writeheader()

    w.writerows(rows)

print("="*72)
print("DONKI CATALOG")
print("="*72)
print("Eventos:",len(rows))
print("Archivo:",OUTFILE)
print("="*72)
