from phase_matrix import matriz_fases, imprimir


longitudes={

"mercury":120,
"venus":60,
"earth":0,
"mars":180,
"jupiter":240,
"saturn":300

}


nombres,M,estados = matriz_fases(longitudes)


imprimir(nombres,M)


print()

print(
"Estados:",
estados
)
