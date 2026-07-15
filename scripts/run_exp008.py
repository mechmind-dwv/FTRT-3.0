import csv
import numpy as np
from scipy.stats import pearsonr, spearmanr

INPUT="results/csv/ftrt_index_v2.csv"

fechas=[]
indices=[]
ssn=[]

with open(INPUT,newline="") as f:
    reader=csv.DictReader(f)
    for row in reader:
        fechas.append(row["fecha"])
        indices.append(float(row["ftrt_index_v2"]))
        ssn.append(float(row["ssn"]))

fechas=np.array(fechas)
indices=np.array(indices)
ssn=np.array(ssn)

print("="*72)
print("EXP008 INDEX ROBUSTNESS")
print("="*72)

# división temporal

mask_train=fechas < "2023-01-01"
mask_test=fechas >= "2023-01-01"


def report(nombre,x,y):
    print()
    print(nombre)
    print("-"*40)
    print("Registros:",len(x))
    print("Pearson :",round(pearsonr(x,y)[0],5))
    print("Spearman:",round(spearmanr(x,y)[0],5))


report(
    "TRAIN 2020-2022",
    indices[mask_train],
    ssn[mask_train]
)

report(
    "TEST 2023-2026",
    indices[mask_test],
    ssn[mask_test]
)


# Bootstrap

rng=np.random.default_rng(42)
r=[]

for i in range(1000):
    idx=rng.integers(0,len(indices),len(indices))
    r.append(
        pearsonr(
            indices[idx],
            ssn[idx]
        )[0]
    )

r=np.array(r)

print()
print("BOOTSTRAP 1000")
print("-"*40)
print("Media r :",round(np.mean(r),5))
print(
    "IC95    :",
    round(np.percentile(r,2.5),5),
    "-",
    round(np.percentile(r,97.5),5)
)

print()
print("="*72)
print("EXP008 FINALIZADO")
print("="*72)
