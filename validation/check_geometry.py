import csv

rows = list(csv.DictReader(open("results/csv/ftrt_geometry_2020_2026.csv")))

print("="*72)
print("CHECK GEOMETRY")
print("="*72)

print("Filas:", len(rows))
print("Inicio:", rows[0]["fecha"])
print("Fin   :", rows[-1]["fecha"])

print("="*72)
