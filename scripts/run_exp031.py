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


q1,q2=np.quantile(
    REG,
    [0.33,0.66]
)


print("="*72)
print("EXP031 QUANTILE REGIME VALIDATION")
print("="*72)

print("Thresholds:",
      round(q1,2),
      round(q2,2))


def rmse(A,B,ytr,yte):

    c=np.linalg.lstsq(
        A,
        ytr,
        rcond=None
    )[0]

    p=B@c

    return np.sqrt(
        np.mean((p-yte)**2)
    )


for name,a,b in [
    ("LOW",-999,q1),
    ("MID",q1,q2),
    ("HIGH",q2,999)
]:

    idx=np.where(
        (REG>=a)&
        (REG<b)
    )[0]


    split=int(len(idx)*0.7)

    tr=idx[:split]
    te=idx[split:]


    base=rmse(
        X[tr,:3],
        X[te,:3],
        Y[tr],
        Y[te]
    )

    full=rmse(
        X[tr],
        X[te],
        Y[tr],
        Y[te]
    )


    print("--------------------------------")
    print(name)
    print("N:",len(idx))
    print("Delta:",
          round(base-full,3))


print("="*72)
