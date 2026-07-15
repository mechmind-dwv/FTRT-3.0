"""
FTRT Scientific Laboratory

Efemérides JPL mediante Skyfield.

Backend:
    de440s.bsp
"""

from pathlib import Path
import numpy as np

from skyfield.api import load


KERNEL = (
    Path(__file__).parent.parent.parent
    / "de440s.bsp"
)


PLANETS = {

    "mercury": "mercury barycenter",
    "venus": "venus barycenter",
    "earth": "earth barycenter",
    "mars": "mars barycenter",
    "jupiter": "jupiter barycenter",
    "saturn": "saturn barycenter",

}



def cargar_ephemeris():

    return load(
        str(KERNEL)
    )



def longitud_heliocentrica(pos):

    """
    Convierte XYZ heliocéntrico
    en longitud orbital grados.
    """

    x,y,z = pos

    angulo = np.degrees(
        np.arctan2(y,x)
    )

    return angulo % 360



def posiciones_sistema(fecha):

    eph = cargar_ephemeris()

    ts = load.timescale()

    t = ts.utc(
        fecha.year,
        fecha.month,
        fecha.day
    )


    sol = eph["sun"]


    resultado={}


    for nombre,cuerpo in PLANETS.items():

        planeta = eph[cuerpo]


        posicion = (
            planeta.at(t)
            .observe(sol)
            .position.km
        )


        resultado[nombre] = np.array(
            posicion
        )


    return resultado



def longitudes_sistema(fecha):

    posiciones = posiciones_sistema(
        fecha
    )


    return {

        planeta:
        longitud_heliocentrica(pos)

        for planeta,pos in posiciones.items()

    }
