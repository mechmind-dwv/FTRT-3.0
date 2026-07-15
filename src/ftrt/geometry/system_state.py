"""
FTRT Scientific Laboratory

Estado completo geométrico del Sistema Solar.

Integra:

- Resonancia angular
- Estado espectral
- Fases planetarias
- Métricas colectivas
"""

from .resonance_matrix import matriz_resonancia
from .state import estado_geometrico

from .phase_matrix import matriz_fases
from .phase_metrics import metricas_fase



def construir_estado(longitudes):

    """
    Genera un snapshot geométrico.

    Parámetro:

    longitudes = {
        planeta: grados heliocéntricos
    }

    """

    nombres, R = matriz_resonancia(
        longitudes
    )


    geometria = estado_geometrico(
        R
    )


    nombres_fase, M, estados = matriz_fases(
        longitudes
    )


    fases = metricas_fase(
        M
    )


    estado = {

        "planetas":
            nombres,


        "lambda_max":
            geometria["lambda_max"],


        "lambda_min":
            geometria["lambda_min"],


        "energia_resonancia":
            geometria["energia"],


        "rango":
            geometria["rango"],


        "entropia_espectral":
            geometria["entropia"],


        "coherencia_espectral":
            geometria["coherencia"],


        "estados_fase":
            fases["estados_activos"],


        "entropia_fase":
            fases["entropia_fase"],


        "concentracion_fase":
            fases["concentracion"],


        "firma_fase":
            estados

    }


    return estado



def imprimir_estado(estado):

    print("="*72)
    print("FTRT SYSTEM GEOMETRIC STATE")
    print("="*72)


    for k,v in estado.items():

        print(
            f"{k:<25}: {v}"
        )
