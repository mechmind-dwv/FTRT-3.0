#!/usr/bin/env python3

from pathlib import Path
import pandas as pd

print("=" * 72)
print("FTRT SCIENTIFIC DASHBOARD")
print("=" * 72)

exp_dir = Path("experiments")

experiments = sorted(
    p for p in exp_dir.iterdir()
    if p.is_dir() and p.name.startswith("EXP")
)

print(f"Experimentos encontrados: {len(experiments)}")
print()

for exp in experiments:
    results = list((exp / "results").glob("*"))
    print(f"{exp.name:<35} {len(results)} archivos")
