import csv
import numpy as np

FTRT_FILE = "results/csv/ftrt_index_v2.csv"
EVENT_FILE = "data/solar_events/x_flares.csv"

rows = list(csv.DictReader(open(FTRT_FILE)))
events = list(csv.DictReader(open(EVENT_FILE)))

ftrt = {r["fecha"]: float(r["ftrt_index_v2"]) for r in rows}

vals = []

for e in events:
    d = e["fecha"]
    if d in ftrt:
        vals.append(ftrt[d])

vals = np.array(vals)

print("="*72)
print("EXP046 X FLARE VALIDATION")
print("="*72)
print("Eventos encontrados:", len(vals))

if len(vals):
    print("Media FTRT:", round(np.mean(vals),5))
    print("Mediana   :", round(np.median(vals),5))
    print("Máximo    :", round(np.max(vals),5))
    print("Mínimo    :", round(np.min(vals),5))
else:
    print("No se encontraron eventos coincidentes.")
print("="*72)
