from system_state import construir_estado, imprimir_estado


longitudes={

    "mercury":120,
    "venus":60,
    "earth":0,
    "mars":180,
    "jupiter":240,
    "saturn":300

}



estado = construir_estado(
    longitudes
)


imprimir_estado(
    estado
)
