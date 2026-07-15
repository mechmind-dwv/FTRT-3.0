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


future=[]

for i in range(365,len(rows)-30):
    future.append(
        ssn[i+30]-ssn[i]
    )


event_threshold=np.percentile(
    future,
    90
)


low_ssn=np.percentile(ssn,30)
high_ssn=np.percentile(ssn,70)


X=[]
Y=[]


for i in range(365,len(rows)-30):

    mean365=np.mean(
        ssn[i-365:i]
    )

    trend90=(
        ssn[i]-ssn[i-90]
    )


    # zona ambigua
    if not (
        low_ssn <= ssn[i] <= high_ssn
        and
        abs(trend90) < 25
    ):
        continue


    f30=np.mean(
        ftrt[i-30:i]
    )


    X.append([
        mean365,
        trend90,
        f30
    ])


    Y.append(
        1 if ssn[i+30]-ssn[i]>=event_threshold else 0
    )


X=np.array(X)
Y=np.array(Y)


print("="*72)
print("EXP042 FTRT HIDDEN TRANSITION TEST")
print("="*72)

print("Samples:",len(Y))
print("Events:",sum(Y))


if len(np.unique(Y))<2:
    print("No hay clases suficientes")
    exit()


split=int(len(X)*0.7)


Xtr=X[:split]
Xte=X[split:]

Ytr=Y[:split]
Yte=Y[split:]


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


    p=model.predict_proba(
        Xte[:,cols]
    )[:,1]


    pred=p>=0.5


    print("--------------------------------")
    print(name)

    print(
        "AUC:",
        round(
            roc_auc_score(Yte,p),
            4
        )
    )

    print(
        "Balanced accuracy:",
        round(
            balanced_accuracy_score(
                Yte,
                pred
            ),
            4
        )
    )

    print("Confusion:")
    print(
        confusion_matrix(
            Yte,
            pred
        )
    )


print("="*72)
