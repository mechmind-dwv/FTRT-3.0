import csv
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    roc_auc_score,
    balanced_accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

INPUT="results/csv/ftrt_index_v2.csv"

rows=list(csv.DictReader(open(INPUT)))

ssn=np.array([float(r["ssn"]) for r in rows])
ftrt=np.array([float(r["ftrt_index_v2"]) for r in rows])

future=[]

for i in range(365,len(rows)-30):
    future.append(ssn[i+30]-ssn[i])

event_threshold=np.percentile(future,90)

low=np.percentile(ssn,30)
high=np.percentile(ssn,70)

X=[]
Y=[]

for i in range(365,len(rows)-30):

    mean365=np.mean(ssn[i-365:i])
    trend90=ssn[i]-ssn[i-90]
    f30=np.mean(ftrt[i-30:i])

    if not (low <= ssn[i] <= high and abs(trend90)<25):
        continue

    X.append([
        mean365,
        trend90,
        f30
    ])

    Y.append(
        1 if (ssn[i+30]-ssn[i])>=event_threshold else 0
    )

X=np.array(X)
Y=np.array(Y)

split=int(len(X)*0.7)

Xtr=X[:split]
Xte=X[split:]

Ytr=Y[:split]
Yte=Y[split:]

models={
    "BASE":[0,1],
    "FULL":[0,1,2]
}

thresholds=[
    0.05,0.10,0.15,0.20,
    0.25,0.30,0.40,0.50
]

print("="*72)
print("EXP043 THRESHOLD SWEEP")
print("="*72)

for name,cols in models.items():

    model=LogisticRegression(max_iter=2000)

    model.fit(Xtr[:,cols],Ytr)

    prob=model.predict_proba(Xte[:,cols])[:,1]

    print("\n"+name)
    print("-"*72)
    print("AUC:",round(roc_auc_score(Yte,prob),4))
    print()

    for t in thresholds:

        pred=(prob>=t).astype(int)

        ba=balanced_accuracy_score(Yte,pred)
        prec=precision_score(Yte,pred,zero_division=0)
        rec=recall_score(Yte,pred,zero_division=0)
        f1=f1_score(Yte,pred,zero_division=0)

        cm=confusion_matrix(Yte,pred)

        print(
            f"T={t:0.2f} | "
            f"BA={ba:.3f} | "
            f"P={prec:.3f} | "
            f"R={rec:.3f} | "
            f"F1={f1:.3f} | "
            f"TP={cm[1,1]} FP={cm[0,1]}"
        )

print("="*72)
