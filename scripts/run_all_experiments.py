#!/usr/bin/env python3

import os
import sys
import time
import subprocess

print("="*72)
print("FTRT SCIENTIFIC LABORATORY")
print("PIPELINE EXP001 → EXP100")
print("="*72)

inicio=time.time()

ok=0
skip=0
error=0

for n in range(1,101):

    script=f"scripts/run_exp{n:03d}.py"

    print()
    print("-"*72)
    print(f"EXP{n:03d}")

    if not os.path.exists(script):
        print("No implementado")
        skip+=1
        continue

    r=subprocess.run(
        [sys.executable, script],
        env={**os.environ, "PYTHONPATH":"src"}
    )

    if r.returncode==0:
        print("OK")
        ok+=1
    else:
        print("ERROR")
        error+=1

print()
print("="*72)
print("RESUMEN FINAL")
print("="*72)
print("Experimentos ejecutados :", ok)
print("No implementados        :", skip)
print("Errores                 :", error)
print("Tiempo total            :", round(time.time()-inicio,2), "seg")
print("="*72)
