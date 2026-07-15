#!/usr/bin/env python3

import csv
import math

INPUT="results/csv/ftrt_silso.csv"
OUTPUT="results/csv/ftrt_index_v2.csv"

# Pesos según signo de correlación EXP001
WEIGHTS = {
    "entropia_fase": 1,
    "estados_fase": 1,
    "entropia_espectral": 1,
    "concentracion_fase": -1,
    "energia_resonancia": -1,
    "lambda_max": -1,
    "coherencia_espectral": -1
}

rows=[]

with open(INPUT,newline="",encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for r in reader:
        rows.append(r)

stats={}

for v in WEIGHTS:
    vals=[float(r[v]) for r in rows]
    m=sum(vals)/len(vals)
    s=math.sqrt(sum((x-m)**2 for x in vals)/len(vals))
    stats[v]=(m,s)

with open(OUTPUT,"w",newline="",encoding="utf-8") as f:

    writer=csv.writer(f)
    writer.writerow(["fecha","ftrt_index_v2","ssn"])

    for r in rows:

        score=0

        for v,w in WEIGHTS.items():
            m,s=stats[v]
            z=(float(r[v])-m)/s if s else 0
            score += w*z

        writer.writerow([
            r["fecha"],
            round(score,6),
            r["ssn"]
        ])

print("="*72)
print("FTRT INDEX v2 GENERADO")
print("="*72)
print("Variables:",len(WEIGHTS))
print("Registros:",len(rows))
print("Salida:",OUTPUT)
print("="*72)
