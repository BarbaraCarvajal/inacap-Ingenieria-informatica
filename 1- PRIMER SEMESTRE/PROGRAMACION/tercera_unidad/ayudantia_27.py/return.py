from re import A


def sumar(): #sin parametros y sin retorno
    n1= int(input("Ingrese valor: "))
    n2= int(input("Ingrese segundo valor: "))
    sumar=n1+n2
    print(f"{sumar}")
sumar()

def sumar2(n1,n2): #con parametros y con retorno
    sumar=n1+n2
    print(f"{sumar}")

sumar2(2,2)

def sumar3(n1,n2): #con parametros y con retorno
    sumar=n1+n2
    print(f"{sumar}")
    return sumar

"""doble_suma=sumar3(2,6)*2
print(f"El doble de la suma es: {doble_suma}")
"""

sumar3(1,2)

def multiplicar(num1,num2):
    return num1*num2



resultado = multiplicar(2,3)
print(resultado)