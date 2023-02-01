
"""
Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando si el número tiene uno o dos dígitos.
(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)
"""


num = int(input("Ingrese un numero de 1 o 2 digitos"))

if num >=1 and num <=9:
    print("El numero ingresado ", num, " contiene 1 digito")
elif num >=10 and num <=99:
    print("El numero ingresado ", num, " contiene 2 digitos")
else: 
    print("Por favor ingrese un numero entre los rangos indicados")
