import os, time

os.system("cls")

def test():
    print("Este print llama desde la función saludar()")
test()

def mensaje():
    print("hola, primera función")
mensaje()

mensaje()
print("chao")
mensaje()

def listado():
    for i in range(1,11,1):
        print(i,end=" ")
listado()

def listado():
    return "cadena"
print(listado())

#lo que hace el return es "guardar" la función en un print.

def suma_dos_numeros(num1, num2):
    return(num1 + num2)
    #codigo principal
x = int(input("Numero 1: "))
y = int(input("Numero 2: "))
print(suma_dos_numeros(x,y))
print(type(suma_dos_numeros(x,y)))

