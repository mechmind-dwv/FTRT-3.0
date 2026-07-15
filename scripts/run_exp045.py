# scripts/run_exp045.py

import csv
import numpy as np

INPUT = "results/csv/ftrt_index_v2.csv"

rows = list(csv.DictReader(open(INPUT)))

# Sustituye estas fechas por el catálogo NOAA/NASA de llamaradas X
EVENTS = {
    "2021-07-03",
    "2022-10-02",
    "2023-02-17",
    "2024-05-10",
}

ftrt = np.array([float(r["ftrt_index_v2"]) for r in rows])
dates = [r["fecha"] for r in rows]

event_idx = [i for i, d in enumerate(dates) if d in EVENTS]

windows = []

for i in event_idx:
    if i >= 30:
        windows.append(np.mean(ftrt[i-30:i]))

background = []

for i in range(30, len(ftrt)):
    if i not in event_idx:
        background.append(np.mean(ftrt[i-30:i]))

windows = np.array(windows)
background = np.array(background)

print("=" * 72)
print("EXP045 PRE-EVENT FTRT")
print("=" * 72)
print("Eventos:", len(windows))
print("Media previa:", round(np.mean(windows), 5))
print("Fondo:", round(np.mean(background), 5))
print("Delta:", round(np.mean(windows) - np.mean(background), 5))
print("=" * 72)
