# Realiza una función llamada area_circulo(radio)
# que devuelva el área bla bla 

from math import pi, pow

def area_circulo(radio):
    return pow(radio,2)*pi
radio = float(input("Ingrese el radio del circulo: "))
print("El area del circulo es: ",round(area_circulo(radio),3))