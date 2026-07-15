import csv
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

INPUT="results/csv/ftrt_index_v2.csv"

f=[]
s=[]

with open(INPUT,newline="") as file:
    r=csv.DictReader(file)
    for row in r:
        f.append(float(row["ftrt_index_v2"]))
        s.append(float(row["ssn"]))

f=np.array(f)
s=np.array(s)


def classes(x):
    a,b=np.percentile(x,[33,66])
    y=np.zeros(len(x),dtype=int)
    y[x>a]=1
    y[x>b]=2
    return y


y=classes(s)


# variables temporales

lag30=np.roll(s,30)
lag30[:30]=s[:30]


X_ssn=lag30.reshape(-1,1)
X_ftrt=f.reshape(-1,1)

X_mix=np.column_stack(
    [lag30,f]
)


split=int(len(s)*0.7)


for name,X in [
    ("SSN 30d",X_ssn),
    ("FTRT",X_ftrt),
    ("COMBINADO",X_mix)
]:

    model=LogisticRegression(max_iter=1000)

    model.fit(
        X[:split],
        y[:split]
    )

    pred=model.predict(
        X[split:]
    )

    print(name)
    print(
        round(
        accuracy_score(y[split:],pred),
        5)
    )
    print("-"*30)

print("="*72)
print("EXP014 FINALIZADO")
print("="*72)
