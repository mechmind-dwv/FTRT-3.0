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

    X.append([1,mean30,trend,ftrt])
    Y.append(futuro)


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

    Xperm=Xtr.copy()

    Xperm[:,3]=rng.permutation(
        Xperm[:,3]
    )

    null.append(
        rmse(Xperm[:,:3],Xte[:,:3])
        -
        rmse(Xperm,Xte)
    )


null=np.array(null)


print("="*72)
print("EXP025 PREDICTIVE PERMUTATION")
print("="*72)

print("Real delta:",round(real,5))

print("Null mean:",
      round(np.mean(null),5))

print("p-value:",
      round(np.mean(null>=real),5))

print("="*72)
