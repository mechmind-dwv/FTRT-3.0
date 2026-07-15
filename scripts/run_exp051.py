#!/usr/bin/env python3

import csv
import numpy as np

INPUT = "data/catalog/master_catalog.csv"

rows = list(csv.DictReader(open(INPUT, encoding="utf-8")))

groups = {
    "M5+": [],
    "M8+": [],
    "X1+": [],
    "X2+": [],
    "X5+": []
}


def parse_goes(clase):
    if clase is None:
        return None

    clase = clase.strip().upper()

    if clase == "":
        return None

    letra = clase[0]

    try:
        valor = float(clase[1:])
    except Exception:
        return None

    return letra, valor


conteo = {
    "C": 0,
    "M": 0,
    "X": 0
}


for r in rows:

    p = parse_goes(r.get("clase", ""))

    if p is None:
        continue

    letra, valor = p

    if letra in conteo:
        conteo[letra] += 1

    try:
        ftrt = float(r["ftrt"])
    except Exception:
        continue

    try:
        ssn = float(r["ssn"])
    except Exception:
        ssn = np.nan

    dato = {
        "ftrt": ftrt,
        "ssn": ssn,
        "fecha": r.get("fecha", ""),
        "clase": r.get("clase", "")
    }

    if letra == "M":

        if valor >= 5:
            groups["M5+"].append(dato)

        if valor >= 8:
            groups["M8+"].append(dato)

    elif letra == "X":

        if valor >= 1:
            groups["X1+"].append(dato)

        if valor >= 2:
            groups["X2+"].append(dato)

        if valor >= 5:
            groups["X5+"].append(dato)


print("=" * 72)
print("EXP051 GOES CLASS VALIDATION")
print("=" * 72)

print("Eventos totales :", len(rows))
print("Clase C         :", conteo["C"])
print("Clase M         :", conteo["M"])
print("Clase X         :", conteo["X"])

print("=" * 72)

for nombre, datos in groups.items():

    print("-" * 72)
    print(nombre)

    if len(datos) == 0:
        print("Sin eventos")
        continue

    ftrt = np.array([x["ftrt"] for x in datos], dtype=float)
    ssn = np.array([x["ssn"] for x in datos], dtype=float)

    print("N            :", len(datos))
    print("FTRT medio   :", round(np.nanmean(ftrt), 6))
    print("FTRT mediana :", round(np.nanmedian(ftrt), 6))
    print("FTRT máximo  :", round(np.nanmax(ftrt), 6))
    print("FTRT mínimo  :", round(np.nanmin(ftrt), 6))
    print("SSN medio    :", round(np.nanmean(ssn), 2))

    print()

    for e in datos:
        print(
            f'  {e["fecha"]}   {e["clase"]:>4}   FTRT={e["ftrt"]:.6f}'
        )

print("=" * 72)
print("FIN EXP051")
print("=" * 72)
