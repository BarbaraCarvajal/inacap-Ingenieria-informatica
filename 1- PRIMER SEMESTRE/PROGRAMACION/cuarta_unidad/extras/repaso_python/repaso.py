import os
os.system("clear")

numeros = list("12345")
print(numeros)
primera_posicion = numeros[0]
print(primera_posicion)
longitud = len(numeros)
print(longitud)

"""for x in numeros:
    print(x)"""

#indexado y sublistas

lista = ["mokita", "barbara", "camilo", "laikita"]
print(lista)
ultima_posicion = lista[-1]
print(ultima_posicion)

sublista = lista[1:3]
print(sublista)

sublista = lista[:4]
print(sublista)
sublista= lista[2:]
print(sublista)

sublista = lista[-3:-1]

# comprobar si una lista contiene o no un elemento

lista = ["mokita", "barbara", "camilo", "laikita"]
palabra  = "mokita"
palabra2 = "sushi"
if palabra in lista:
    print(f"La palabra {palabra} esta en la lista")
if palabra2 not in lista:
    print(f"La palabra {palabra2} no esta en la lista")
    
# modificar elementos de una lista

lenguajes = ["c","python","kotlin","java","swift"]
lenguajes[1] = "angular"
print(lenguajes)
lenguajes[0] = lenguajes[0]+ "++"
print(lenguajes)

lenguajes[2:4] = ["anaconda","typescript"] 
print(lenguajes)

lenguajes[1:2] = ["Hola", "como","estas"]
print(lenguajes)


# métodos (funciones ya listas en python)

lenguajes = ["c","python","kotlin","java","swift"]


