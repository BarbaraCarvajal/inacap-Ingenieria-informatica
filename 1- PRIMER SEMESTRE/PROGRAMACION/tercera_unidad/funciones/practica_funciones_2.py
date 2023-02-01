#funciones sin retorno de valor

def saludar(nombre):
    print(f"Hola {nombre}")


saludar("Bárbara") #llamamos la función y se ejecuta
#en este caso se agrega el string q agregamos :"barbara".


def tabla_multiplicar(num):
    for x in range(1,11):
        print(f"{num} x {x} = {num*x}")
tabla_multiplicar(3)
print()
tabla_multiplicar(4)

#funciones con retorno de valor.

def multiplicar(num1,num2):
    mult = num1 * num2
    return mult

mult = multiplicar(2,3)#opcion 1
print(mult)#parte de la opcion 1

print(multiplicar(2,3)) #opcion 2


def prueba():
    return "hola",445,[1,2,3]

c,n,l = prueba()
print(c,n,l)    
print(prueba())

#argumentos y parámetros

def resta(num1, num2): #parametros
    return num1 - num2

print(resta(4,3)) # argumentos por posicion
print(resta(num2=3,num1=4)) # argumentos por nombre

#argumentos por valor o por referencia.

#por valor: 

def doblar_valor(numero):
    numero *= 2
    print(numero)

n = 5
doblar_valor(n) 
print(n)

def doblar_valor(numero):
    return numero * 2

n = 5
n = doblar_valor(n) 
print(n)

#por referencia:
#todas las colecciones (listas, diccionarios,conjuntos,etc)
#se pasan por argumento por referencias automáticamente.

def valor_doble(numeros):
    for x,n in enumerate(numeros):
        numeros[x] *= 2

n = [5,10,15,20]
valor_doble(n)
print(n)

