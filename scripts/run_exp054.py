# EXP054 - FTRT Scientific Pipeline
import csv
import random
import math

INPUT="data/catalog/master_catalog.csv"

con=[]
sin=[]

with open(INPUT) as f:
    for r in csv.DictReader(f):

        try:
            ftrt=float(r["ftrt"])
        except:
            continue

        cme=int(r["cme_asociada"] or 0)

        if cme>0:
            con.append(ftrt)
        else:
            sin.append(ftrt)

if len(con)==0 or len(sin)==0:
    print("No hay suficientes datos.")
    raise SystemExit

def media(x):
    return sum(x)/len(x)

obs = media(con)-media(sin)

todos = con + sin
n1 = len(con)

N = 10000
extremos = 0

random.seed(42)

for _ in range(N):

    random.shuffle(todos)

    a=todos[:n1]
    b=todos[n1:]

    d=media(a)-media(b)

    if abs(d)>=abs(obs):
        extremos+=1

p=(extremos+1)/(N+1)

print("="*72)
print("EXP054 PERMUTATION TEST")
print("="*72)
print("Con CME           :",len(con))
print("Sin CME           :",len(sin))
print()
print("Δ observado       :",round(obs,6))
print("Permutaciones     :",N)
print("p-value           :",round(p,6))
print("="*72)

OUT="experiments/EXP054_permutation/results/permutation_results.csv"

with open(OUT,"w") as f:
    f.write("delta_observado,p_value,n_perm\n")
    f.write(f"{obs},{p},{N}\n")

print("Archivo:",OUT)
