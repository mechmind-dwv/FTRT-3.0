#!/usr/bin/env python3

import csv
import os
from datetime import datetime, timedelta

CATALOG = "data/catalog/master_catalog.csv"
FTRT_FILE = "results/csv/ftrt_index_v2.csv"

OUT = "experiments/EXP061_join_expansion/results/join_expansion.csv"

FMT = "%Y-%m-%d"


# -------------------------
# Cargar FTRT
# -------------------------

ftrt = {}

with open(FTRT_FILE, newline="", encoding="utf-8") as f:

    reader = csv.DictReader(f)

    print("Columnas FTRT:", reader.fieldnames)

    for r in reader:

        fecha = None

        for key in ["date","fecha","day"]:
            if key in r and r[key]:
                fecha = r[key]
                break

        if fecha is None:
            continue

        try:
            fecha = datetime.strptime(fecha[:10], FMT)
            valor = float(r.get("ftrt", r.get("ftrt_index_v2")))
            ftrt[fecha] = valor

        except:
            continue


# -------------------------
# Join expandido
# -------------------------

rows=[]

contador={
    "exact":0,
    "±1":0,
    "±2":0,
    "±3":0,
    "none":0
}


with open(CATALOG,newline="",encoding="utf-8") as f:

    reader=csv.DictReader(f)

    for r in reader:

        fecha=datetime.strptime(r["fecha"],FMT)

        encontrado=False


        for ventana in range(0,4):

            candidatos=[fecha]

            if ventana>0:
                candidatos=[
                    fecha+timedelta(days=ventana),
                    fecha-timedelta(days=ventana)
                ]


            for d in candidatos:

                if d in ftrt:

                    r["ftrt_join"]=ftrt[d]
                    r["lag_days"]=(d-fecha).days

                    if ventana==0:
                        metodo="exact"
                    else:
                        metodo=f"±{ventana}"

                    r["join_method"]=metodo

                    contador[metodo]+=1

                    encontrado=True
                    break


            if encontrado:
                break


        if not encontrado:

            r["ftrt_join"]=""
            r["lag_days"]=""
            r["join_method"]="none"

            contador["none"]+=1


        rows.append(r)



os.makedirs(
    os.path.dirname(OUT),
    exist_ok=True
)


with open(OUT,"w",newline="",encoding="utf-8") as f:

    writer=csv.DictWriter(
        f,
        fieldnames=rows[0].keys()
    )

    writer.writeheader()
    writer.writerows(rows)



total=len(rows)

con_ftrt=total-contador["none"]


print("="*72)
print("EXP061 JOIN EXPANSION")
print("="*72)

print("Eventos :",total)

for k,v in contador.items():
    print(f"{k:8}: {v}")

print("-"*72)

print("Con FTRT :",con_ftrt)
print(
    "Cobertura:",
    round(con_ftrt*100/total,2),
    "%"
)

print("="*72)
print("Archivo:",OUT)
print("="*72)

