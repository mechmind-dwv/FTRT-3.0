import csv

rows=list(csv.DictReader(open("data/catalog/master_catalog.csv")))

ids=[r["id"] for r in rows]

dup=len(ids)-len(set(ids))

print("="*72)
print("CHECK DUPLICATES")
print("="*72)

print("Eventos    :",len(rows))
print("Duplicados :",dup)

if dup==0:
    print("Estado : OK")
else:
    print("Estado : ERROR")
    raise SystemExit(1)

print("="*72)
