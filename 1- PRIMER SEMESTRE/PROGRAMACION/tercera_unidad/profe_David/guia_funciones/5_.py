"""
Elaborar una función que reciba tres enteros y 
nos retorne el valor promedio de los mismos.
"""

def promedio():
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    num3 = int(input("Numero 3: "))
    promedio = (num1+num2+num3)/3
    print(promedio)

promedio()