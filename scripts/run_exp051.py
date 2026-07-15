import csv
import numpy as np

INPUT="data/catalog/solar_event_catalog.csv"

rows=list(csv.DictReader(open(INPUT)))

groups={
    "M5+":[],
    "M8+":[],
    "X1+":[],
    "X2+":[],
    "X5+":[]
}

def parse_goes(clase):

    if not clase:
        return None

    letra=clase[0].upper()

    try:
        valor=float(clase[1:])
    except:
        return None

    return letra,valor

for r in rows:

    p=parse_goes(r["clase"])

    if p is None:
        continue

    letra,valor=p

    try:
        ftrt=float(r["ftrt"])
    except:
        continue

    try:
        f7=float(r["ftrt_7d"])
    except:
        f7=np.nan

    try:
        f14=float(r["ftrt_14d"])
    except:
        f14=np.nan

    d={
        "ftrt":ftrt,
        "f7":f7,
        "f14":f14
    }

    if letra=="M":
        if valor>=5:
            groups["M5+"].append(d)
        if valor>=8:
            groups["M8+"].append(d)

    if letra=="X":
        if valor>=1:
            groups["X1+"].append(d)
        if valor>=2:
            groups["X2+"].append(d)
        if valor>=5:
            groups["X5+"].append(d)

print("="*72)
print("EXP051 GOES CLASS VALIDATION")
print("="*72)

for name,data in groups.items():

    print("-"*72)
    print(name)

    if len(data)==0:
        print("Sin eventos")
        continue

    f=np.array([x["ftrt"] for x in data])

    f7=np.array([x["f7"] for x in data],dtype=float)

    f14=np.array([x["f14"] for x in data],dtype=float)

    print("N          :",len(f))
    print("FTRT medio :",round(np.nanmean(f),5))
    print("FTRT max   :",round(np.nanmax(f),5))
    print("FTRT 7d    :",round(np.nanmean(f7),5))
    print("FTRT 14d   :",round(np.nanmean(f14),5))

print("="*72)
