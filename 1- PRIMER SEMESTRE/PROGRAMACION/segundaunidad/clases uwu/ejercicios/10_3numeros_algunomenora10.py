"""Se ingresan por teclado tres números, 
si al menos uno de los valores ingresados es menor a 
10, imprimir en pantalla la leyenda 
"Alguno de los números es menor a diez"."""

num1 = int(input("Ingrese el primer numero\n"))
num2 = int(input("Ingrese el segundo numero\n"))
num3 = int(input("Ingrese el tercer y ultimo numero\n"))

if num1 < 10 or num2 < 10 or num3 < 10:
    print("Al menos 1 numero es menor a 10")
else:
    print("No hay numeros ingresados que sean menores a 10 :c ")
