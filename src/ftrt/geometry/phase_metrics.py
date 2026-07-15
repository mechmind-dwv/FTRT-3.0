"""
FTRT Scientific Laboratory

Métricas colectivas del espacio de fase.
"""

import numpy as np



def metricas_fase(M):

    """
    M:
    matriz planetas x 12 estados
    """

    ocupacion = np.sum(
        M,
        axis=0
    )


    total = np.sum(ocupacion)


    if total > 0:

        p = ocupacion / total

    else:

        p = ocupacion



    estados_activos = np.sum(
        ocupacion > 0
    )


    entropia = 0.0


    for x in p:

        if x > 0:

            entropia -= x*np.log(x)



    concentracion = np.max(p)



    return {

        "estados_activos":
            int(estados_activos),

        "entropia_fase":
            float(entropia),

        "concentracion":
            float(concentracion),

        "ocupacion":
            ocupacion.tolist()

    }



def imprimir_metricas(datos):

    print("="*72)
    print("MÉTRICAS DE FASE")
    print("="*72)


    for k,v in datos.items():

        print(
            f"{k:<20}: {v}"
        )
