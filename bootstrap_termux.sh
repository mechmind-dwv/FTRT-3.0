#!/data/data/com.termux/files/usr/bin/bash

echo "=== FTRT 3.0 - Bootstrap ==="

mkdir -p \
src \
src/ftrt \
src/geometry \
src/validation \
src/physics \
src/utils \
scripts \
tests \
docs \
reports \
data/raw \
data/processed \
data/external \
notebooks

touch \
src/__init__.py \
src/ftrt/__init__.py \
src/geometry/__init__.py \
src/validation/__init__.py \
src/physics/__init__.py \
src/utils/__init__.py

cat > run.sh <<'RUN'
#!/data/data/com.termux/files/usr/bin/bash

echo "===================================="
echo " FTRT 3.0 Scientific Laboratory"
echo "===================================="

python src/main.py
RUN

chmod +x run.sh

cat > src/main.py <<'PY'
from datetime import datetime
import numpy as np
import scipy

print("FTRT 3.0")
print("---------------------------")
print("Fecha:", datetime.utcnow())
print("NumPy:", np.__version__)
print("SciPy:", scipy.__version__)
print()
print("Laboratorio correctamente inicializado.")
PY

echo
echo "Bootstrap completado."
echo "Ejecuta:"
echo "./run.sh"
