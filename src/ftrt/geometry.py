"""
Geometría del Sistema Solar
FTRT 3.1-dev
"""

from skyfield.api import load
import numpy as np

ts = load.timescale()
eph = load("de440s.bsp")

SUN = eph["sun"]

PLANETS = {
    "Mercury":"mercury barycenter",
    "Venus":"venus barycenter",
    "Earth":"earth barycenter",
    "Mars":"mars barycenter",
    "Jupiter":"jupiter barycenter",
    "Saturn":"saturn barycenter",
    "Uranus":"uranus barycenter",
    "Neptune":"neptune barycenter"
}

def posiciones(fecha=None):

    if fecha is None:
        t = ts.now()
    else:
        t = ts.utc(fecha.year,fecha.month,fecha.day)

    datos={}

    for nombre,obj in PLANETS.items():
        r=SUN.at(t).observe(eph[obj]).position.km
        datos[nombre]=np.array(r)

    return datos


if __name__=="__main__":

    d=posiciones()

    print("="*60)

    for p,v in d.items():

        dist=np.linalg.norm(v)

        print(f"{p:8s}  {dist:12.0f} km")
