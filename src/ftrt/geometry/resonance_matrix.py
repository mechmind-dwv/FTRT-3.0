"""
FTRT Scientific Laboratory

Matriz de resonancia geométrica del Sistema Solar.
Calcula relaciones angulares entre longitudes heliocéntricas.
"""

from __future__ import annotations

import numpy as np


def matriz_resonancia(longitudes):
    """
    Calcula la matriz armónica angular.

    Parámetros
    ----------
    longitudes : dict
        {
            "mercury": grados,
            "venus": grados,
            "earth": grados,
            ...
        }

    Retorna
    -------
    nombres, R
        nombres: lista de planetas
        R: matriz NxN con cos(theta_i - theta_j)
    """

    nombres = list(longitudes.keys())
    n = len(nombres)

    R = np.zeros((n, n))

    for i in range(n):
        for j in range(n):

            delta = np.radians(
                longitudes[nombres[i]]
                -
                longitudes[nombres[j]]
            )

            R[i, j] = np.cos(delta)

    return nombres, R


def imprimir(nombres, R):

    print("=" * 72)
    print("MATRIZ DE RESONANCIA ANGULAR")
    print("=" * 72)

    print("".ljust(12), end="")

    for nombre in nombres:
        print(f"{nombre[:8]:>10}", end="")

    print()

    for i, nombre in enumerate(nombres):

        print(f"{nombre[:10]:<12}", end="")

        for j in range(len(nombres)):
            print(f"{R[i,j]:10.3f}", end="")

        print()
