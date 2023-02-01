# 6-  Desarrollar un algoritmo que almacene 5 valores enteros
# aleatorios en una lista e imprima: 
# a: el valor mayor
# b: la suma de los números
# c: el promedio de los números


from random import randint as aleatorio
 
import os
#os.system("clear") #mac
os.system("cls") #windows


lista = []
valores = 0
for x in range(1,6):
    valores = aleatorio(1,100)
    lista.append(valores)
    suma = sum(lista)

promedio = suma/len(lista)
print(lista)
print(f"El número mayor es: {max(lista)}")
print(f"La suma de los numeros de la lista: {sum(lista)}")
print(f"El promedio de los numeros de la lista es: {promedio}")
