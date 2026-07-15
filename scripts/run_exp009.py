import csv
import numpy as np
from scipy.stats import pearsonr

INPUT="results/csv/ftrt_index_v2.csv"

dates=[]
idx=[]
ssn=[]

with open(INPUT,newline="") as f:
    r=csv.DictReader(f)
    for row in r:
        dates.append(row["fecha"])
        idx.append(float(row["ftrt_index_v2"]))
        ssn.append(float(row["ssn"]))

idx=np.array(idx)
ssn=np.array(ssn)

print("="*72)
print("EXP009 WALK FORWARD WINDOWS")
print("="*72)

for window in [180,365]:

    print()
    print("WINDOW:",window,"days")
    print("-"*40)

    values=[]

    for i in range(window,len(idx)):
        r=pearsonr(
            idx[i-window:i],
            ssn[i-window:i]
        )[0]

        values.append(r)

    values=np.array(values)

    print("Mean r :",round(values.mean(),5))
    print("Max r  :",round(values.max(),5))
    print("Min r  :",round(values.min(),5))

print()
print("="*72)
print("EXP009 FINALIZADO")
print("="*72)
