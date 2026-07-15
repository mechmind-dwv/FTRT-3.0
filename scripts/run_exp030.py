import csv
import numpy as np
import math

INPUT="results/csv/ftrt_index_v2.csv"

rows=list(csv.DictReader(open(INPUT)))

ssn=np.array([float(r["ssn"]) for r in rows])
ftrt=np.array([float(r["ftrt_index_v2"]) for r in rows])

X=[]
Y=[]
REG=[]

lag=30
window=365

for i in range(window,len(rows)-lag):

    mean365=np.mean(ssn[i-window:i])
    trend=ssn[i]-mean365

    X.append([
        1,
        mean365,
        trend,
        ftrt[i]
    ])

    Y.append(ssn[i+lag])
    REG.append(ssn[i])


X=np.array(X)
Y=np.array(Y)
REG=np.array(REG)


idx=np.where(REG>=117)[0]

X=X[idx]
Y=Y[idx]


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

for _ in range(1000):

    Xp=Xtr.copy()

    Xp[:,3]=rng.permutation(
        Xp[:,3]
    )

    null.append(
        rmse(Xp[:,:3],Xte[:,:3])
        -
        rmse(Xp,Xte)
    )


null=np.array(null)


print("="*72)
print("EXP030 HIGH SOLAR REGIME PERMUTATION")
print("="*72)

print("Base RMSE:",
round(base,3))

print("Full RMSE:",
round(full,3))

print("Real delta:",
round(real,3))

print("Null mean:",
round(np.mean(null),3))

print("p-value:",
round(np.mean(null>=real),5))

print("="*72)
