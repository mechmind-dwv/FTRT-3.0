import csv
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, balanced_accuracy_score


INPUT="results/csv/ftrt_index_v2.csv"

rows=list(csv.DictReader(open(INPUT)))

ssn=np.array([float(r["ssn"]) for r in rows])
ftrt=np.array([float(r["ftrt_index_v2"]) for r in rows])


X=[]
Y=[]

window=365
lag=30

threshold=117


for i in range(window,len(rows)-lag):

    mean365=np.mean(ssn[i-window:i])
    trend=ssn[i]-mean365

    X.append([
        mean365,
        trend,
        ftrt[i]
    ])

    Y.append(
        1 if ssn[i+lag]>=threshold else 0
    )


X=np.array(X)
Y=np.array(Y)


high=np.where(Y==1)[0]
low=np.where(Y==0)[0]


n=min(len(high),len(low))

rng=np.random.default_rng(42)

idx=np.concatenate([
    rng.choice(high,n,replace=False),
    rng.choice(low,n,replace=False)
])

rng.shuffle(idx)


X=X[idx]
Y=Y[idx]


split=int(len(X)*0.7)


Xtr=X[:split]
Xte=X[split:]

Ytr=Y[:split]
Yte=Y[split:]


for feat in ([0,1],[0,1,2]):

    model=LogisticRegression(
        max_iter=2000
    )

    model.fit(
        Xtr[:,feat],
        Ytr
    )

    p=model.predict_proba(
        Xte[:,feat]
    )[:,1]


    print("--------------------------------")
    print("Features:",feat)
    print("AUC:",
          round(roc_auc_score(Yte,p),4))
    print("Balanced accuracy:",
          round(balanced_accuracy_score(
              Yte,
              p>0.5
          ),4))


print("="*72)
