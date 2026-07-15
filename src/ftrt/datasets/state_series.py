"""
FTRT Scientific Laboratory

Generador de series temporales geométricas.
"""

import sys
from pathlib import Path

# Añadir raíz ftrt al PATH
BASE = Path(__file__).resolve().parent.parent

sys.path.append(str(BASE))


from geometry.resonance_matrix import matriz_resonancia
from geometry.state import estado_geometrico


from datetime import datetime, timedelta
import csv



def generar(dias=30):

    fecha = datetime(2026,1,1)

    resultados=[]


    for i in range(dias):

        longitudes = {

            "mercury":120+i*1.6,
            "venus":60+i*0.6,
            "earth":i*0.98,
            "mars":180+i*0.52,
            "jupiter":240+i*0.08,
            "saturn":300+i*0.03

        }


        _,R = matriz_resonancia(longitudes)


        estado = estado_geometrico(R)


        estado["fecha"] = (
            fecha + timedelta(days=i)
        ).isoformat()


        resultados.append(estado)


    return resultados




def guardar(datos, archivo):

    campos = list(datos[0].keys())


    with open(
        archivo,
        "w",
        newline=""
    ) as f:

        writer = csv.DictWriter(
            f,
            fieldnames=campos
        )

        writer.writeheader()
        writer.writerows(datos)




if __name__ == "__main__":

    datos = generar(30)

    guardar(
        datos,
        "ftrt_geometry_series.csv"
    )


    print(
        "Dataset generado:",
        len(datos),
        "registros"
    )
