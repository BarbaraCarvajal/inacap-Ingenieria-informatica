""""
Plantear una función que reciba un string en mayúsculas o minúsculas y 
retorne la cantidad de letras 'a' o 'A'. 
"""

def a_A():
    frase = input(("Ingrese su frase, palabra, etc: ").lower())
    contador = 0
    for letra in frase:
        if letra == "a":
            contador += 1
    print(f"En la frase: ({frase}) hay {contador} veces la letra A")
a_A()
