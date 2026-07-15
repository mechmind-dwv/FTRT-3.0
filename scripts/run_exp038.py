import csv
import numpy as np
import math


INPUT="results/csv/ftrt_index_v2.csv"


rows=list(csv.DictReader(open(INPUT)))


ssn=np.array([float(r["ssn"]) for r in rows])
ftrt=np.array([float(r["ftrt_index_v2"]) for r in rows])


X=[]
Y=[]


lag=30


for i in range(365,len(rows)-lag):

    mean365=np.mean(ssn[i-365:i])
    trend=ssn[i]-mean365

    f30=np.mean(ftrt[i-30:i])


    X.append([
        1,
        mean365,
        trend,
        f30
    ])

    Y.append(ssn[i+lag])


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

    return np.sqrt(
        np.mean((p-Yte)**2)
    )


base=rmse(
    Xtr[:,:3],
    Xte[:,:3]
)

full=rmse(
    Xtr,
    Xte
)


real=base-full


rng=np.random.default_rng(42)

null=[]


for _ in range(2000):

    xp=Xtr.copy()

    xp[:,3]=rng.permutation(
        xp[:,3]
    )

    delta=(
        rmse(xp[:,:3],Xte[:,:3])
        -
        rmse(xp,Xte)
    )

    null.append(delta)


null=np.array(null)


print("="*72)
print("EXP038 FTRT30 PERMUTATION")
print("="*72)

print("Base RMSE:",
      round(base,5))

print("Full RMSE:",
      round(full,5))

print("Real delta:",
      round(real,5))

print("Null mean:",
      round(np.mean(null),5))

print("p-value:",
      round(np.mean(null>=real),5))

print("="*72)
