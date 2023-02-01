"""
Desarrollar un programa que pueda calcular el valor 
del tipo de cambio de tu monedahacia el dólar y viceversa.
"""

def cambio_pesos_a_dolares(pesos):
    return pesos/823

def cambio_dolares_a_pesos(dolares):
    return dolares*823

sw= True
while sw == True:
    print("""
             ...MENU...
1: convertir de pesos chilenos a dolares
2: convertir de dolares a pesos chilenos
3: Salir """)

    opcion = int(input("Digite una opcion \n"))
    print()
    if opcion == 1:
        pesos = float(input("Cantidad de pesos chilenos\n"))
        print(f"Dólares -> ${cambio_pesos_a_dolares(pesos):.2f}")
    elif opcion == 2:
        dolares = float(input("Cantidad de dolares\n"))
        print(f"Pesos chilenos -> ${cambio_dolares_a_pesos(dolares):.2f}")
    elif opcion == 3:
        print("Hasta luego <3")
        sw = False
    else:
        print("Opcion incorrecta")