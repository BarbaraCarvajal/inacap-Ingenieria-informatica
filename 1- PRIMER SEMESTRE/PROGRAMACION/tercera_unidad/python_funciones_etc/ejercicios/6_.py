"""Crear un programa que cuente el número de vocales de
 una palabra o frase ingresada por teclado. """

def contador_vocales():
    contador = 0
    frase=input("Ingrese su frase o palabra: ")
    for letra in frase:
        if letra.lower() in "aeiou":
            contador += 1
    print(f"En el siguiente texto: {frase}, hay {contador} vocales")
    
contador_vocales()