import os
os.system("clear") # cls para windows
#genera un limpiado de pantalla

"""
Desarrollar un programa que solicite la carga de tres valores y muestre el 
menor. Desde el bloque principal del programa llamar 2 veces a dicha 
función (sin utilizar una estructura repetitiva)
"""

def menor ():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    num3 = int(input("Ingrese el tercer numero: "))
    if num1>num2 and num1>num3:
        print(f"El número mayor es el primero: {num1}")
    elif num2>num1 and num2>num3:
        print(f"El número mayor es el segundo: {num2}")
    elif num3>num1 and num3>num2:
        print(f"El número mayor es el tercero: {num3}")
    else:
        print(f"Todos los numeros son iguales: {num1, num2, num3}")


menor()
menor()