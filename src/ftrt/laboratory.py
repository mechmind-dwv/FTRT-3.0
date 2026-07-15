"""
FTRT Scientific Laboratory
Versión 3.1-dev
"""

from datetime import datetime, UTC

class FTRTLaboratory:

    def __init__(self):
        self.version = "3.1-dev"

    def banner(self):
        print("="*60)
        print("FTRT SCIENTIFIC LABORATORY")
        print("="*60)
        print("Versión :", self.version)
        print("UTC      :", datetime.now(UTC).isoformat())
        print()

    def roadmap(self):
        print("Módulos científicos")
        print("-------------------")
        print("[ ] Efemérides JPL")
        print("[ ] Baricentro Solar")
        print("[ ] Geometría Planetaria")
        print("[ ] Fuerzas de Marea (FTRT)")
        print("[ ] Ciclos Orbitales")
        print("[ ] Datos NOAA/NASA")
        print("[ ] Validación Estadística")
        print("[ ] Predicción Experimental")

if __name__ == "__main__":
    lab = FTRTLaboratory()
    lab.banner()
    lab.roadmap()
