#!/usr/bin/env python3
# EXP071 - Null Model Validation

from pathlib import Path
from datetime import datetime, timezone
import csv
import random
import statistics


BASE = Path(__file__).resolve().parent.parent

INPUT = BASE / "experiments/EXP064_master_catalog/results/master_catalog_v2.csv"

RESULT = BASE / "experiments/EXP071_null_model_validation/results"


N_PERMUTATIONS = 10000


def load_events():

    events=[]

    with open(INPUT) as f:

        reader=csv.DictReader(f)

        for r in reader:

            if r["ftrt"]:

                events.append(
                    {
                        "fecha": r["fecha"],
                        "ftrt": float(r["ftrt"])
                    }
                )

    return events



def main():

    RESULT.mkdir(
        parents=True,
        exist_ok=True
    )


    print("="*72)
    print("EXP071 NULL MODEL VALIDATION")
    print("="*72)


    events=load_events()


    values=[
        e["ftrt"]
        for e in events
    ]


    observed=sum(
        v>1.5 for v in values
    )


    print("Eventos con FTRT:",len(values))
    print("Umbral:",1.5)
    print("Observados:",observed)


    null=[]


    for i in range(N_PERMUTATIONS):

        shuffled=values.copy()

        random.shuffle(shuffled)

        score=sum(
            x>1.5
            for x in shuffled
        )

        null.append(score)



    mean_null=statistics.mean(null)

    std_null=statistics.stdev(null)


    z=(observed-mean_null)/std_null if std_null else 0


    timestamp=datetime.now(
        timezone.utc
    ).isoformat()


    outfile=RESULT/"null_validation.csv"


    with open(outfile,"w",newline="") as f:

        writer=csv.writer(f)

        writer.writerow(
            [
                "timestamp",
                "events",
                "observed",
                "null_mean",
                "null_std",
                "z_score"
            ]
        )


        writer.writerow(
            [
                timestamp,
                len(values),
                observed,
                mean_null,
                std_null,
                z
            ]
        )


    print("-"*72)
    print("Null simulations:",N_PERMUTATIONS)
    print("Null mean:",mean_null)
    print("Null std:",std_null)
    print("Z score:",z)
    print("-"*72)
    print("Archivo:",outfile)
    print("="*72)



if __name__=="__main__":
    main()

