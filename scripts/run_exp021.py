import csv
import numpy as np
import math

INPUT="results/csv/ftrt_index_v2.csv"

rows=list(csv.DictReader(open(INPUT)))

X=[]
Y=[]

for i in range(60,len(rows)-30):

    ssn_now=float(rows[i]["ssn"])

    mean30=sum(
        float(r["ssn"])
        for r in rows[i-30:i]
    )/30

    trend=(
        float(rows[i]["ssn"])
        -
        float(rows[i-30]["ssn"])
    )

    ftrt=float(rows[i]["ftrt_index_v2"])

    X.append([
        1,
        ssn_now,
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
Ytr=Y[:split]

Xte=X[split:]
Yte=Y[split:]


def evaluate(Atrain,Atest):

    coef=np.linalg.lstsq(
        Atrain,
        Ytr,
        rcond=None
    )[0]

    pred=Atest@coef

    rmse=math.sqrt(
        np.mean((pred-Yte)**2)
    )

    return rmse,coef


# sin FTRT
rmse0,c0=evaluate(
    Xtr[:,:4],
    Xte[:,:4]
)

# con FTRT
rmse1,c1=evaluate(
    Xtr,
    Xte
)


print("="*72)
print("EXP021 AUTOCORRELATION CONTROL")
print("="*72)

print("Sin FTRT RMSE:",
      round(rmse0,3))

print("Con FTRT RMSE:",
      round(rmse1,3))

print("Delta RMSE:",
      round(rmse0-rmse1,3))

print("b_FTRT:",
      round(c1[-1],5))

print("="*72)
