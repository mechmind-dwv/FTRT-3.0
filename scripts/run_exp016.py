import csv
import math

INPUT="results/csv/ftrt_index_v2.csv"

data=[]

with open(INPUT) as f:
    for r in csv.DictReader(f):
        data.append({
            "ssn":float(r["ssn"]),
            "ftrt":float(r["ftrt_index_v2"])
        })

for i in range(30,len(data)-30):
    mean30=sum(x["ssn"] for x in data[i-30:i])/30
    data[i]["mean30"]=mean30
    data[i]["target"]=data[i+30]["ssn"]

data=[x for x in data if "target" in x]


train=data[:int(len(data)*0.7)]
test=data[int(len(data)*0.7):]


def rmse(pred,true):
    return math.sqrt(sum((a-b)**2 for a,b in zip(pred,true))/len(true))


# Modelo 1: persistencia solar
p1=[x["mean30"] for x in test]
y=[x["target"] for x in test]


# Modelo 2: FTRT solo normalizado simple
p2=[x["ftrt"]*20+80 for x in test]


# Modelo 3 combinado
p3=[
    0.8*x["mean30"]+5*x["ftrt"]
    for x in test
]


print("="*72)
print("EXP016 ABLATION TEST")
print("="*72)

print("SSN baseline RMSE :",round(rmse(p1,y),3))
print("FTRT only RMSE    :",round(rmse(p2,y),3))
print("COMBINED RMSE     :",round(rmse(p3,y),3))

print("="*72)
