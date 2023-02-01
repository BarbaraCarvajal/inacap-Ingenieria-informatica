import os
os.system("clear")

"""1. Escriba la función contar_letras(oracion) que retorne un diccionario asociando a
cada letra la cantidad de veces que aparece en la oración:
contar_letras('El elefante avanza hacia Asia’)
{'a': 8, 'c': 1, 'e': 4, 'f': 1, 'h': 1, 'i': 2, 'l': 2, 'n': 2, 's': 1, 't': 1, 'v': 1, 'z': 1}
Cada valor del diccionario debe considerar tanto las apariciones en mayúscula como en minúscula de 
la letra correspondiente. Los espacios deben ser eliminados.
"""

def contar_letras(oracion):
    diccionario = {}
    for x in oracion.lower():
        if x in diccionario:
            diccionario[x] = diccionario[x]+1
        else:
            diccionario[x]  =1
        if x == " ":
            del diccionario[x]
    diccionario = dict(sorted(diccionario.items())) #hay que ponerlo en diccionario, porq si no, lo pone como tupla
    return print(diccionario)


#oracion = input("Ingrese un oración: ")
#contar_letras(oracion)

"""2. Escriba una función promedio(num) que entregue el promedio 
de los valores de todas las claves:
n = {2:2, 8:7, 4:2, 6:4}
El promedio de las claves es: 5.0"""

def promedio_claves(num):
    promedio = sum(n.keys())/len(n)
    return print(f"El promedio es: {promedio}")

def promedio_valores(num):
    promedio = sum(n.values())/len(n)
    return print(f"El promedio es: {promedio}")

n = {
    2:2,
    8:7,
    4:2,
    6:4,
    9:9
}

promedio_claves(n)
promedio_valores(n)


"""3. Escriba una función maximo_par(j) que entregue el valor 
máximo de la suma de una clave y su valor en el diccionario j:
j = {5:1, 4:7, 9:0, 2:2} Resultado: 11"""

def maximo_par(num):

    lista = []
    for x,y in j.items():
        suma = x + y
        lista.append(suma)
    print(f"Lista: {lista}")
    print(f"El numero más grande de la suma de clave:valor es: {(max(lista))}")

j = {
    5:1,
    4:7,
    9:0,
    2:2
}
maximo_par(j)

def otra_opcion(j):
    diccionario = {}
    for x,y in j.items():
        suma = x + y
        diccionario[x,y] = suma
    diccionario = (sorted(diccionario.values()))
    print(f"El numero más grande de la suma de clave:valor es: {diccionario[-1]}")

otra_opcion(j)

#bonustrack

def contar_vocales(frase):
    diccionario = dict(a=0, e=0, i=0, o=0, u=0)
    for x in frase.lower():
        if x in diccionario:
            diccionario[x] = diccionario[x]+1
    return print(diccionario)

#frase = input("Ingrese una frase: ").lower()
#contar_vocales(frase)

#bonustrack 2

def bonustrack(j):
    valores = sorted(j.values())
    print(valores)
    diccionario = {}

    for x in valores:
        for i in j.keys():
            if j[i] == x:
                diccionario[i] = j[i]
    return diccionario


diccionario1= {
    1:"j",
    2:"a",
    3:"b"
}
print(bonustrack(diccionario1))