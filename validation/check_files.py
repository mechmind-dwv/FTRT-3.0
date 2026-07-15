from pathlib import Path

FILES = [
    "results/csv/ftrt_index_v2.csv",
    "results/csv/ftrt_geometry_2020_2026.csv",
    "data/catalog/master_catalog.csv",
    "data/catalog/donki_catalog.csv",
]

print("="*72)
print("CHECK FILES")
print("="*72)

ok = True

for f in FILES:
    p = Path(f)
    if p.exists() and p.stat().st_size > 0:
        print(f"[OK] {f}")
    else:
        ok = False
        print(f"[ERROR] {f}")

print("="*72)
print("RESULTADO:", "OK" if ok else "ERROR")
print("="*72)
