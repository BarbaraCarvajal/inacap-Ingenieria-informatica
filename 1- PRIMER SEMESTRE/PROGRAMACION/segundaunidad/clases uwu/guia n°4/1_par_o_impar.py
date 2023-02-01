"""
Al leer un número entero positivo 
(asuma que el número cumple las condiciones),
imprima PAR si el número es par
e IMPAR si es impar.
"""

num = (int(input("Ingrese un numero entero positivo\n")))

if num >=1:
    if num % 2 ==0:
        print("El numero es par")
    else:
        print("El numero es impar!!")
else:
    print("Porfavor ingrese un numero entero positivo!")
