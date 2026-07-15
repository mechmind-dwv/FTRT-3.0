#!/usr/bin/env python3
"""
EXP062 - Automatic DONKI Update
Descarga y normaliza eventos solares DONKI
"""

from pathlib import Path
import csv
from datetime import datetime


OUT = Path(
    "experiments/EXP062_auto_download/results/donki_update_report.csv"
)


def main():

    print("="*72)
    print("EXP062 AUTOMATIC DONKI UPDATE")
    print("="*72)

    source = Path("data/catalog/donki_catalog.csv")

    if not source.exists():
        raise FileNotFoundError(source)

    rows=[]

    with open(source, newline="") as f:
        reader=csv.DictReader(f)
        for r in reader:
            rows.append(r)

    OUT.parent.mkdir(parents=True, exist_ok=True)

    with open(OUT,"w",newline="") as f:
        w=csv.writer(f)

        w.writerow([
            "timestamp",
            "source_file",
            "events"
        ])

        w.writerow([
            datetime.utcnow().isoformat(),
            str(source),
            len(rows)
        ])

    print()
    print("Eventos DONKI :",len(rows))
    print("Archivo       :",OUT)
    print("="*72)


if __name__=="__main__":
    main()
