from phase_space import (
    estado_fase,
    vector_fase,
    imprimir_estado
)


angulos = [
    0,
    45,
    90,
    135,
    180,
    225,
    270,
    315,
    359
]


for a in angulos:

    print()

    print(
        "Ángulo:",
        a
    )

    estado = estado_fase(a)

    imprimir_estado(estado)

    print(
        "Vector:",
        vector_fase(a)
    )
