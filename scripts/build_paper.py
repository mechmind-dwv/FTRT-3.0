from pathlib import Path
from datetime import datetime

ROOT = Path("experiments")
OUT = Path("papers/FTRT_Experimental_Report.md")

lines = []

lines.append("# FTRT-3.0 Experimental Report")
lines.append("")
lines.append("Generado automáticamente.")
lines.append("")
lines.append("Fecha: " + str(datetime.now()))
lines.append("")
lines.append("---")
lines.append("")

experiments = sorted([d for d in ROOT.iterdir() if d.is_dir()])

for exp in experiments:

    lines.append(f"## {exp.name}")
    lines.append("")

    readme = exp / "README.md"

    if readme.exists():
        lines.append(readme.read_text(encoding="utf8"))
    else:
        lines.append("*Sin documentación.*")

    lines.append("")
    lines.append("---")
    lines.append("")

OUT.write_text("\n".join(lines), encoding="utf8")

print("="*72)
print("DOCUMENTO GENERADO")
print("="*72)
print(OUT)
