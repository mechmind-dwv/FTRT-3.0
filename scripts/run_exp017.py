import csv
import math

INPUT="results/csv/ftrt_index_v2.csv"

X=[]
Y=[]

with open(INPUT) as f:
    rows=list(csv.DictReader(f))

for i in range(30,len(rows)-30):
    mean30=sum(float(r["ssn"]) for r in rows[i-30:i])/30
    
    X.append([
        1,
        mean30,
        float(rows[i]["ftrt_index_v2"])
    ])
    
    Y.append(float(rows[i+30]["ssn"]))


split=int(len(X)*0.7)

Xtrain=X[:split]
Ytrain=Y[:split]

Xtest=X[split:]
Ytest=Y[split:]


# resolver mínimos cuadrados con numpy si existe
try:
    import numpy as np
    
    A=np.array(Xtrain)
    b=np.array(Ytrain)

    coef=np.linalg.lstsq(A,b,rcond=None)[0]

    pred=[]
    for x in Xtest:
        pred.append(sum(a*c for a,c in zip(x,coef)))

    rmse=math.sqrt(
        sum((p-y)**2 for p,y in zip(pred,Ytest))
        /len(Ytest)
    )

    print("="*72)
    print("EXP017 MULTIVARIATE REGRESSION")
    print("="*72)
    print("a =",coef[0])
    print("b_ssn =",coef[1])
    print("b_ftrt =",coef[2])
    print("RMSE =",round(rmse,3))
    print("="*72)

except Exception as e:
    print(e)
