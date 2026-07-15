import csv
import numpy as np
import math

INPUT="results/csv/ftrt_index_v2.csv"

rows=list(csv.DictReader(open(INPUT)))

ssn=np.array([float(r["ssn"]) for r in rows])
ftrt=np.array([float(r["ftrt_index_v2"]) for r in rows])


X=[]
Y=[]

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


X=np.array(X)
Y=np.array(Y)


def rmse(Atrain,Btest,ytrain,ytest):

    c=np.linalg.lstsq(
        Atrain,
        ytrain,
        rcond=None
    )[0]

    pred=Btest@c

    return math.sqrt(
        np.mean((pred-ytest)**2)
    )


print("="*72)
print("EXP028 WALK FORWARD MODEL COMPARISON")
print("="*72)


window_test=180
start=1000

base_scores=[]
ftrt_scores=[]
full_scores=[]


while start+window_test < len(X):

    train_end=start
    test_end=start+window_test

    Xtr=X[:train_end]
    Xte=X[train_end:test_end]

    Ytr=Y[:train_end]
    Yte=Y[train_end:test_end]


    base=rmse(
        Xtr[:,0:3],
        Xte[:,0:3],
        Ytr,
        Yte
    )


    ftrt=rmse(
        Xtr[:,[0,3]],
        Xte[:,[0,3]],
        Ytr,
        Yte
    )


    full=rmse(
        Xtr,
        Xte,
        Ytr,
        Yte
    )


    base_scores.append(base)
    ftrt_scores.append(ftrt)
    full_scores.append(full)


    print("----------------------------------------")
    print("Window:",start,"-",test_end)
    print("BASE :",round(base,3))
    print("FTRT :",round(ftrt,3))
    print("FULL :",round(full,3))


    start += window_test


print("="*72)
print("EXP028 SUMMARY")
print("="*72)

print("BASE mean:",
      round(np.mean(base_scores),3))

print("FTRT mean:",
      round(np.mean(ftrt_scores),3))

print("FULL mean:",
      round(np.mean(full_scores),3))


print("Delta BASE-FULL:",
      round(
          np.mean(base_scores)
          -
          np.mean(full_scores),
          3
      ))

print("="*72)
