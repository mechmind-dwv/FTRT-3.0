#!/usr/bin/env python3

import csv

INFILE = "data/silso/SN_d_tot_V2.0.csv"
OUTFILE = "data/silso/silso_daily.csv"

n = 0

with open(INFILE, encoding="utf-8") as fin, \
     open(OUTFILE, "w", newline="", encoding="utf-8") as fout:

    writer = csv.writer(fout)
    writer.writerow(["fecha","ssn"])

    for line in fin:

        if line.startswith("#"):
            continue

        cols = line.split(";")

        if len(cols) < 5:
            continue

        try:
            year = int(cols[0])
            month = int(cols[1])
            day = int(cols[2])
            ssn = float(cols[4])
        except ValueError:
            continue

        fecha = f"{year:04d}-{month:02d}-{day:02d}"

        writer.writerow([fecha, ssn])
        n += 1

print("="*72)
print("SILSO IMPORTADO")
print("="*72)
print("Registros:", n)
print("Salida:", OUTFILE)
