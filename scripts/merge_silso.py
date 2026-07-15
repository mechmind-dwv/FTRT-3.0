"""
Une el dataset FTRT con SILSO por fecha.
"""

import csv

FTRT = "results/csv/ftrt_geometry_2020_2026.csv"
SILSO = "data/silso/silso_daily.csv"
OUT = "results/csv/ftrt_silso.csv"

# ---------- leer FTRT ----------

ftrt = {}

with open(FTRT, newline="") as f:

    for row in csv.DictReader(f):

        ftrt[row["fecha"]] = row

# ---------- unir ----------

n = 0

with open(SILSO, newline="") as fin, \
     open(OUT, "w", newline="") as fout:

    reader = csv.DictReader(fin)

    campos = None

    writer = None

    for row in reader:

        fecha = row["fecha"]

        if fecha not in ftrt:
            continue

        merged = dict(ftrt[fecha])

        merged["ssn"] = row["ssn"]

        if writer is None:

            campos = list(merged.keys())

            writer = csv.DictWriter(
                fout,
                fieldnames=campos
            )

            writer.writeheader()

        writer.writerow(merged)

        n += 1

print("=" * 72)
print("MERGE COMPLETADO")
print("=" * 72)
print("Registros:", n)
print("Salida:", OUT)
