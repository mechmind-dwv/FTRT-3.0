"""
FTRT Scientific Laboratory

Matriz de ocupación de fases planetarias.
"""

import numpy as np

from .phase_space import estado_fase



def matriz_fases(longitudes):

    nombres=list(longitudes.keys())

    estados=[]


    for planeta in nombres:

        fase = estado_fase(
            longitudes[planeta]
        )

        estados.append(
            fase["estado_12"]
        )


    M=np.zeros(
        (len(nombres),12),
        dtype=int
    )


    for i,estado in enumerate(estados):

        M[i,estado]=1


    return nombres,M,estados




def imprimir(nombres,M):

    print("="*72)
    print("MATRIZ DE FASE PLANETARIA")
    print("="*72)


    print(
        "".ljust(12),
        end=""
    )

    for i in range(12):
        print(
            f"{i:3}",
            end=""
        )

    print()


    for i,nombre in enumerate(nombres):

        print(
            f"{nombre:<12}",
            end=""
        )

        for x in M[i]:

            print(
                f"{x:3}",
                end=""
            )

        print()
