"""
confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. La 
carga de los valores hacerlo por teclado.
"""

def num_mayor():
    num1 = int(input("Primer nuemero: "))
    num2 = int(input("Segundo nuemero: "))
    num3 = int(input("Tercer nuemero: "))

    if num1> num2 and num1 > num3:
        print(f"El numero mayor es el primero: {num1}")
    elif num2> num1 and num2 > num3:
        print(f"El numero mayor es el segundo: {num2}")
    elif num3> num1 and num3 > num2:
        print(f"El numero mayor es el tercero: {num3}")
    else:
        print(f"Todos los numeros son iguales: {num1}-{num2}-{num3}")

num_mayor()
        