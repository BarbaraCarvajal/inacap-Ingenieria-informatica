
"""
Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es
positivo, negativo o nulo (es decir cero)

"""

num= int(input("Ingrese un numero entero por favor"))

if num >=1 :
    print("El numero ",num, " es positivo!")
elif num <0:
    print("El numero ",num, " es negativo!")
elif num == 0:
    print("El numero ",num, " es neutro!")
else:
    print("Porfavor ingrese un numero valido")


