"""
Confeccionar un programa que permita cargar un número entero positivo de hasta tres
cifras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error
si el número de cifras es mayor.

"""


num = int(input("Ingrese un numero de hasta 3 cifras porfavor\n"))

if num >= 1 and num <=9:
    print("El numero: ",num," contiene 1 cifra")
elif num >= 1 and num <=99:
    print("El numero: ",num," contiene 2 cifras")
elif num >= 100 and num <=999:
    print("El numero: ",num," contiene 3 cifras")
elif num >999:
    print("Error! El numero ",num," contiene mas de 3 cifras")    
else:
    print("Porfavor ingresar un numero dentro de los rasgos pedidos")