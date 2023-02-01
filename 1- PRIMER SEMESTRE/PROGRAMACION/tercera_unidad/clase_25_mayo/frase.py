#funcion que reciba una frase por teclado
#y retorne la ultima letra de la frase ingresada

def ultima_letra(palabra):
    return palabra[len(palabra)-1] #palabra[2]...0,1,2,3,4...
palabra = str(input("Ingrese una palabra: "))
print(f"La última letra es: {ultima_letra(palabra)}")