import csv
import statistics

vals=[]

for r in csv.DictReader(open("results/csv/ftrt_index_v2.csv")):
    vals.append(float(r["ftrt_index_v2"]))

print("="*72)
print("CHECK STATISTICS")
print("="*72)

print("N      :",len(vals))
print("Media  :",round(statistics.mean(vals),6))
print("STD    :",round(statistics.stdev(vals),6))
print("Min    :",round(min(vals),6))
print("Max    :",round(max(vals),6))
print("Mediana:",round(statistics.median(vals),6))

print("="*72)
