import csv
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    roc_auc_score,
    balanced_accuracy_score,
    confusion_matrix
)


INPUT="results/csv/ftrt_index_v2.csv"


rows=list(csv.DictReader(open(INPUT)))


ssn=np.array([
    float(r["ssn"])
    for r in rows
])


ftrt=np.array([
    float(r["ftrt_index_v2"])
    for r in rows
])


future_delta=[]

for i in range(365,len(rows)-30):

    future_delta.append(
        ssn[i+30]-ssn[i]
    )


threshold=np.percentile(
    future_delta,
    90
)


X=[]
Y=[]


for i in range(365,len(rows)-30):

    mean365=np.mean(
        ssn[i-365:i]
    )

    trend=ssn[i]-mean365

    f30=np.mean(
        ftrt[i-30:i]
    )

    X.append([
        mean365,
        trend,
        f30
    ])

    Y.append(
        1 if ssn[i+30]-ssn[i]>=threshold else 0
    )


X=np.array(X)
Y=np.array(Y)


split=int(len(X)*0.7)


Xtr=X[:split]
Xte=X[split:]

Ytr=Y[:split]
Yte=Y[split:]


print("="*72)
print("EXP041 SOLAR TRANSITION EVENT DETECTION")
print("="*72)

print("Event threshold:",
      round(threshold,3))

for name,cols in {
    "BASE":[0,1],
    "FULL":[0,1,2]
}.items():

    model=LogisticRegression(
        max_iter=2000
    )

    model.fit(
        Xtr[:,cols],
        Ytr
    )

    prob=model.predict_proba(
        Xte[:,cols]
    )[:,1]

    pred=(prob>=0.5).astype(int)


    print("--------------------------------")
    print(name)

    print("AUC:",
          round(
              roc_auc_score(Yte,prob),
              4
          ))

    print("Balanced accuracy:",
          round(
              balanced_accuracy_score(
                  Yte,
                  pred
              ),
              4
          ))

    print("Confusion:")
    print(
        confusion_matrix(
            Yte,
            pred
        )
    )


print("="*72)
