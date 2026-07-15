import csv
import numpy as np

INPUT="results/csv/ftrt_index_v2.csv"

rows=list(csv.DictReader(open(INPUT)))

ssn=np.array([float(r["ssn"]) for r in rows])
ftrt=np.array([float(r["ftrt_index_v2"]) for r in rows])

X=[]
Y=[]
REG=[]

window=365
lag=30

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


threshold=np.quantile(REG,0.66)

idx=np.where(REG>=threshold)[0]

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


base=rmse(Xtr[:,:3],Xte[:,:3])
full=rmse(Xtr,Xte)

real=base-full


rng=np.random.default_rng(42)

null=[]

for _ in range(2000):

    xp=Xtr.copy()

    xp[:,3]=rng.permutation(xp[:,3])

    null.append(
        rmse(xp[:,:3],Xte[:,:3])
        -
        rmse(xp,Xte)
    )


null=np.array(null)


print("="*72)
print("EXP032 QUANTILE HIGH REGIME PERMUTATION")
print("="*72)

print("Threshold:",
      round(threshold,3))

print("N:",
      len(X))

print("Base RMSE:",
      round(base,3))

print("Full RMSE:",
      round(full,3))

print("Real delta:",
      round(real,3))

print("Null mean:",
      round(np.mean(null),3))

print("p-value:",
      np.mean(null>=real))

print("="*72)
