#!/usr/bin/env python3
# EXP067 - Prediction History

from pathlib import Path
import csv
import statistics
from datetime import datetime, timezone


BASE = Path(__file__).resolve().parent.parent

CATALOG = BASE / "experiments/EXP064_master_catalog/results/master_catalog_v2.csv"

FTRT_FILE = BASE / "results/csv/ftrt_index_v2.csv"

OUT = BASE / "experiments/EXP067_prediction_history/results"


def classify_ftrt(value):

    if value >= 7:
        return "EXTREME"

    if value >= 5:
        return "HIGH"

    if value >= 2:
        return "MODERATE"

    return "LOW"



def main():

    print("="*72)
    print("EXP067 PREDICTION HISTORY")
    print("="*72)


    OUT.mkdir(parents=True, exist_ok=True)


    # cargar FTRT diario

    ftrt={}

    with open(FTRT_FILE,newline="") as f:

        for r in csv.DictReader(f):

            ftrt[r["fecha"]] = float(
                r["ftrt_index_v2"]
            )



    output=[]


    with open(CATALOG,newline="") as f:

        events=list(csv.DictReader(f))



    for e in events:

        fecha=e["fecha"]

        value=ftrt.get(fecha)


        output.append({

            "fecha":fecha,

            "clase":e["clase"],

            "region_activa":e["region_activa"],

            "ftrt":value if value is not None else "",

            "risk_level":
                classify_ftrt(value)
                if value is not None else "UNKNOWN",

            "timestamp":
                datetime.now(timezone.utc).isoformat()

        })



    file=OUT/"prediction_history.csv"


    with open(file,"w",newline="") as f:

        writer=csv.DictWriter(
            f,
            fieldnames=output[0].keys()
        )

        writer.writeheader()
        writer.writerows(output)



    values=[
        float(x["ftrt"])
        for x in output
        if x["ftrt"] != ""
    ]


    print("-"*72)

    print("Eventos registrados :",len(output))

    print("Con FTRT            :",len(values))


    if values:

        print(
            "Media FTRT          :",
            round(statistics.mean(values),6)
        )

        print(
            "Máximo FTRT         :",
            round(max(values),6)
        )



    print("-"*72)

    print("Archivo:")
    print(file)

    print("="*72)



if __name__=="__main__":
    main()

