from pathlib import Path
import re
from datetime import datetime

ROOT = Path("experiments")
OUT = ROOT / "README.md"

lines = []

lines.append("# FTRT-3.0 Experimental Laboratory")
lines.append("")
lines.append("## Índice automático de experimentos")
lines.append("")
lines.append("| Experimento | Estado | README |")
lines.append("|-------------|--------|--------|")

count = 0

for exp in sorted(ROOT.iterdir()):
    if not exp.is_dir():
        continue

    if not re.match(r"EXP\d+", exp.name):
        continue

    count += 1

    readme = exp / "README.md"

    estado = "✅" if readme.exists() else "❌"

    lines.append(
        f"| {exp.name} | {estado} | {readme.name if readme.exists() else '-'} |"
    )

lines.append("")
lines.append(f"Total experimentos: **{count}**")
lines.append("")
lines.append(f"Generado: {datetime.now()}")

OUT.write_text("\n".join(lines), encoding="utf8")

print("="*72)
print("EXP101 DOCUMENTATION INDEX")
print("="*72)
print("Experimentos:", count)
print("Archivo:", OUT)
print("="*72)
