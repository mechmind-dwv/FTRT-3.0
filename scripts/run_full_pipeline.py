#!/usr/bin/env python3

import os
import subprocess
import sys
import time

PIPELINE = [

    "scripts/build_geometry_dataset.py",
    "scripts/quality_control.py",
    "scripts/build_manifest.py",
    "scripts/run_report.py",
    "scripts/validate_all.py",

    "scripts/merge_silso.py",

    "scripts/run_exp001.py",
    "scripts/run_exp002.py",
    "scripts/run_exp003.py",
    "scripts/run_exp004.py",
    "scripts/run_exp005.py",
    "scripts/run_exp006.py",
    "scripts/run_exp007.py",
    "scripts/run_exp008.py",
    "scripts/run_exp009.py",
    "scripts/run_exp010.py",
    "scripts/run_exp011.py",
    "scripts/run_exp012.py",
    "scripts/run_exp013.py",
    "scripts/run_exp014.py",
    "scripts/run_exp015.py",
    "scripts/run_exp016.py",
    "scripts/run_exp017.py",
    "scripts/run_exp018.py",
    "scripts/run_exp019.py",
    "scripts/run_exp020.py",
    "scripts/run_exp021.py",
    "scripts/run_exp022.py",
    "scripts/run_exp023.py",
    "scripts/run_exp024.py",
    "scripts/run_exp025.py",
    "scripts/run_exp026.py",
    "scripts/run_exp027.py",
    "scripts/run_exp028.py",
    "scripts/run_exp029.py",
    "scripts/run_exp030.py",
    "scripts/run_exp031.py",
    "scripts/run_exp032.py",
    "scripts/run_exp033.py",
    "scripts/run_exp034.py",
    "scripts/run_exp041.py",
    "scripts/run_exp042.py",
    "scripts/run_exp043.py",
    "scripts/run_exp044.py",
    "scripts/run_exp045.py",
    "scripts/run_exp046.py",
    "scripts/run_exp047.py",
    "scripts/run_exp048.py",
    "scripts/run_exp049.py",
    "scripts/run_exp050.py",
    "scripts/run_exp051.py",
]

print("="*72)
print("FTRT SCIENTIFIC LABORATORY")
print("FULL REPRODUCIBLE PIPELINE")
print("="*72)

start=time.time()

ok=0
fail=0

for script in PIPELINE:

    print()
    print("="*72)
    print(script)
    print("="*72)

    if not os.path.exists(script):
        print("NO EXISTE ->",script)
        fail+=1
        continue

    r=subprocess.run(
        [sys.executable,script],
        env=dict(os.environ, PYTHONPATH="src")
    )

    if r.returncode==0:
        ok+=1
    else:
        fail+=1

elapsed=time.time()-start

print()
print("="*72)
print("PIPELINE FINALIZADO")
print("="*72)
print("Correctos :",ok)
print("Errores   :",fail)
print("Tiempo    :",round(elapsed,1),"segundos")
print("="*72)
