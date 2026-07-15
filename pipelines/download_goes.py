#!/usr/bin/env python3

from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "goes"
OUT.mkdir(parents=True, exist_ok=True)

FILES = {
    "goes_xray_events.json":
    "https://services.swpc.noaa.gov/json/goes/primary/xray-flares-latest.json"
}

print("="*72)
print("DOWNLOAD GOES")
print("="*72)

for name, url in FILES.items():
    dest = OUT / name
    print(f"Descargando {name}...")

    try:
        urllib.request.urlretrieve(url, dest)
        print(f"OK -> {dest}")
    except Exception as e:
        print(f"ERROR -> {e}")

print("="*72)
