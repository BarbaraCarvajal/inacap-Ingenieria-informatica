"""import os, msvcrt
os.system("cls")

import msvcrt
msvcrt.getch()
"""

def suma(num: int):
    
    suma_numeros = 0
    num = str(num)
    for x in num:
        
        suma_numeros = suma_numeros + x
        num = int((num))
    return print(suma_numeros)


num = int(input("Ingrese un numero: "))
suma(num) 

