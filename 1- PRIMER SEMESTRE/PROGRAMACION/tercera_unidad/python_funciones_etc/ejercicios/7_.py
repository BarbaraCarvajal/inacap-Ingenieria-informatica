"""Escribir un programa que genere frases de forma aleatoria,
 para el mismo se introducirán 3 sujetos, 3 verbos y 
3 predicados. El algoritmo generará tres frases al azar 
con cualquier sujeto, verbo y predicado."""


def mensaje():
    import random
    sujetos = " "
    verbos = " "
    predicados = " "
    for x in range(1,4):
        sujetos[" "] = input(f"{x} Ingrese un sujeto: ")
    for i in range(1,4):
        verbos[" "] = input(f"{x} Ingrese un verbo: ")
    for b in range(1,4):
        predicados[" "] = input(f"{x} Ingrese un predicado: ")

print(random.choice(sujetos))

mensaje()



"""import random

print(random.uniform(10,60))

# El método choice() devuelve un elemento seleccionado
# aleatoriamente de la secuencia especificada.

import random
x = "12345 saludo" # tiene q ser un string
print(random.choice(x))
"""