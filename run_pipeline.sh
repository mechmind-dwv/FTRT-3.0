#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "=============================================="
echo "FTRT SCIENTIFIC PIPELINE"
echo "=============================================="

export PYTHONPATH=src

echo
echo "[1/4] Generando dataset..."
python scripts/generate_geometry_dataset.py

echo
echo "[2/4] Control de calidad..."
python scripts/qc_geometry_dataset.py

echo
echo "[3/4] Manifest..."
python scripts/experiment_manifest.py

echo
echo
echo "[4/5] Run report..."
python scripts/run_report.py
echo
echo "[5/5] Finalizado."


echo
echo "Pipeline completado correctamente."

echo
echo "[6/6] Validación completa..."
PYTHONPATH=src python scripts/validate_project.py
