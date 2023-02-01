"""
Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al segundo informar su suma y diferencia, en caso contrario informar el producto y 
la división del primero respecto al segundo.
"""

num1= int(input("ingrese el primer numero porfavor"))
num2= int(input("ingrese el segundo numero porfavor"))

if num1 > num2:
    suma = num1 + num2 
    resta = num1 - num2
    print("La suma de: ",num1," y ",num2, "es: ",suma)
    print("La diferencia de: ",num1," y ",num2, "es: ",resta)
else:
    producto = num1 * num2
    division = num2 / num1
    print("El producto entre ",num1," y ",num2, "es: ",producto)
    print("La division de: ",num1," y ",num2, "es: ",division)


