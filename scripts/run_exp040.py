import csv
import numpy as np


INPUT="results/csv/ftrt_index_v2.csv"

rows=list(csv.DictReader(open(INPUT)))

ssn=np.array([float(r["ssn"]) for r in rows])
ftrt=np.array([float(r["ftrt_index_v2"]) for r in rows])

windows=[7,14,21,30,45,60,90]


def build(w, f):

    X=[]
    Y=[]

    for i in range(365,len(rows)-30):

        mean365=np.mean(ssn[i-365:i])
        trend=ssn[i]-mean365

        fw=np.mean(
            f[i-w:i]
        )

        X.append([
            1,
            mean365,
            trend,
            fw
        ])

        Y.append(ssn[i+30])

    return np.array(X),np.array(Y)


def delta_for(w,f):

    X,Y=build(w,f)

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


    return (
        rmse(Xtr[:,:3],Xte[:,:3])
        -
        rmse(Xtr,Xte)
    )


real=[]

for w in windows:
    real.append(
        delta_for(w,ftrt)
    )

best_real=max(real)


rng=np.random.default_rng(42)

null_best=[]


for _ in range(1000):

    fp=rng.permutation(ftrt)

    vals=[]

    for w in windows:
        vals.append(
            delta_for(w,fp)
        )

    null_best.append(
        max(vals)
    )


null_best=np.array(null_best)


print("="*72)
print("EXP040 MULTIPLE WINDOW CORRECTION")
print("="*72)

print("Real best delta:",
      round(best_real,5))

print("Null mean:",
      round(np.mean(null_best),5))

print("Null 95%:",
      round(np.percentile(null_best,95),5))

print("p-value:",
      round(np.mean(null_best>=best_real),5))

print("="*72)
