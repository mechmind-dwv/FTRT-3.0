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

    trend=np.mean(
        ssn[i-window:i]
    )

    residual=ssn[i]-trend

    future_residual=(
        ssn[i+lag]
        -
        np.mean(ssn[i+lag-window:i+lag])
    )

    X.append([
        1,
        residual,
        ftrt[i]
    ])

    Y.append(future_residual)


X=np.array(X)
Y=np.array(Y)


split=int(len(X)*0.7)

Xtr=X[:split]
Xte=X[split:]

Ytr=Y[:split]
Yte=Y[split:]


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
print("EXP026 DETRENDED SOLAR RESIDUAL")
print("="*72)

print("Train:",len(Xtr))
print("Test :",len(Xte))

print("Coef residual:",
      round(coef[1],5))

print("Coef FTRT:",
      round(coef[2],5))

print("RMSE:",
      round(rmse,5))

print("="*72)
