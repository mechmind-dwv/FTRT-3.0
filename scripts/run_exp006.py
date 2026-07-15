#!/usr/bin/env python3

import csv
import math

INPUT="results/csv/ftrt_silso.csv"
LAG=44

rows=[]

with open(INPUT,newline="",encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for r in reader:
        try:
            rows.append({
                "fecha":r["fecha"],
                "x":float(r["entropia_fase"]),
                "y":float(r["ssn"])
            })
        except:
            pass

pred=[]
obs=[]

for i in range(LAG,len(rows)):
    pred.append(rows[i-LAG]["x"])
    obs.append(rows[i]["y"])

mx=sum(pred)/len(pred)
my=sum(obs)/len(obs)

num=sum((x-mx)*(y-my) for x,y in zip(pred,obs))
denx=sum((x-mx)**2 for x in pred)
deny=sum((y-my)**2 for y in obs)

r=num/math.sqrt(denx*deny)

a=my-r*mx

mae=0
mse=0

for x,y in zip(pred,obs):
    yp=a+r*x
    mae+=abs(yp-y)
    mse+=(yp-y)**2

mae/=len(obs)
rmse=math.sqrt(mse/len(obs))

print("="*72)
print("EXP006 LAG PREDICTION")
print("="*72)
print("Lag :",LAG,"días")
print("r   :",round(r,5))
print("MAE :",round(mae,3))
print("RMSE:",round(rmse,3))
print("="*72)
