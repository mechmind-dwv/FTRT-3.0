import csv
import numpy as np

FTRT_FILE="results/csv/ftrt_index_v2.csv"
EVENT_FILE="data/solar_events/x_flares.csv"

rows=list(csv.DictReader(open(FTRT_FILE)))
events=set(r["fecha"] for r in csv.DictReader(open(EVENT_FILE)))

dates=[r["fecha"] for r in rows]
ftrt=np.array([float(r["ftrt_index_v2"]) for r in rows])

windows=[1,3,7,14,30]
rng=np.random.default_rng(42)

print("="*72)
print("EXP049 PRECURSOR PERMUTATION TEST")
print("="*72)

for w in windows:

    idx=[]
    vals=[]

    for i,d in enumerate(dates):
        if d in events and i>=w:
            idx.append(i)
            vals.append(np.mean(ftrt[i-w:i]))

    if len(vals)==0:
        continue

    vals=np.array(vals)

    mask=np.ones(len(ftrt),dtype=bool)
    mask[idx]=False
    background=ftrt[mask]

    real=np.mean(vals)-np.mean(background)

    deltas=[]

    for _ in range(10000):
        sample=rng.choice(background,size=len(vals),replace=False)
        deltas.append(np.mean(sample)-np.mean(background))

    deltas=np.array(deltas)

    print("-"*72)
    print(f"Ventana {w} días")
    print("Eventos     :",len(vals))
    print("Delta real  :",round(real,5))
    print("Null mean   :",round(np.mean(deltas),5))
    print("IC95 null   :",
          round(np.percentile(deltas,2.5),5),
          "-",
          round(np.percentile(deltas,97.5),5))
    print("p-value     :",round(np.mean(deltas>=real),5))

print("="*72)
