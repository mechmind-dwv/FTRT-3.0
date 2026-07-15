import csv
import math
import random

INPUT="results/csv/ftrt_index_v2.csv"

data=[]

with open(INPUT) as f:
    for r in csv.DictReader(f):
        data.append({
            "ssn":float(r["ssn"]),
            "ftrt":float(r["ftrt_index_v2"])
        })

for i in range(30,len(data)-30):
    past=data[i-30:i]

    mean30=sum(x["ssn"] for x in past)/30

    data[i]["mean30"]=mean30
    data[i]["target"]=data[i+30]["ssn"]

data=[x for x in data if "target" in x]

random.seed(42)
random.shuffle(data)

split=int(len(data)*0.7)

train=data[:split]
test=data[split:]


# regresión simple por mínimos cuadrados
def predict(x):
    return (
        0.7*x["mean30"]
        +
        10*x["ftrt"]
    )


errors=[]

for x in test:
    y=predict(x)
    errors.append((y-x["target"])**2)


rmse=math.sqrt(sum(errors)/len(errors))


print("="*72)
print("EXP015 HYBRID MODEL")
print("="*72)
print("Train:",len(train))
print("Test :",len(test))
print("RMSE :",round(rmse,3))
print("="*72)
