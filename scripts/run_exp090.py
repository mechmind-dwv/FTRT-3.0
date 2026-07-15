#!/usr/bin/env python3
# EXP090 - FTRT SSN Cross Lag Correlation Analysis

from datetime import datetime, UTC
import csv
import math
import os

INPUT = "results/csv/ftrt_index_v2.csv"
OUTPUT = "experiments/EXP090_cross_lag/results/cross_lag.csv"

dates = []
ftrt = []
ssn = []

with open(INPUT, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        dates.append(row["fecha"])
        ftrt.append(float(row["ftrt_index_v2"]))
        ssn.append(float(row["ssn"]))

def pearson(x, y):
    n = len(x)
    if n < 3:
        return 0.0

    mx = sum(x) / n
    my = sum(y) / n

    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    denx = math.sqrt(sum((a - mx) ** 2 for a in x))
    deny = math.sqrt(sum((b - my) ** 2 for b in y))

    if denx == 0 or deny == 0:
        return 0.0

    return num / (denx * deny)

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)

with open(OUTPUT, "w", newline="", encoding="utf-8") as out:

    writer = csv.writer(out)
    writer.writerow([
        "timestamp",
        "lag_days",
        "pearson",
        "samples"
    ])

    print("=" * 72)
    print("EXP090 FTRT SSN CROSS LAG")
    print("=" * 72)

    best_lag = None
    best_r = -999

    for lag in range(-30, 31):

        xs = []
        ys = []

        for i in range(len(ftrt)):

            j = i + lag

            if 0 <= j < len(ftrt):
                xs.append(ftrt[i])
                ys.append(ssn[j])

        r = pearson(xs, ys)

        writer.writerow([
            datetime.now(UTC).isoformat(),
            lag,
            round(r, 6),
            len(xs)
        ])

        print(f"Lag {lag:>3}: Pearson={r: .4f} n={len(xs)}")

        if abs(r) > abs(best_r):
            best_r = r
            best_lag = lag

print("-" * 72)
print(f"MEJOR LAG: {best_lag}")
print(f"PEARSON : {best_r:.4f}")
print(f"Archivo: {OUTPUT}")
print("=" * 72)
