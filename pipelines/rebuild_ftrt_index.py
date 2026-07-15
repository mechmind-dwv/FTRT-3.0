import csv

GEOM="results/csv/ftrt_geometry_2020_2026.csv"
OUT="results/csv/ftrt_index_v2.csv"

rows=[]

with open(GEOM) as f:
    r=csv.DictReader(f)

    for x in r:

        fecha=x["fecha"]

        # localizar automáticamente la columna numérica principal
        valor=None
        for k,v in x.items():
            if k=="fecha":
                continue
            try:
                valor=float(v)
                break
            except:
                pass

        rows.append({
            "fecha":fecha,
            "ftrt_index_v2":valor,
            "ssn":""
        })

with open(OUT,"w",newline="") as f:
    w=csv.DictWriter(
        f,
        fieldnames=["fecha","ftrt_index_v2","ssn"]
    )
    w.writeheader()
    w.writerows(rows)

print("="*72)
print("FTRT INDEX RECONSTRUIDO")
print("="*72)
print("Filas :",len(rows))
print("Salida:",OUT)
print("="*72)
