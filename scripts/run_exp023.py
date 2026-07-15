import csv
import numpy as np
import math

INPUT="results/csv/ftrt_index_v2.csv"

rows=list(csv.DictReader(open(INPUT)))

X=[]
Y=[]
dates=[]

for i in range(30,len(rows)-30):

    fecha=rows[i]["fecha"]

    ssn=float(rows[i]["ssn"])

    mean30=np.mean([
        float(r["ssn"])
        for r in rows[i-30:i]
    ])

    trend=ssn-float(rows[i-30]["ssn"])

    ftrt=float(rows[i]["ftrt_index_v2"])

    futuro=float(rows[i+30]["ssn"])

    X.append([
        1,
        mean30,
        trend,
        ftrt
    ])

    Y.append(futuro)
    dates.append(fecha)



X=np.array(X)
Y=np.array(Y)


train=[]
test=[]

for i,d in enumerate(dates):

    year=int(d[:4])

    if year<=2023:
        train.append(i)

    else:
        test.append(i)


Xtr=X[train]
Ytr=Y[train]

Xte=X[test]
Yte=Y[test]


coef=np.linalg.lstsq(
    Xtr,
    Ytr,
    rcond=None
)[0]


pred=Xte@coef


rmse=math.sqrt(
    np.mean((pred-Yte)**2)
)


print("="*72)
print("EXP023 CYCLE VALIDATION")
print("="*72)

print("Train:",len(train))
print("Test :",len(test))

print("Coef mean30 :",round(coef[1],5))
print("Coef trend  :",round(coef[2],5))
print("Coef FTRT   :",round(coef[3],5))

print("RMSE:",round(rmse,5))

print("="*72)
