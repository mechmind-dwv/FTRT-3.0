import csv
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix

INPUT="results/csv/ftrt_index_v2.csv"

ftrt=[]
ssn=[]

with open(INPUT,newline="") as f:
    r=csv.DictReader(f)
    for row in r:
        ftrt.append(float(row["ftrt_index_v2"]))
        ssn.append(float(row["ssn"]))

ftrt=np.array(ftrt)
ssn=np.array(ssn)

print("="*72)
print("EXP011 SOLAR REGIME CLASSIFICATION")
print("="*72)

# clases reales SSN

s1,s2=np.percentile(ssn,[33,66])

true=np.zeros(len(ssn),dtype=int)
true[ssn>s1]=1
true[ssn>s2]=2


# predicción por FTRT

f1,f2=np.percentile(ftrt,[33,66])

pred=np.zeros(len(ftrt),dtype=int)
pred[ftrt>f1]=1
pred[ftrt>f2]=2


print("SSN thresholds:",s1,s2)
print("FTRT thresholds:",f1,f2)

print()
print("Accuracy:",
      round(accuracy_score(true,pred),5))

print()
print("Confusion matrix:")
print(confusion_matrix(true,pred))

print("="*72)
print("EXP011 FINALIZADO")
print("="*72)
