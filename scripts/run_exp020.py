import csv
import numpy as np

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


rng=np.random.default_rng(42)

coefs=[]

for _ in range(1000):

    idx=rng.integers(
        0,
        len(X),
        len(X)
    )

    coef=np.linalg.lstsq(
        X[idx],
        Y[idx],
        rcond=None
    )[0]

    coefs.append(coef[2])


coefs=np.array(coefs)

print("="*72)
print("EXP020 BOOTSTRAP FTRT COEFFICIENT")
print("="*72)

print("Media b_FTRT:",
      round(np.mean(coefs),5))

print("IC95:",
      np.percentile(coefs,2.5),
      "-",
      np.percentile(coefs,97.5))

print("Probabilidad b>0:",
      round(np.mean(coefs>0),4))

print("="*72)
