"""
Baricentro del Sistema Solar
FTRT 3.1-dev
"""

import numpy as np

class SolarBarycenter:

    def __init__(self):
        self.planetas = {}

    def agregar(self, nombre, masa, posicion):
        """
        posicion = (x,y,z) en metros
        """
        self.planetas[nombre] = {
            "masa": masa,
            "r": np.asarray(posicion, dtype=float)
        }

    def calcular(self):

        masa_total = sum(p["masa"] for p in self.planetas.values())

        if masa_total == 0:
            return np.zeros(3)

        r = np.zeros(3)

        for p in self.planetas.values():
            r += p["masa"] * p["r"]

        return r / masa_total


if __name__ == "__main__":

    sb = SolarBarycenter()

    # Ejemplo simple
    sb.agregar("Jupiter",1.8982e27,(7.78e11,0,0))
    sb.agregar("Saturn",5.6834e26,(1.43e12,0,0))

    print("Baricentro (m):")
    print(sb.calcular())
