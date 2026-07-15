import csv
import numpy as np
import math

INPUT="results/csv/ftrt_index_v2.csv"

rows=list(csv.DictReader(open(INPUT)))

ssn=np.array([float(r["ssn"]) for r in rows])
ftrt=np.array([float(r["ftrt_index_v2"]) for r in rows])

X=[]
Y=[]

window=365
lag=30

for i in range(window,len(rows)-lag):

    base=np.mean(ssn[i-window:i])

    residual=ssn[i]-base

    future=ssn[i+lag]-np.mean(ssn[i+lag-window:i+lag])

    X.append([1,residual,ftrt[i]])
    Y.append(future)


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

    p=B@c

    return math.sqrt(
        np.mean((p-Yte)**2)
    )


base=rmse(
    Xtr[:,:2],
    Xte[:,:2]
)

full=rmse(
    Xtr,
    Xte
)

real=base-full


rng=np.random.default_rng(42)

null=[]

for _ in range(1000):

    Xp=Xtr.copy()

    Xp[:,2]=rng.permutation(Xp[:,2])

    null.append(
        rmse(Xp[:,:2],Xte[:,:2])
        -
        rmse(Xp,Xte)
    )


print("="*72)
print("EXP027 RESIDUAL FTRT PERMUTATION")
print("="*72)

print("Base RMSE:",
      round(base,5))

print("FTRT RMSE:",
      round(full,5))

print("Delta:",
      round(real,5))

print("Null mean:",
      round(np.mean(null),5))

print("p-value:",
      round(np.mean(np.array(null)>=real),5))

print("="*72)
