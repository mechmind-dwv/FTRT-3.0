from planets import get_planet_positions
from resonance import matriz_angulos, imprimir

pos = get_planet_positions()

nombres, M = matriz_angulos(pos)

imprimir(nombres, M)
