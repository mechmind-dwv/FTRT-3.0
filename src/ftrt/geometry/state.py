"""
FTRT Scientific Laboratory

Estado geométrico del Sistema Solar.
Extrae variables de una matriz de resonancia.
"""

from __future__ import annotations

import numpy as np


def estado_geometrico(R):
    """
    Calcula características geométricas
    de una matriz de resonancia.
    """

    eig = np.linalg.eigvalsh(R)

    # energía espectral
    energia = np.sum(eig**2)


    # rango numérico
    rango = np.sum(
        np.abs(eig) > 1e-10
    )


    # usamos energía positiva para distribución
    pesos = eig**2

    if energia > 0:
        p = pesos / energia
    else:
        p = pesos


    # entropía espectral
    H = 0.0

    for x in p:

        if x > 0:
            H -= x * np.log(x)


    # coherencia:
    # concentración en el modo dominante

    coherencia = (
        np.max(p)
        if energia > 0
        else 0
    )


    return {

        "lambda_max":
            float(np.max(eig)),

        "lambda_min":
            float(np.min(eig)),

        "energia":
            float(energia),

        "rango":
            int(rango),

        "entropia":
            float(H),

        "coherencia":
            float(coherencia)

    }



def imprimir_estado(datos):

    print("="*72)
    print("ESTADO GEOMÉTRICO FTRT")
    print("="*72)

    for clave,valor in datos.items():

        print(
            f"{clave:<15}: {valor}"
        )
