#!/usr/bin/env python3

import csv

rows=list(csv.DictReader(open("data/catalog/master_catalog.csv")))

total=len(rows)

ok=sum(1 for r in rows if r["ftrt"]!="")

print("="*72)
print("CATALOG CHECK")
print("="*72)
print("Eventos :",total)
print("Con FTRT:",ok)
print("Cobertura:",round(100*ok/total,2),"%")
print("="*72)
