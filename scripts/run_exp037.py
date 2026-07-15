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


lag=30


for i in range(180,len(rows)-lag):

    f30=np.mean(
        ftrt[i-30:i]
    )

    f90=np.mean(
        ftrt[i-90:i]
    )

    f180=np.mean(
        ftrt[i-180:i]
    )

    fmax=np.max(
        ftrt[i-180:i]
    )


    mean365=np.mean(
        ssn[i-365:i]
    ) if i>=365 else np.mean(
        ssn[:i]
    )


    trend=ssn[i]-mean365


    X.append([
        1,
        mean365,
        trend,
        ftrt[i],
        f30,
        f90,
        f180,
        fmax
    ])


    Y.append(
        ssn[i+lag]
    )


X=np.array(X)
Y=np.array(Y)


split=int(len(X)*0.7)


Xtr=X[:split]
Xte=X[split:]

Ytr=Y[:split]
Yte=Y[split:]


def rmse(cols):

    c=np.linalg.lstsq(
        Xtr[:,cols],
        Ytr,
        rcond=None
    )[0]


    pred=Xte[:,cols]@c


    return math.sqrt(
        np.mean(
            (pred-Yte)**2
        )
    )


base=rmse([0,1,2])


tests={
"instant":[0,1,2,3],
"30d":[0,1,2,4],
"90d":[0,1,2,5],
"180d":[0,1,2,6],
"MAX180":[0,1,2,7],
"ALL":[0,1,2,3,4,5,6,7]
}


print("="*72)
print("EXP037 FTRT TEMPORAL MEMORY FEATURES")
print("="*72)

print("BASE RMSE:",
      round(base,5))


for name,cols in tests.items():

    r=rmse(cols)

    print("--------------------------------")
    print(name)
    print("RMSE:",
          round(r,5))
    print("Delta:",
          round(base-r,5))


print("="*72)
