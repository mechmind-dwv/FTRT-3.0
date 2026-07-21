#!/usr/bin/env python3

from pathlib import Path
import subprocess
import re

print("="*72)
print("FTRT EXPERIMENT AUDIT (EXP001-EXP100)")
print("="*72)

rows=[]

for n in range(1,101):
    script=Path(f"scripts/run_exp{n:03d}.py")

    if not script.exists():
        rows.append((n,"MISSING"))
        print(f"EXP{n:03d}: MISSING")
        continue

    try:
        p=subprocess.run(
            ["python",str(script)],
            capture_output=True,
            text=True,
            timeout=300,
            env={"PYTHONPATH":"src"}
        )

        if p.returncode==0:
            status="OK"
        else:
            status="FAIL"

        rows.append((n,status))

        print(f"EXP{n:03d}: {status}")

    except Exception:
        rows.append((n,"ERROR"))
        print(f"EXP{n:03d}: ERROR")

out=Path("experiments/EXP_AUDIT/results")
out.mkdir(parents=True,exist_ok=True)

with open(out/"audit.csv","w") as f:
    f.write("experiment,status\n")
    for n,s in rows:
        f.write(f"EXP{n:03d},{s}\n")

ok=sum(1 for _,s in rows if s=="OK")
fail=sum(1 for _,s in rows if s=="FAIL")
missing=sum(1 for _,s in rows if s=="MISSING")
error=sum(1 for _,s in rows if s=="ERROR")

print("-"*72)
print("OK      :",ok)
print("FAIL    :",fail)
print("MISSING :",missing)
print("ERROR   :",error)
print("Archivo :",out/"audit.csv")
print("="*72)
