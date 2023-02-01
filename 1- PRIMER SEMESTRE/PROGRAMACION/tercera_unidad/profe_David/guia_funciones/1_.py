"""
Desarrollar un programa con dos funciones. 
La primera que solicite el ingreso de un entero y 
muestre el cuadrado de dicho valor. 
La segunda que solicite la carga de dos valores y
muestre el producto de los mismos. LLamar desde el 
bloque del programa principal a ambas funciones.
"""

def cuadrado():
    num = int(input("Número: "))
    print(f"El cuadrado del número {num} es: {num**2}")

def producto():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    print(f"El producto entre los numeros {num1} y {num2} es: {num1*num2}")


cuadrado()
producto()

