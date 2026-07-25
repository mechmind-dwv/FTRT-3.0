from pathlib import Path
import subprocess
import sys

steps = [
    ["python", "scripts/run_all_experiments.py"],
    ["python", "scripts/build_experiment_index.py"],
    ["python", "scripts/build_paper.py"],
    ["python", "scripts/build_report.py"],
]

print("=" * 72)
print("FTRT-3.2 DEVELOPER MODE")
print("=" * 72)

for step in steps:
    print(">>>", " ".join(step))
    result = subprocess.run(step)
    if result.returncode != 0:
        print("ERROR:", " ".join(step))
        sys.exit(result.returncode)

print("=" * 72)
print("LABORATORIO COMPLETADO")
print("=" * 72)
