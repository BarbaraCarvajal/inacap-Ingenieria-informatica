"""
5. Escriba la función vocales(frase), que retorne un 
diccionario con las vocales y la cantidad de veces 
que aparecen en una frase. La frase debe ser ingresada 
por teclado.
Nota: Debe considerar las apariciones en mayúsculas 
como en minúsculas, NO con considerar vocales con tilde 
y si la vocal no aparece debe estar de igual manera en 
el diccionario con valor.

"""
import os
os.system("clear")

frase = input("Ingresa una frase: ")
def letras(frase):
    letras = {}
    for x in frase:
        if x not in letras:
            letras[x] = 1
        elif x == " ":
            del letras[x]
        else:
            letras[x] += 1
    print(letras)
    
letras(frase)
def vocales(frase):
    print(frase)
    vocales = {"a":0, "e":0, "i":0, "o":0, "u":0 }
    for x in frase:
        if x in vocales:
            vocales[x] += 1
    print(vocales)

vocales(frase)




















"""

frase = input("Ingrese una frase:   ")
def vocales(frase):
    diccionario = {"a":0,"e":0,"i":0,"o":0,"u":0}
    for x in frase:
        if x in diccionario.keys():
            diccionario[x] =  diccionario[x] +1
    print(diccionario)

vocales(frase)"""