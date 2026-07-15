"""
FTRT Scientific Laboratory

Análisis espectral de matrices de resonancia.
"""

import numpy as np


def analizar(R):

    print("=" * 72)
    print("ANÁLISIS ESPECTRAL")
    print("=" * 72)

    eig = np.linalg.eigvalsh(R)

    energia = np.sum(eig**2)

    print("\nAutovalores:")

    for i,e in enumerate(eig):
        print(f"lambda_{i+1}: {e:.6f}")

    print("\nRango numérico:")

    rango = np.sum(np.abs(eig) > 1e-10)

    print(rango)

    print("\nEnergía espectral:")

    print(energia)

    return eig
