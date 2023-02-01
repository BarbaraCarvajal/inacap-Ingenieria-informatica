"""
Desarrollar un programa que permita cargar n números 
enteros y luego nos informe cuántos valores fueron pares 
y cuántos impares.
Emplear el operador “%” en la condición de
la estructura condicional (este operador retorna el resto de 
la división de dos valores, por ejemplo 11%2 retorna un 1):
if valor%2==0:
"""

cantidad = int(input("¿Cuántos números desea cargar?\n"))
x=1
par = 0
impar = 0
while x <= cantidad:
    
    num = int(input(f"N° {x} \n"))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    x += 1
print("Totales:")
print(f"Numeros Pares: {par}")
print(f"Numeros Impares: {impar}")
