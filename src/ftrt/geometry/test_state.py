from resonance_matrix import matriz_resonancia
from state import estado_geometrico, imprimir_estado


longitudes = {

    "mercury":120,
    "venus":60,
    "earth":0,
    "mars":180,
    "jupiter":240,
    "saturn":300

}


nombres,R = matriz_resonancia(longitudes)


estado = estado_geometrico(R)


imprimir_estado(estado)
