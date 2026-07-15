#!/usr/bin/env python3

import csv
import math

INPUT="results/csv/ftrt_silso.csv"
OUTPUT="experiments/EXP005_prediction_validation/results/predictions.csv"

rows=[]

with open(INPUT,newline="",encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for r in reader:
        try:
            r["ssn"]=float(r["ssn"])
            r["entropia_fase"]=float(r["entropia_fase"])
            rows.append(r)
        except:
            pass

train=[]
test=[]

for r in rows:
    if r["fecha"]<"2025-01-01":
        train.append(r)
    else:
        test.append(r)

media=sum(x["ssn"] for x in train)/len(train)

with open(OUTPUT,"w",newline="",encoding="utf-8") as f:
    writer=csv.writer(f)
    writer.writerow(["fecha","observado","predicho"])

    mae=0.0
    mse=0.0

    for r in test:
        pred=media
        obs=r["ssn"]

        writer.writerow([r["fecha"],obs,pred])

        err=abs(obs-pred)
        mae+=err
        mse+=(obs-pred)**2

mae/=len(test)
rmse=math.sqrt(mse/len(test))

print("="*72)
print("EXP005 PREDICTION VALIDATION")
print("="*72)
print("Entrenamiento :",len(train))
print("Test          :",len(test))
print("MAE           :",round(mae,3))
print("RMSE          :",round(rmse,3))
print()
print("Resultado:",OUTPUT)
print("="*72)
