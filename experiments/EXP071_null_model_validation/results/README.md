# EXP071 - Null Model Validation

## Resultado

El primer modelo nulo basado exclusivamente en eventos con FTRT no es discriminante.

## Diagnóstico

El experimento utilizaba únicamente los 8 eventos que ya tenían valor FTRT.

Todos los valores seleccionados superaban el umbral definido:

FTRT > 1.5

Por tanto, cualquier permutación interna mantenía:

- eventos analizados: 8
- éxitos: 8

Resultado:

null_std = 0

El modelo nulo no tenía capacidad estadística.

## Conclusión

Se requiere un modelo nulo temporal utilizando:

- serie completa FTRT diaria (2373 días)
- catálogo completo de eventos (71 eventos)
- selección aleatoria temporal Monte Carlo

Este enfoque permitirá evaluar si la concentración de eventos en valores FTRT elevados supera lo esperado por azar.
