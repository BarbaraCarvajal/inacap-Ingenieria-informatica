import os
os.system("clear")
#genera un limpiado de pantalla

"""import msvcrt
msvcrt.getch()
#lee una pulsación de una tecla
"""
"""
Confeccionar una función que reciba tres enteros y los muestre ordenados 
de menor a mayor. En otra función solicitar la carga de 3 enteros por teclado 
y proceder a llamar a la primer función definida
"""


def ordenados ():
    num1 = int((input("Primer número: ")))
    num2 = int((input("Segundo número: ")))
    num3 = int((input("Tercer número: ")))

    if num1 > num2 and num1 > num3:
        print(num1)
    elif num2 > num1 and num2 > num3:
        print(num2)
    else:
        print(num3)

ordenados()