"""
1. Escribir una función de nombre sin_repetidos(lista), 
que, dada la siguiente lista de números enteros 
[1, 2, 2, 1, 4, 6, 2, 3, 4, 4, 1, 3] 
(enviada como parámetro), retorne una lista nueva 
que mantenga el orden de la lista original 
pero no tenga repetidos."""


lista = [1, 2, 2, 1, 4, 6, 2, 3, 4, 4, 1, 3] 

def sin_repetidos(lista):
    lista2= []
    for x in lista:
        if x not in lista2:
            lista2.append(x)
    print(f"Lista original {lista}")
    print(f"Lista nueva: {lista2}")

#sin_repetidos(lista)
def sin_repetidos2(lista):
    lista = list(set(lista))
    print(lista)

sin_repetidos2(lista)


print(dir(print()))










"""import os
os.system("clear")

lista = [1, 2, 2, 1, 4, 6, 2, 3, 4, 4, 1, 3] 
listaNueva = []

for x in lista:
    if not x in listaNueva:
        listaNueva.append(x)
print(lista)
print(listaNueva) 

# otra forma:
print()
lista = [1, 2, 2, 1, 4, 6, 2, 3, 4, 4, 1, 3] 
print(lista)
lista = list(set(lista))
print(lista)
"""






