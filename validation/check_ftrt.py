import csv

rows = list(csv.DictReader(open("results/csv/ftrt_index_v2.csv")))

vals = [float(r["ftrt_index_v2"]) for r in rows]

print("="*72)
print("CHECK FTRT")
print("="*72)

print("Días :", len(vals))
print("Min  :", min(vals))
print("Max  :", max(vals))
print("Media:", sum(vals)/len(vals))

print("="*72)
