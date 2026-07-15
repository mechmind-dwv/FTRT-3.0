#!/usr/bin/env python3

import subprocess
import time

steps = [
    ("EXP051", "scripts/run_exp051.py"),
    ("EXP052", "scripts/run_exp052.py"),
    ("EXP053", "scripts/run_exp053.py"),
    ("EXP054", "scripts/run_exp054.py"),
    ("EXP055", "scripts/run_exp055.py"),
    ("EXP056", "scripts/run_exp056.py"),
    ("EXP057", "scripts/run_exp057.py"),
    ("EXP058", "scripts/run_exp058.py"),
    ("EXP059", "scripts/run_exp059.py"),
]

print("=" * 72)
print("EXP060 - COMPLETE SCIENTIFIC PIPELINE")
print("=" * 72)

t0 = time.time()

ok = 0

for name, script in steps:

    print()
    print("-" * 72)
    print(name)
    print("-" * 72)

    r = subprocess.run(["python", script])

    if r.returncode == 0:
        ok += 1
    else:
        print("ERROR:", name)
        raise SystemExit(1)

print()
print("=" * 72)
print(f"Experimentos ejecutados : {ok}/{len(steps)}")
print(f"Tiempo total            : {time.time()-t0:.2f} s")
print("=" * 72)

print("\nEjecutando validación científica...\n")

subprocess.check_call([
    "python",
    "tests/run_scientific.py"
])

print("\nPIPELINE COMPLETADO")
