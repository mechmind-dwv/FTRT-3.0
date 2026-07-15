import csv
import numpy as np

FTRT_FILE="results/csv/ftrt_index_v2.csv"
EVENT_FILE="data/solar_events/x_flares.csv"

rows=list(csv.DictReader(open(FTRT_FILE)))
events=list(csv.DictReader(open(EVENT_FILE)))

event_dates=set(r["fecha"] for r in events)

event_vals=[]
background=[]

for r in rows:
    v=float(r["ftrt_index_v2"])
    if r["fecha"] in event_dates:
        event_vals.append(v)
    else:
        background.append(v)

event_vals=np.array(event_vals)
background=np.array(background)

real_delta=np.mean(event_vals)-np.mean(background)

rng=np.random.default_rng(42)

allvals=np.concatenate([event_vals,background])

deltas=[]

for _ in range(10000):
    rng.shuffle(allvals)
    a=allvals[:len(event_vals)]
    b=allvals[len(event_vals):]
    deltas.append(np.mean(a)-np.mean(b))

deltas=np.array(deltas)

print("="*72)
print("EXP047 X FLARE PERMUTATION")
print("="*72)
print("Eventos:",len(event_vals))
print("Background:",len(background))
print()
print("Media eventos :",round(np.mean(event_vals),5))
print("Media fondo   :",round(np.mean(background),5))
print("Delta real    :",round(real_delta,5))
print()
print("Media null    :",round(np.mean(deltas),5))
print("IC95 null     :",
      round(np.percentile(deltas,2.5),5),
      "-",
      round(np.percentile(deltas,97.5),5))
print("p-value       :",round(np.mean(deltas>=real_delta),5))
print("="*72)
