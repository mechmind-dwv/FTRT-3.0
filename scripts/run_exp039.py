import csv
import numpy as np
import math


INPUT="results/csv/ftrt_index_v2.csv"

rows=list(csv.DictReader(open(INPUT)))

ssn=np.array([float(r["ssn"]) for r in rows])
ftrt=np.array([float(r["ftrt_index_v2"]) for r in rows])


windows=[7,14,21,30,45,60,90]


for w in windows:

    X=[]
    Y=[]

    for i in range(365,len(rows)-30):

        mean365=np.mean(ssn[i-365:i])
        trend=ssn[i]-mean365

        fw=np.mean(
            ftrt[i-w:i]
        )

        X.append([
            1,
            mean365,
            trend,
            fw
        ])

        Y.append(
            ssn[i+30]
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


    print(
        w,
        round(base-full,5)
    )
