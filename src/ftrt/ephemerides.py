"""
FTRT Scientific Laboratory

Lector de efemérides JPL SPICE.

Requiere:
    spiceypy
    de440s.bsp
"""

from pathlib import Path
import numpy as np


KERNEL = Path(
    __file__
).parent.parent.parent / "de440s.bsp"



def cargar_kernel():

    import spiceypy as spice

    spice.furnsh(
        str(KERNEL)
    )

    return spice



def posicion_planeta(
    planeta,
    fecha
):

    spice = cargar_kernel()


    et = spice.str2et(
        fecha
    )


    cuerpo = {

        "mercury":199,
        "venus":299,
        "earth":399,
        "mars":499,
        "jupiter":599,
        "saturn":699

    }


    pos, _ = spice.spkpos(
        str(cuerpo[planeta]),
        et,
        "ECLIPJ2000",
        "NONE",
        "SUN"
    )


    return np.array(pos)



def posiciones_sistema(fecha):

    planetas=[
        "mercury",
        "venus",
        "earth",
        "mars",
        "jupiter",
        "saturn"
    ]


    return {

        p:posicion_planeta(
            p,
            fecha
        )

        for p in planetas

    }
