import csv
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, log_loss


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


def train_eval(cols):

    model=LogisticRegression(
        max_iter=2000
    )

    model.fit(
        Xtr[:,cols],
        Ytr
    )

    p=model.predict_proba(
        Xte[:,cols]
    )[:,1]

    return (
        roc_auc_score(Yte,p),
        log_loss(Yte,p)
    )


auc_base,ll_base=train_eval([0,1])

auc_full,ll_full=train_eval([0,1,2])


print("="*72)
print("EXP035 INCREMENTAL FTRT INFORMATION")
print("="*72)

print("BASE")
print("AUC:",round(auc_base,5))
print("LogLoss:",round(ll_base,5))

print("--------------------------------")

print("FULL")
print("AUC:",round(auc_full,5))
print("LogLoss:",round(ll_full,5))

print("--------------------------------")

print("Delta AUC:",
      round(auc_full-auc_base,5))

print("Delta LogLoss:",
      round(ll_base-ll_full,5))

print("="*72)
