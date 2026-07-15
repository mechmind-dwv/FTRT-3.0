import csv
import numpy as np
import math


INPUT="results/csv/ftrt_index_v2.csv"


rows=list(csv.DictReader(open(INPUT)))


ssn=np.array([
    float(r["ssn"])
    for r in rows
])

ftrt=np.array([
    float(r["ftrt_index_v2"])
    for r in rows
])


X=[]
Y=[]


window=365
lag=30


for i in range(window,len(rows)-lag):

    mean365=np.mean(
        ssn[i-window:i]
    )

    anomaly_future = (
        ssn[i+lag]
        -
        mean365
    )

    trend = (
        ssn[i]
        -
        mean365
    )


    X.append([
        1,
        trend,
        ftrt[i]
    ])

    Y.append(
        anomaly_future
    )


X=np.array(X)
Y=np.array(Y)


split=int(len(X)*0.7)


Xtr=X[:split]
Xte=X[split:]

Ytr=Y[:split]
Yte=Y[split:]


def rmse(A,B):

    c=np.linalg.lstsq(
        A,
        Ytr,
        rcond=None
    )[0]

    pred=B@c

    return math.sqrt(
        np.mean(
            (pred-Yte)**2
        )
    )


base=rmse(
    Xtr[:,:2],
    Xte[:,:2]
)


full=rmse(
    Xtr,
    Xte
)


delta=base-full


print("="*72)
print("EXP036 RESIDUAL SOLAR INFORMATION TEST")
print("="*72)

print("BASE RMSE:",
      round(base,5))

print("FULL RMSE:",
      round(full,5))

print("Delta:",
      round(delta,5))

print("="*72)
