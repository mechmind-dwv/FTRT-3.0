import csv

FILE="data/catalog/master_catalog.csv"

rows=list(csv.DictReader(open(FILE)))

fechas=[r["fecha"] for r in rows]

print("="*72)
print("CHECK DATES")
print("="*72)

print("Eventos:",len(fechas))
print("Primera:",min(fechas))
print("Última :",max(fechas))
print("Únicas :",len(set(fechas)))

if fechas==sorted(fechas):
    print("Orden : OK")
else:
    print("Orden : ERROR")
    raise SystemExit(1)

print("="*72)
