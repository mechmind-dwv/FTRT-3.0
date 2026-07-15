import csv
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    roc_curve,
    roc_auc_score,
    precision_recall_curve,
    average_precision_score
)

INPUT="results/csv/ftrt_index_v2.csv"

rows=list(csv.DictReader(open(INPUT)))

ssn=np.array([float(r["ssn"]) for r in rows])
ftrt=np.array([float(r["ftrt_index_v2"]) for r in rows])

future=[ssn[i+30]-ssn[i] for i in range(365,len(rows)-30)]
thr=np.percentile(future,90)

low=np.percentile(ssn,30)
high=np.percentile(ssn,70)

X=[]
Y=[]

for i in range(365,len(rows)-30):

    mean365=np.mean(ssn[i-365:i])
    trend90=ssn[i]-ssn[i-90]
    f30=np.mean(ftrt[i-30:i])

    if not(low<=ssn[i]<=high and abs(trend90)<25):
        continue

    X.append([mean365,trend90,f30])
    Y.append(1 if ssn[i+30]-ssn[i]>=thr else 0)

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

plt.figure(figsize=(6,6))

for name,cols in models.items():

    m=LogisticRegression(max_iter=2000)
    m.fit(Xtr[:,cols],Ytr)

    p=m.predict_proba(Xte[:,cols])[:,1]

    fpr,tpr,_=roc_curve(Yte,p)

    print()
    print(name)
    print("ROC AUC :",round(roc_auc_score(Yte,p),4))
    print("PR AUC  :",round(average_precision_score(Yte,p),4))

    plt.plot(fpr,tpr,label=name)

plt.plot([0,1],[0,1],'--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("EXP044 ROC")
plt.legend()

plt.tight_layout()

plt.savefig(
"experiments/EXP044_roc.png",
dpi=200
)

plt.close()

plt.figure(figsize=(6,6))

for name,cols in models.items():

    m=LogisticRegression(max_iter=2000)
    m.fit(Xtr[:,cols],Ytr)

    p=m.predict_proba(Xte[:,cols])[:,1]

    prec,rec,_=precision_recall_curve(Yte,p)

    plt.plot(rec,prec,label=name)

plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("EXP044 Precision-Recall")
plt.legend()

plt.tight_layout()

plt.savefig(
"experiments/EXP044_pr.png",
dpi=200
)

print("\nFiguras guardadas:")
print("experiments/EXP044_roc.png")
print("experiments/EXP044_pr.png")
