"""
Escribir un programa que permita al 
usuario ingresar 6 números enteros,
que pueden ser positivos o negativos. 
Al finalizar, mostrar la sumatoria de 
los números negativos y el promedio 
de los positivos.
No olvides que no es 
posible dividir por cero, por lo que es necesario 
evitar que el programa arroje un error si no se ingresaron números positivos.
"""

print("Ingrese 6 números :D")

suma_negativos = 0
suma_positivos = 0
positivos = 0
promedio = 0
for x in range(1,7):
    num = int(input(f"numero: {x}: \n"))
    if num < 0: 
        suma_negativos = suma_negativos + num
    if num > 0:
        positivos += 1
        suma_positivos += num
        promedio = suma_positivos/positivos
print(f"La suma de los numeros negativos es: {suma_negativos}, y el promedio de los positivos es: {promedio}")
