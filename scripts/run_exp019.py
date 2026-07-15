import csv
import numpy as np
import math

INPUT="results/csv/ftrt_index_v2.csv"

rows=list(csv.DictReader(open(INPUT)))

X=[]
Y=[]

for i in range(30,len(rows)-30):
    mean30=sum(float(r["ssn"]) for r in rows[i-30:i])/30

    X.append([
        1,
        mean30,
        float(rows[i]["ftrt_index_v2"])
    ])

    Y.append(float(rows[i+30]["ssn"]))


X=np.array(X)
Y=np.array(Y)


folds=5
size=len(X)//folds

print("="*72)
print("EXP019 TEMPORAL CROSS VALIDATION")
print("="*72)

rmses=[]
coefs=[]

for k in range(1,folds):

    train_end=size*k

    Xtrain=X[:train_end]
    Ytrain=Y[:train_end]

    Xtest=X[train_end:train_end+size]
    Ytest=Y[train_end:train_end+size]


    coef=np.linalg.lstsq(
        Xtrain,
        Ytrain,
        rcond=None
    )[0]


    pred=Xtest@coef

    rmse=math.sqrt(
        np.mean((pred-Ytest)**2)
    )

    rmses.append(rmse)
    coefs.append(coef[2])


    print()
    print("Fold",k)
    print("RMSE:",round(rmse,3))
    print("b_FTRT:",round(coef[2],5))


print()
print("-"*72)
print("MEDIA RMSE:",round(np.mean(rmses),3))
print("STD RMSE:",round(np.std(rmses),3))
print("MEDIA b_FTRT:",round(np.mean(coefs),5))
print("STD b_FTRT:",round(np.std(coefs),5))

print("="*72)
