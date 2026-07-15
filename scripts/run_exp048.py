import csv
import numpy as np

FTRT="results/csv/ftrt_index_v2.csv"
EVENTS="data/solar_events/x_flares.csv"

rows=list(csv.DictReader(open(FTRT)))
events=set(r["fecha"] for r in csv.DictReader(open(EVENTS)))

dates=[r["fecha"] for r in rows]
values=np.array([float(r["ftrt_index_v2"]) for r in rows])

windows=[1,3,7,14,30]

print("="*72)
print("EXP048 PRECURSOR WINDOWS")
print("="*72)

for w in windows:

    vals=[]

    for i,d in enumerate(dates):
        if d in events and i>=w:
            vals.append(np.mean(values[i-w:i]))

    if len(vals)==0:
        continue

    vals=np.array(vals)

    print(
        f"{w:2d} días | "
        f"N={len(vals):3d} | "
        f"Media={vals.mean():.5f} | "
        f"STD={vals.std():.5f}"
    )

print("="*72)
