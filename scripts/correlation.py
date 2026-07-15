"""
Correlación FTRT vs SSN
"""

import csv
import numpy as np

archivo = "results/csv/ftrt_silso.csv"

energia = []
ssn = []

with open(archivo, newline="") as f:

    for row in csv.DictReader(f):

        energia.append(
            float(row["energia_resonancia"])
        )

        ssn.append(
            float(row["ssn"])
        )

energia = np.array(energia)
ssn = np.array(ssn)

r = np.corrcoef(
    energia,
    ssn
)[0,1]

print("=" * 72)
print("CORRELACIÓN")
print("=" * 72)
print("Pearson =", r)
