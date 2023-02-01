"""
Se cargan por teclado tres números distintos. 
Mostrar por pantalla el mayor de ellos.
"""

"""x = 1
while x <= 3:
    num = int(input("Ingrese un numero"))
    
print("El numero mayor es: ") """

num1 = int(input("Ingrese el primer numero"))
num2 = int(input("Ingrese el segundo numero"))
num3 = int(input("Ingrese el tercer numero"))

if num1 > num2 and num1 > num3:
    print("El numero mayor es: ",num1)
elif num2 > num1 and num2 > num3:
    print("El numero mayor es: ",num2)
elif num3 > num1 and num3 > num2:
    print("El numero mayor es: ",num3)
else:
    print("Porfis ingrese un numero valido")