"""
Solicitar al usuario que 
ingrese una frase y luego 
imprimir un listado de las 
vocales que aparecen 
en esa frase (sin repetirlas).
"""

frase = input("Ingrese una frase :D \n")

for x in frase:
    if x in frase == "a":
        print(x)