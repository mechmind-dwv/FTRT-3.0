import subprocess

TESTS = [
    "validation/check_files.py",
    "validation/check_geometry.py",
    "validation/check_ftrt.py",
    "validation/check_catalog.py",
    "validation/check_dates.py",
    "validation/check_join.py",
    "validation/check_statistics.py",
    "validation/check_duplicates.py",
]

ok = 0

print("="*72)
print("FTRT SCIENTIFIC VALIDATION")
print("="*72)

for t in TESTS:
    print(f"\n>>> {t}")
    r = subprocess.run(["python", t])
    if r.returncode == 0:
        ok += 1

print("\n"+"="*72)
print(f"PASADOS {ok}/{len(TESTS)}")
print("="*72)
