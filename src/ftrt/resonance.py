"""
FTRT Scientific Laboratory
Resonancias geométricas del Sistema Solar
"""

import numpy as np
from vector import angulo

def matriz_angulos(posiciones):
    """
    posiciones = {
        "earth": np.array([...]),
        "jupiter": ...
    }
    """
    nombres = list(posiciones.keys())
    n = len(nombres)

    M = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            M[i, j] = angulo(
                posiciones[nombres[i]],
                posiciones[nombres[j]]
            )

    return nombres, M


def imprimir(nombres, M):

    print("=" * 72)
    print("MATRIZ DE ÁNGULOS PLANETARIOS")
    print("=" * 72)

    print("".ljust(12), end="")

    for n in nombres:
        print(f"{n[:8]:>10}", end="")

    print()

    for i, nombre in enumerate(nombres):
        print(f"{nombre[:10]:<12}", end="")

        for j in range(len(nombres)):
            print(f"{M[i,j]:10.1f}", end="")

        print()
