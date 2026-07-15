"""
Test matriz resonancia FTRT
"""

from resonance_matrix import matriz_resonancia, imprimir


longitudes = {

    "mercury": 120.0,
    "venus": 60.0,
    "earth": 0.0,
    "mars": 180.0,
    "jupiter": 240.0,
    "saturn": 300.0

}


nombres, R = matriz_resonancia(longitudes)

imprimir(nombres, R)


print()
print("=" * 72)
print("AUTOVALORES")
print("=" * 72)

import numpy as np

eig = np.linalg.eigvalsh(R)

for i, valor in enumerate(eig):
    print(f"lambda_{i+1}: {valor:.5f}")

from resonance_analysis import analizar

analizar(R)
