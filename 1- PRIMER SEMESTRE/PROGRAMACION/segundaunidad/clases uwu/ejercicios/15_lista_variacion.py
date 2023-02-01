"""
Escribir un programa en el cual: dada una lista 
de tres valores numéricos distintos se calcule 
e informe su rango de variación
(debe mostrar el mayor y el menor de ellos) 
"""

print("Porfavor ingresar solo numeros diferentes")
num1 = int(input("Ingrese el primer numero\n"))
num2 = int(input("Ingrese el segundo numero\n"))
num3 = int(input("Ingrese el tercer y ultimo numero\n"))

if num1 != num2 != num3:
    variacion1 = num1 - num2
    variacion2 = num1 - num3
    variacion3 = num2 - num3
    print(f"La variacion entre {num1} y {num2} es: {variacion1}\n La variacion entre {num1} y {num3} es: {variacion2}\n La variacion entre {num2} y {num3} es: {variacion3}\n ")
else:
    print("Porfavor ingresar solo numeros diferentes")

if num1> num2 and num1>num3:
    print(f"El numero mayor es {num1}")
elif num2 > num1 and num2 >num3:
    print(f"El numero mayor es {num2}")
elif num3 > num1 and num3 > num2:
    print(f"El numero mayor es {num3}")
else:
    print("No hay numero mayor porque todos son iguales")