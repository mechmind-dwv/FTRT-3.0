#!/usr/bin/env python3
"""
EXP063 - Automatic FTRT Update
"""

from pathlib import Path
from datetime import datetime, timezone
import csv


BASE = Path(__file__).resolve().parent.parent

INPUT = BASE / "experiments/EXP062_auto_download/results/donki_update_report.csv"

OUTPUT = BASE / "experiments/EXP063_auto_update/results/ftrt_update_report.csv"


def main():

    print("="*72)
    print("EXP063 AUTOMATIC FTRT UPDATE")
    print("="*72)

    if not INPUT.exists():
        raise FileNotFoundError(INPUT)

    rows=[]

    with open(INPUT) as f:
        reader=csv.DictReader(f)
        for r in reader:
            rows.append(r)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT,"w",newline="") as f:
        writer=csv.writer(f)

        writer.writerow([
            "timestamp_utc",
            "events_processed",
            "status"
        ])

        writer.writerow([
            datetime.now(timezone.utc).isoformat(),
            len(rows),
            "OK"
        ])

    print(f"Eventos procesados : {len(rows)}")
    print(f"Archivo            : {OUTPUT}")
    print("="*72)


if __name__=="__main__":
    main()
