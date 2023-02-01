"""Se ingresan por teclado tres números, 
si todos los valores ingresados son menores a 10, 
imprimir en pantalla la leyenda 
"Todos los números son menores a diez"."""
""" x= 0
while x <= 3:
    num = int(input("ingrese un numero"))
if num
 """

num1 = int(input("Ingrese el primer numero\n"))
num2 = int(input("Ingrese el segundo numero\n"))
num3 = int(input("Ingrese el tercer y ultimo numero\n"))

if num1 < 10 and num2 < 10 and num3 < 10:
    print("Todos los números son menores a diez")
else:
    print("No todos los numeros son menores a 10 :c ")
