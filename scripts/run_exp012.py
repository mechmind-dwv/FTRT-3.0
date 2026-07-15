import csv
import numpy as np
from sklearn.metrics import accuracy_score

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


def classify(x):
    a,b=np.percentile(x,[33,66])
    y=np.zeros(len(x),dtype=int)
    y[x>a]=1
    y[x>b]=2
    return y


true=classify(ssn)

real=classify(ftrt)

print("="*72)
print("EXP012 TEMPORAL NULL MODEL")
print("="*72)

print("Real FTRT accuracy:",
      round(accuracy_score(true,real),5))


rng=np.random.default_rng(42)

scores=[]

for i in range(1000):
    shuffled=rng.permutation(ftrt)
    pred=classify(shuffled)
    scores.append(
        accuracy_score(true,pred)
    )

scores=np.array(scores)

print()
print("NULL 1000 permutations")
print("Mean:",
      round(scores.mean(),5))

print("95%:",
      round(np.percentile(scores,2.5),5),
      "-",
      round(np.percentile(scores,97.5),5))

print()
print("="*72)
print("EXP012 FINALIZADO")
print("="*72)
