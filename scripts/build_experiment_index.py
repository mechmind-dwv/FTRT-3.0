from pathlib import Path
import os

ROOT = Path("experiments")
OUT = ROOT / "EXPERIMENT_INDEX.md"

lines = []

lines.append("# FTRT Scientific Laboratory")
lines.append("")
lines.append("## Master Experiment Index")
lines.append("")
lines.append("Este documento resume todos los experimentos del laboratorio.")
lines.append("")
lines.append("| EXP | Estado | README | Resultados |")
lines.append("|-----|--------|--------|------------|")

for exp in sorted(ROOT.iterdir()):

    if not exp.is_dir():
        continue

    if not exp.name.startswith("EXP"):
        continue

    readme = "README.md" if (exp/"README.md").exists() else "-"

    results = exp/"results"

    if results.exists():
        n = len(list(results.glob("*")))
        res = f"{n} archivos"
    else:
        res = "-"

    estado = "OK"

    lines.append(
        f"| {exp.name} | {estado} | {readme} | {res} |"
    )

OUT.write_text("\n".join(lines), encoding="utf-8")

print("="*72)
print("MASTER INDEX GENERADO")
print("="*72)
print(OUT)
