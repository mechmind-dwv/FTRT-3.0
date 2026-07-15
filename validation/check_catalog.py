import csv

rows = list(csv.DictReader(open("data/catalog/master_catalog.csv")))

print("="*72)
print("CHECK MASTER CATALOG")
print("="*72)

print("Eventos :", len(rows))

con_ftrt = sum(1 for r in rows if r.get("ftrt"))

print("Con FTRT:", con_ftrt)

duplicados = len(rows) - len(set(r["id"] for r in rows))

print("Duplicados:", duplicados)

print("="*72)
