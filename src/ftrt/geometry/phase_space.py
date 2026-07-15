"""
FTRT Scientific Laboratory

Espacio de fases angular.

Convierte una fase circular continua
en estados discretos de análisis.

4 cuadrantes x 3 estados = 12 fases.
"""

from __future__ import annotations

import numpy as np


def normalizar_angulo(grados):
    """
    Lleva un ángulo a [0,360)
    """

    return grados % 360



def fase_continua(grados):
    """
    Convierte grados a radianes.
    """

    return np.radians(
        normalizar_angulo(grados)
    )



def estado_fase(grados):

    """
    Divide el círculo:

    4 cuadrantes
    3 estados internos

    Retorna:

    cuadrante
    etapa
    estado_12
    """

    angulo = normalizar_angulo(grados)


    # tamaño de cada cuadrante

    cuadrante = int(
        angulo // 90
    )


    # posición dentro del cuadrante

    local = angulo % 90


    etapa = int(
        local // 30
    )


    estado = (
        cuadrante * 3
        +
        etapa
    )


    return {
        "angulo": angulo,
        "cuadrante": cuadrante,
        "etapa": etapa,
        "estado_12": estado
    }



def vector_fase(grados):

    """
    Representación continua
    en círculo unitario.
    """

    rad = fase_continua(grados)

    return np.array([
        np.cos(rad),
        np.sin(rad)
    ])



def imprimir_estado(datos):

    print("="*72)
    print("ESTADO DE FASE")
    print("="*72)

    for k,v in datos.items():

        print(
            f"{k:<15}: {v}"
        )
