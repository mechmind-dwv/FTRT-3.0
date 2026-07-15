import csv
import numpy as np
from scipy.stats import pearsonr

INPUT="results/csv/ftrt_index_v2.csv"

idx=[]
ssn=[]

with open(INPUT,newline="") as f:
    r=csv.DictReader(f)
    for row in r:
        idx.append(float(row["ftrt_index_v2"]))
        ssn.append(float(row["ssn"]))

idx=np.array(idx)
ssn=np.array(ssn)

print("="*72)
print("EXP010 FTRT REGIMES")
print("="*72)

q1,q2=np.percentile(idx,[33,66])

print("Q1:",q1)
print("Q2:",q2)

regimes=[
    ("LOW",idx<q1),
    ("MEDIUM",(idx>=q1)&(idx<q2)),
    ("HIGH",idx>=q2)
]

for name,mask in regimes:

    print()
    print(name)
    print("-"*40)

    print("N:",mask.sum())
    print("FTRT mean:",round(idx[mask].mean(),5))
    print("SSN mean:",round(ssn[mask].mean(),5))

    if mask.sum()>10:
        print("Pearson:",
              round(pearsonr(idx[mask],ssn[mask])[0],5))

print()
print("="*72)
print("EXP010 FINALIZADO")
print("="*72)
