#!/usr/bin/env python3

from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/"data"/"noaa"
OUT.mkdir(parents=True, exist_ok=True)

URL = "https://kauai.ccmc.gsfc.nasa.gov/DONKI/WS/get/FLR"

DEST = OUT/"donki_flares.json"

print("="*72)
print("DOWNLOAD DONKI")
print("="*72)

try:
    urllib.request.urlretrieve(URL, DEST)

    if DEST.stat().st_size == 0:
        raise RuntimeError("Archivo vacío")

    print("OK")
    print("Archivo:", DEST)
    print("Bytes:", DEST.stat().st_size)

except Exception as e:
    print("ERROR:", e)

print("="*72)
