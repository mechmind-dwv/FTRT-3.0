import subprocess

TESTS = [
    "validation/check_files.py",
    "validation/check_geometry.py",
    "validation/check_ftrt.py",
    "validation/check_catalog.py",
]

print("="*72)
print("FTRT 3.0 VALIDATION SUITE")
print("="*72)

ok = 0

for t in TESTS:
    print("\n>>>", t)
    r = subprocess.run(["python", t])
    if r.returncode == 0:
        ok += 1

print("\n" + "="*72)
print(f"SUPERADOS: {ok}/{len(TESTS)}")
print("="*72)
