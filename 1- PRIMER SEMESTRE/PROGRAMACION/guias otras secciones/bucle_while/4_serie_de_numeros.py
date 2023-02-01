"""Realizar un programa que imprima 25
términos de la serie 11-22-33-44, etc. 
(No se ingresan valores por teclado)"""

x=1
num =0
while x <= 25:
    num = num + 11
    print(f"N° {x}:   {num}")
    x = x +1