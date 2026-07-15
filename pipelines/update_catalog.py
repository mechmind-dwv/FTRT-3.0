#!/usr/bin/env python3

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

PIPELINE = [
    "download_goes.py",
    "download_noaa.py",
    "download_cme.py",
    "merge_catalog.py",
    "build_features.py",
    "validate_catalog.py",
]

print("="*72)
print("FTRT 3.0 DATA PIPELINE")
print("="*72)

for script in PIPELINE:
    path = ROOT / "pipelines" / script

    if not path.exists():
        print(f"[SKIP] {script}")
        continue

    print(f"[RUN ] {script}")

    result = subprocess.run(
        [sys.executable, str(path)],
        cwd=ROOT
    )

    if result.returncode != 0:
        print(f"[FAIL] {script}")
        sys.exit(result.returncode)

print("="*72)
print("PIPELINE FINALIZADO")
print("="*72)
