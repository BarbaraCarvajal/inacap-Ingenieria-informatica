"""
Confeccionar una función que calcule la superficie de un rectángulo y la 
retorne, la función recibe como parámetros los valores de dos de sus lados: 
def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos y 
luego mostrar cuál de los dos tiene una superficie mayor.
"""

def superficie():
    lado1 = float(input("Ingrese el primer lado: "))
    lado2 = float(input("Ingrese el segundo lado: "))
    superficie = lado1*lado2
    print(f"La superficie del rectangulo es: {superficie}")

superficie()