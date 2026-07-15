#!/usr/bin/env python3

import csv
import math

INPUT="results/csv/ftrt_index_v2.csv"

x=[]
y=[]

with open(INPUT,newline="",encoding="utf-8") as f:
    for r in csv.DictReader(f):
        x.append(float(r["ftrt_index_v2"]))
        y.append(float(r["ssn"]))

mx=sum(x)/len(x)
my=sum(y)/len(y)

num=sum((a-mx)*(b-my) for a,b in zip(x,y))
denx=sum((a-mx)**2 for a in x)
deny=sum((b-my)**2 for b in y)

r=num/math.sqrt(denx*deny)

print("="*72)
print("EXP007 v2 FTRT WEIGHTED INDEX")
print("="*72)
print("Registros :",len(x))
print("Pearson r :",round(r,5))
print("="*72)
