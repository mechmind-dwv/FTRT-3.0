import csv
import numpy as np
import math

INPUT="results/csv/ftrt_index_v2.csv"

rows=list(csv.DictReader(open(INPUT)))

X=[]
Y=[]

for i in range(60,len(rows)-30):

    ssn=float(rows[i]["ssn"])

    mean30=sum(
        float(r["ssn"])
        for r in rows[i-30:i]
    )/30

    trend=ssn-float(rows[i-30]["ssn"])

    ftrt=float(rows[i]["ftrt_index_v2"])

    X.append([
        1,
        ssn,
        mean30,
        trend,
        ftrt
    ])

    Y.append(
        float(rows[i+30]["ssn"])
    )


X=np.array(X)
Y=np.array(Y)


split=int(len(X)*0.7)

Xtr=X[:split]
Xte=X[split:]

Ytr=Y[:split]
Yte=Y[split:]


def rmse(Atrain,Btest,ytrain,ytest):

    coef=np.linalg.lstsq(
        Atrain,
        ytrain,
        rcond=None
    )[0]

    pred=Btest@coef

    return math.sqrt(
        np.mean((pred-ytest)**2)
    )


real_base=rmse(
    Xtr[:,:4],
    Xte[:,:4],
    Ytr,
    Yte
)

real_full=rmse(
    Xtr,
    Xte,
    Ytr,
    Yte
)

delta_real=real_base-real_full


rng=np.random.default_rng(42)

deltas=[]

block=30


for _ in range(1000):

    shuffled=[]

    starts=list(range(0,len(Xtr),block))

    rng.shuffle(starts)

    for s in starts:
        shuffled.extend(
            Xtr[s:s+block,4]
        )

    Xnull=Xtr.copy()

    Xnull[:,4]=shuffled[:len(Xtr)]


    base=rmse(
        Xnull[:,:4],
        Xte[:,:4],
        Ytr,
        Yte
    )

    full=rmse(
        Xnull,
        Xte,
        Ytr,
        Yte
    )


    deltas.append(base-full)



deltas=np.array(deltas)


print("="*72)
print("EXP022 BLOCK PERMUTATION TEST")
print("="*72)

print("Delta real:",
      round(delta_real,5))

print("Media null:",
      round(np.mean(deltas),5))

print("IC95 null:",
      round(np.percentile(deltas,2.5),5),
      "-",
      round(np.percentile(deltas,97.5),5))

print("p-value:",
      round(np.mean(deltas>=delta_real),5))

print("="*72)
