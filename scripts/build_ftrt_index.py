#!/usr/bin/env python3

import csv
import math

INPUT="results/csv/ftrt_silso.csv"
OUTPUT="results/csv/ftrt_index.csv"

VARS=[
"lambda_max",
"energia_resonancia",
"coherencia_espectral",
"entropia_espectral",
"estados_fase",
"entropia_fase",
"concentracion_fase"
]

rows=[]

with open(INPUT,newline="",encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for r in reader:
        rows.append(r)

stats={}

for v in VARS:
    vals=[float(r[v]) for r in rows]
    m=sum(vals)/len(vals)
    s=math.sqrt(sum((x-m)**2 for x in vals)/len(vals))
    stats[v]=(m,s)

with open(OUTPUT,"w",newline="",encoding="utf-8") as f:

    writer=csv.writer(f)
    writer.writerow(["fecha","ftrt_index","ssn"])

    for r in rows:

        score=0.0

        for v in VARS:
            m,s=stats[v]
            z=(float(r[v])-m)/s if s>0 else 0.0
            score+=z

        writer.writerow([r["fecha"],round(score,6),r["ssn"]])

print("="*72)
print("FTRT INDEX GENERADO")
print("="*72)
print("Variables:",len(VARS))
print("Registros:",len(rows))
print("Salida:",OUTPUT)
print("="*72)
