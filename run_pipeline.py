#!/usr/bin/env python3

from pathlib import Path
import subprocess
import time
import re
import csv
import os

SCRIPTS = Path("scripts")
LOG = Path("pipeline.log")
SUMMARY = Path("pipeline_summary.csv")

pattern = re.compile(r"run_exp(\d+)\.py$")

runs = []

for f in SCRIPTS.glob("run_exp*.py"):
    m = pattern.match(f.name)
    if m:
        runs.append((int(m.group(1)), f))

runs.sort()

inicio = time.time()

with open(LOG, "w", encoding="utf8") as log, \
     open(SUMMARY, "w", newline="", encoding="utf8") as fout:

    writer = csv.writer(fout)
    writer.writerow([
        "EXP",
        "Estado",
        "Tiempo_seg"
    ])

    print("="*72)
    print("FTRT COMPLETE PIPELINE")
    print("="*72)

    for numero, script in runs:

        print(f"\nEXP{numero:03d}")

        t0 = time.time()

        r = subprocess.run(
            ["python", str(script)],
            env={**os.environ, "PYTHONPATH": "src"},
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        tiempo = round(time.time()-t0,2)

        log.write("\n")
        log.write("="*72+"\n")
        log.write(script.name+"\n")
        log.write("="*72+"\n")
        log.write(r.stdout)

        estado = "OK" if r.returncode==0 else "ERROR"

        writer.writerow([
            f"EXP{numero:03d}",
            estado,
            tiempo
        ])

        print(estado, tiempo, "seg")

fin = round(time.time()-inicio,2)

print("\n"+"="*72)
print("PIPELINE FINALIZADO")
print("="*72)
print("Experimentos :", len(runs))
print("Tiempo total :", fin, "seg")
print("Resumen      :", SUMMARY)
print("Log          :", LOG)
