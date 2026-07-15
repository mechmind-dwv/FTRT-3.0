"""
FTRT JPL Integration Test
"""

from datetime import date

from ftrt.ephemerides_skyfield import (
    longitudes_sistema
)

from ftrt.geometry.system_state import (
    construir_estado,
    imprimir_estado
)


fecha = date(
    2026,
    7,
    14
)


print("="*72)
print("FECHA")
print("="*72)

print(fecha)


longitudes = longitudes_sistema(
    fecha
)


print()
print("="*72)
print("LONGITUDES HELIOCÉNTRICAS")
print("="*72)


for planeta,angulo in longitudes.items():

    print(
        f"{planeta:<10}: {float(angulo):.6f}"
    )



estado = construir_estado(
    longitudes
)


print()

imprimir_estado(
    estado
)
