"""
FTRT Scientific Laboratory
Módulo de álgebra vectorial.
"""

from __future__ import annotations

import numpy as np


def norma(v):
    """Norma euclídea."""
    return np.linalg.norm(v)


def unitario(v):
    """Vector unitario."""
    n = norma(v)
    if n == 0:
        return v
    return v / n


def distancia(a, b):
    """Distancia entre dos vectores."""
    return norma(a - b)


def angulo(a, b):
    """
    Ángulo entre dos vectores (grados).
    """
    ua = unitario(a)
    ub = unitario(b)

    c = np.clip(np.dot(ua, ub), -1.0, 1.0)

    return np.degrees(np.arccos(c))


def alineados(a, b, tolerancia=5):
    """
    True si dos vectores forman casi una línea.
    """
    ang = angulo(a, b)

    return (
        ang <= tolerancia
        or abs(180 - ang) <= tolerancia
    )
