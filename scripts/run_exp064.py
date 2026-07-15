#!/usr/bin/env python3
"""
EXP064 - Master Catalog Builder
"""

from pathlib import Path
import csv
from datetime import datetime, timezone


BASE = Path(__file__).resolve().parent.parent


DONKI = BASE / "data/catalog/donki_catalog.csv"
FTRT = BASE / "results/csv/ftrt_index_v2.csv"

OUT = BASE / "experiments/EXP064_master_catalog/results/master_catalog_v2.csv"


def load_csv(path):

    if not path.exists():
        raise FileNotFoundError(path)

    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def main():

    print("="*72)
    print("EXP064 MASTER CATALOG BUILDER")
    print("="*72)

    donki = load_csv(DONKI)
    ftrt = load_csv(FTRT)

    print(f"DONKI eventos : {len(donki)}")
    print(f"FTRT filas    : {len(ftrt)}")

    ftrt_map={}

    for r in ftrt:
        fecha=r.get("fecha")

        if fecha:
            ftrt_map[fecha]=r


    OUT.parent.mkdir(parents=True, exist_ok=True)

    count=0

    with open(OUT,"w",newline="") as f:

        writer=csv.writer(f)

        writer.writerow([
            "fecha",
            "hora",
            "clase",
            "region_activa",
            "cme",
            "ftrt",
            "ssn",
            "builder_timestamp"
        ])

        for e in donki:

            fecha=e.get("fecha","")

            fr=ftrt_map.get(fecha,{})

            writer.writerow([
                fecha,
                e.get("hora",""),
                e.get("clase",""),
                e.get("region_activa",""),
                e.get("cme_asociada",""),
                fr.get("ftrt_index_v2",""),
                fr.get("ssn",""),
                datetime.now(timezone.utc).isoformat()
            ])

            count+=1


    print("-"*72)
    print(f"Eventos generados : {count}")
    print(f"Archivo           : {OUT}")
    print("="*72)


if __name__=="__main__":
    main()
