import csv

rows=list(csv.DictReader(open("data/catalog/master_catalog.csv")))

n=len(rows)

ftrt=sum(r["ftrt"]!="" for r in rows)
ssn=sum(r["ssn"]!="" for r in rows)
region=sum(r["region_activa"]!="" for r in rows)

print("="*72)
print("CHECK JOIN")
print("="*72)

print(f"Eventos      : {n}")
print(f"Con FTRT     : {ftrt} ({100*ftrt/n:.1f}%)")
print(f"Con SSN      : {ssn} ({100*ssn/n:.1f}%)")
print(f"Con RegiónAR : {region} ({100*region/n:.1f}%)")

print("="*72)
