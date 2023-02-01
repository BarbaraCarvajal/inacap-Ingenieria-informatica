"""
Escribir un programa que muestre 
la sumatoria de todos los múltiplos 
de 3 encontrados entre el 0 y el 100.
"""
multiplo_de_3 = 0
suma_multiplos =0
for x in range(0,100):
    if x % 3 == 0:
        multiplo_de_3 += 1
        suma_multiplos +=  x
print(f"La suma de los {multiplo_de_3} multiplos de 3 desde el 0 al 100 es: {suma_multiplos}")