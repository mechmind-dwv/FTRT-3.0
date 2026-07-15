import csv
import os
from datetime import datetime

FTRT_FILE="results/csv/ftrt_index_v2.csv"
EVENT_FILE="data/solar_events/x_flares.csv"
OUT_FILE="data/catalog/solar_event_catalog.csv"

# ------------------------
# Leer serie FTRT
# ------------------------

series={}

with open(FTRT_FILE,newline="") as f:
    for r in csv.DictReader(f):
        d=r["fecha"][:10]
        series[d]=r

# ------------------------
# Función media ventana
# ------------------------

def mean_window(fecha,days):

    fechas=sorted(series.keys())

    if fecha not in fechas:
        return ""

    i=fechas.index(fecha)

    if i<days:
        return ""

    vals=[]

    for j in range(i-days,i):
        try:
            vals.append(float(series[fechas[j]]["ftrt_index_v2"]))
        except:
            pass

    if len(vals)==0:
        return ""

    return round(sum(vals)/len(vals),5)

# ------------------------
# Construir catálogo
# ------------------------

os.makedirs("data/catalog",exist_ok=True)

out=[]

with open(EVENT_FILE,newline="") as f:

    for e in csv.DictReader(f):

        fecha=e["fecha"][:10]

        if fecha not in series:
            continue

        s=series[fecha]

        row={

            "fecha":fecha,

            "hora":e.get("time",""),

            "clase":e.get("class",""),

            "magnitud":e.get("class",""),

            "latitud":e.get("latitude",""),

            "longitud":e.get("longitude",""),

            "region_activa":e.get("region",""),

            "velocidad_cme":e.get("cme_speed",""),

            "kp":e.get("kp",""),

            "dst":e.get("dst",""),

            "ftrt":s["ftrt_index_v2"],

            "ftrt_3d":mean_window(fecha,3),

            "ftrt_7d":mean_window(fecha,7),

            "ftrt_14d":mean_window(fecha,14),

            "ftrt_30d":mean_window(fecha,30)

        }

        out.append(row)

# ------------------------
# Guardar
# ------------------------

with open(OUT_FILE,"w",newline="") as f:

    w=csv.DictWriter(
        f,
        fieldnames=list(out[0].keys())
    )

    w.writeheader()

    w.writerows(out)

print("="*72)
print("EXP050 MASTER CATALOG")
print("="*72)
print("Eventos :",len(out))
print("Archivo :",OUT_FILE)
print("="*72)

