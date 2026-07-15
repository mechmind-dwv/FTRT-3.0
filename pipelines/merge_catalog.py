#!/usr/bin/env python3

from pathlib import Path
import json
import csv

ROOT = Path(__file__).resolve().parents[1]

GOES = ROOT/"data/goes/goes_xray_events.json"
CATALOG = ROOT/"data/catalog/solar_event_catalog.csv"

rows=[]

if GOES.exists() and GOES.stat().st_size>0:

    print("Leyendo GOES...")

    try:

        with open(GOES,"r") as f:
            events=json.load(f)

        print("Eventos GOES:",len(events))

        for e in events:

            rows.append({
                "fecha":e.get("max_time","")[:10],
                "hora":e.get("max_time","")[11:19],
                "clase":e.get("max_class",""),
                "magnitud":"",
                "latitud":"",
                "longitud":"",
                "region_activa":e.get("region",""),
                "velocidad_cme":"",
                "kp":"",
                "dst":"",
                "ftrt":"",
                "ftrt_3d":"",
                "ftrt_7d":"",
                "ftrt_14d":"",
                "ftrt_30d":""
            })

    except Exception as ex:
        print("GOES inválido:",ex)

else:

    print("GOES vacío o inexistente. Se conserva el catálogo actual.")

if rows:

    with open(CATALOG,"w",newline="") as f:

        w=csv.DictWriter(f,fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)

print("="*72)
print("MERGE FINALIZADO")
print("Filas nuevas:",len(rows))
print("="*72)
