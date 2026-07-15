import csv
import numpy as np
import math

INPUT="results/csv/ftrt_index_v2.csv"

rows=list(csv.DictReader(open(INPUT)))

X=[]
Y=[]

for i in range(30,len(rows)-30):

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


X=np.array(X)
Y=np.array(Y)


split=int(len(X)*0.7)

Xtr=X[:split]
Xte=X[split:]

Ytr=Y[:split]
Yte=Y[split:]


def calc(A,B):

    c=np.linalg.lstsq(
        A,
        Ytr,
        rcond=None
    )[0]

    p=B@c

    return math.sqrt(
        np.mean((p-Yte)**2)
    )


rmse_base=calc(
    Xtr[:,:3],
    Xte[:,:3]
)

rmse_ftrt=calc(
    Xtr,
    Xte
)


print("="*72)
print("EXP024 OUT OF SAMPLE ABLATION")
print("="*72)

print("BASE RMSE :",round(rmse_base,5))
print("FTRT RMSE :",round(rmse_ftrt,5))
print("DELTA     :",round(rmse_base-rmse_ftrt,5))

print("="*72)
