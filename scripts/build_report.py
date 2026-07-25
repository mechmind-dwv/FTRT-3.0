from pathlib import Path
import subprocess

md = Path("papers/FTRT_Experimental_Report.md")
html = Path("papers/FTRT_Experimental_Report.html")
pdf = Path("papers/FTRT_Experimental_Report.pdf")

subprocess.run([
    "pandoc",
    str(md),
    "-s",
    "-o",
    str(html)
], check=True)

subprocess.run([
    "pandoc",
    str(md),
    "--pdf-engine=typst",
    "-o",
    str(pdf)
], check=True)

print("="*60)
print("INFORME CIENTÍFICO GENERADO")
print("="*60)
print("Markdown :", md)
print("HTML     :", html)
print("PDF      :", pdf)
print("="*60)
