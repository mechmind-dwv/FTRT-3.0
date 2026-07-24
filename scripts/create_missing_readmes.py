from pathlib import Path

ROOT=Path("experiments")

template="""# {name}

## Objetivo

Pendiente de documentar.

## Entrada

Describe aquí los datasets utilizados.

## Salida

Describe los archivos generados.

## Ejecución

```bash
PYTHONPATH=src python scripts/run_{script}.py

Resultados

Pendiente.

Estado

Implementado. """

for exp in ROOT.iterdir():

if not exp.is_dir():
    continue

if not exp.name.startswith("EXP"):
    continue

readme=exp/"README.md"

if readme.exists():
    continue

script=exp.name.lower()

readme.write_text(
    template.format(
        name=exp.name,
        script=script
    ),
    encoding="utf8"
)

print("Creado:",readme)

print("Finalizado.") EOF
```
"""
