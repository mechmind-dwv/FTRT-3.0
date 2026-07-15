from phase_matrix import matriz_fases
from phase_metrics import metricas_fase, imprimir_metricas



longitudes={

"mercury":120,
"venus":60,
"earth":0,
"mars":180,
"jupiter":240,
"saturn":300

}



nombres,M,estados = matriz_fases(longitudes)


datos = metricas_fase(M)


imprimir_metricas(datos)
