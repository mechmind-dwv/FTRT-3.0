#!/usr/bin/env python3
# EXP076 - Leave One Active Region Out Analysis

from pathlib import Path
import csv
import statistics
from datetime import datetime, timezone

CATALOG = Path(
    "experiments/EXP064_master_catalog/results/master_catalog_v2.csv"
)

OUT = Path(
    "experiments/EXP076_leave_region_out/results/leave_region_out.csv"
)

THRESHOLD = 1.5


def load_events():

    rows=[]

    with open(CATALOG) as f:
        reader=csv.DictReader(f)

        for r in reader:

            try:
                ftrt=float(r["ftrt"])
            except:
                ftrt=None

            rows.append({
                "region": r["region_activa"],
                "ftrt": ftrt
            })

    return rows


def main():

    events=load_events()

    regions=sorted(
        set(r["region"] for r in events)
    )

    OUT.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    results=[]

    print("="*72)
    print("EXP076 LEAVE ONE REGION OUT")
    print("="*72)

    for region in regions:

        subset=[
            e for e in events
            if e["region"] != region
        ]

        hits=[
            e["ftrt"]
            for e in subset
            if e["ftrt"] is not None
            and e["ftrt"] >= THRESHOLD
        ]

        mean=(
            statistics.mean(hits)
            if hits else 0
        )

        maxv=max(hits) if hits else 0

        results.append([
            datetime.now(timezone.utc).isoformat(),
            region,
            len(subset),
            len(hits),
            round(mean,6),
            round(maxv,6)
        ])

        print(
            f"Sin {region}: "
            f"hits={len(hits)} "
            f"mean={mean:.3f} "
            f"max={maxv:.3f}"
        )


    with open(OUT,"w") as f:

        writer=csv.writer(f)

        writer.writerow([
            "timestamp",
            "removed_region",
            "events_remaining",
            "ftrt_hits",
            "mean_ftrt",
            "max_ftrt"
        ])

        writer.writerows(results)


    print("-"*72)
    print("Archivo:", OUT)
    print("="*72)


if __name__=="__main__":
    main()
