"""
Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares.
"""

positivos = 0
negativos = 0
multiplos_de_15 = 0
suma_pares = 0
print("Ingrese 10 valores")
for x in range(1,11):
    num = int(input())
    if num > 0 : positivos += 1
    elif num < 0 : negativos += 1
    if num % 15 == 0: multiplos_de_15 += 1
    if num %2 == 0 :suma_pares = suma_pares + num
print(f"Numeros positivos totales: {positivos}")
print(f"Numeros negativos totales: {negativos}")
print(f"Multiplos de 15: {multiplos_de_15}")
print(f"La suma de los numeros ingresados pares es: {suma_pares}")
