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

    future=ssn[i+lag]

    X.append([
        1,
        mean365,
        trend,
        ftrt[i]
    ])

    Y.append(future)

    REG.append(ssn[i])


X=np.array(X)
Y=np.array(Y)
REG=np.array(REG)


def rmse(A,B,y1,y2):

    c=np.linalg.lstsq(
        A,
        y1,
        rcond=None
    )[0]

    p=B@c

    return math.sqrt(
        np.mean((p-y2)**2)
    )


print("="*72)
print("EXP029 SOLAR REGIME FTRT")
print("="*72)


regimes=[
    ("LOW",0,50),
    ("MEDIUM",50,117),
    ("HIGH",117,999)
]


for name,a,b in regimes:

    idx=np.where(
        (REG>=a)&
        (REG<b)
    )[0]


    if len(idx)<50:
        continue


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


    print("----------------------------------------")
    print(name)
    print("N:",len(idx))
    print("BASE:",
          round(base,3))
    print("FULL:",
          round(full,3))
    print("DELTA:",
          round(base-full,3))


print("="*72)
