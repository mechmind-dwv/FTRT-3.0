import csv
import numpy as np
from sklearn.metrics import accuracy_score

INPUT="results/csv/ftrt_index_v2.csv"

dates=[]
ftrt=[]
ssn=[]

with open(INPUT,newline="") as f:
    r=csv.DictReader(f)
    for row in r:
        dates.append(row["fecha"])
        ftrt.append(float(row["ftrt_index_v2"]))
        ssn.append(float(row["ssn"]))

ftrt=np.array(ftrt)
ssn=np.array(ssn)


def classify(x):
    a,b=np.percentile(x,[33,66])
    y=np.zeros(len(x),dtype=int)
    y[x>a]=1
    y[x>b]=2
    return y


true=classify(ssn)

print("="*72)
print("EXP013 BASELINE COMPARISON")
print("="*72)


# FTRT

pred_ftrt=classify(ftrt)

print("FTRT:")
print(round(accuracy_score(true,pred_ftrt),5))


# tendencia temporal SSN suavizada

smooth=np.convolve(
    ssn,
    np.ones(30)/30,
    mode="same"
)

pred_smooth=classify(smooth)

print("30-day SSN mean:")
print(round(accuracy_score(true,pred_smooth),5))


# SSN desplazado 30 días

lag=np.roll(ssn,30)

pred_lag=classify(lag)

print("SSN lag 30:")
print(round(accuracy_score(true,pred_lag),5))


print("="*72)
print("EXP013 FINALIZADO")
print("="*72)
