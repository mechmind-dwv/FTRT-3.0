import csv
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix


INPUT="results/csv/ftrt_index_v2.csv"

rows=list(csv.DictReader(open(INPUT)))

ssn=np.array([float(r["ssn"]) for r in rows])
ftrt=np.array([float(r["ftrt_index_v2"]) for r in rows])


X=[]
Y=[]

window=365
lag=30


threshold=np.quantile(ssn,0.66)


for i in range(window,len(rows)-lag):

    mean365=np.mean(ssn[i-window:i])

    trend=ssn[i]-mean365

    future=ssn[i+lag]


    X.append([
        mean365,
        trend,
        ftrt[i]
    ])


    Y.append(
        1 if future>=threshold else 0
    )


X=np.array(X)
Y=np.array(Y)


split=int(len(X)*0.7)


Xtr=X[:split]
Xte=X[split:]

Ytr=Y[:split]
Yte=Y[split:]


def evaluate(features):

    model=LogisticRegression(
        max_iter=2000
    )

    model.fit(
        Xtr[:,features],
        Ytr
    )

    prob=model.predict_proba(
        Xte[:,features]
    )[:,1]


    pred=(prob>=0.5).astype(int)


    print("--------------------------------")
    print("Features:",features)
    print("Accuracy:",
          round(accuracy_score(Yte,pred),4))

    print("AUC:",
          round(roc_auc_score(Yte,prob),4))

    print("Confusion:")
    print(confusion_matrix(Yte,pred))


print("="*72)
print("EXP033 SOLAR ACTIVITY CLASSIFICATION")
print("="*72)

print("Threshold:",
      round(threshold,3))

evaluate([0,1])

evaluate([0,1,2])


print("="*72)
