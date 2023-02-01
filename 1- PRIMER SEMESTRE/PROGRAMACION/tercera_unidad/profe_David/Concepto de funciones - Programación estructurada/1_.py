"""
Problema 1: 
Confeccionar una aplicación que muestre una presentación en pantalla del programa. 
Solicite la carga de dos valores y nos muestre la suma. Mostrar finalmente un mensaje 
de despedida del programa. 
Implementar estas actividades en tres funciones
"""

import math

def presentación():
    print("Bienvenidos")

def suma():
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    total = (num1+num2)
    return print(f"El total de la suma es: {total}")

def despedida():
    print("Hasta luego")

presentación()
suma()
despedida()

