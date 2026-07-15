import csv
import math
import random
import numpy as np

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

Xtrain=np.array(X[:split])
Ytrain=np.array(Y[:split])

Xtest=np.array(X[split:])
Ytest=np.array(Y[split:])


def model(A):
    coef=np.linalg.lstsq(A,Ytrain,rcond=None)[0]
    pred=Xtest[:,:A.shape[1]]@coef
    rmse=math.sqrt(np.mean((pred-Ytest)**2))
    return rmse,coef


# Modelo sin FTRT
rmse0,coef0=model(Xtrain[:,:2])

# Modelo con FTRT
rmse1,coef1=model(Xtrain)


# Permutación FTRT
Xperm=Xtrain.copy()
random.shuffle(Xperm[:,2])

coef=np.linalg.lstsq(Xperm,Ytrain,rcond=None)[0]

pred=Xtest@coef
rmse_perm=math.sqrt(np.mean((pred-Ytest)**2))


print("="*72)
print("EXP018 FEATURE SIGNIFICANCE")
print("="*72)

print("Sin FTRT RMSE :",round(rmse0,3))
print("Con FTRT RMSE :",round(rmse1,3))
print("Permutado RMSE:",round(rmse_perm,3))

print("Coef FTRT     :",round(coef1[2],5))

print("="*72)
