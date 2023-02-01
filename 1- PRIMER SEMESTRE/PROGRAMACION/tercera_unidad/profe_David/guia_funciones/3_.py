"""
Desarrollar una función que reciba un string como parámetro y nos muestre 
la cantidad de vocales. Llamarla desde el bloque principal del programa 3 
veces con string distintos.
"""

def contador_vocales(frase):
    contador = 0
    for x in frase:
        frase = frase.lower()
        if x in "aeiou":
            contador +=1
    print(f"En la frase {frase} hay {contador} vocales")

contador_vocales("barbara")
contador_vocales("Camilo i love u")
contador_vocales("Mokita hermosa")

for x in range(3):
    frase = (input("Ingrese la palabra o frase \n").lower())
    contador_vocales(frase)