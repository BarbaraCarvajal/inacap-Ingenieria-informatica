"""
Al ingresar dos números imprima el 
mayor de ellos o IGUALES si son iguales.
"""
num1 = int(input("Ingrese el primer numero\n"))
num2 = int(input("Ingrese el segundo numero\n"))

if num1 == num2:
    print("{} y {} son iguales!".format(num1,num2))
elif num1 > num2:
    print("El numero {} es el mayor".format(num1))
else:
    print("El numero {} es el mayor".format(num2))