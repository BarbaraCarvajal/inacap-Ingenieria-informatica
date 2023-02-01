# Dado una lista de 100 elementos numéricos enteros (1 al 100),
# generar el código que muestre todos los números de la lista 
# y la suma de ella
import os
#os.system("clear") #mac
os.system("cls") #windows


numeros = []
for x in range(1,101): 
    numeros.append(x)
print(numeros)

suma = 0
for x in numeros:
    suma = suma + x
print(f"La suma de los números ingresados es: {suma}")
print(f"La suma de los números ingresados es: {sum(numeros)}")


