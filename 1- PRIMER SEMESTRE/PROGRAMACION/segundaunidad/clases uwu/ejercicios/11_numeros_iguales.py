"""
Se ingresan tres valores por teclado, 
si todos son iguales se imprime la suma 
del primero con 
el segundo y a este resultado 
se lo multiplica por el tercero. """


num1 = int(input("Ingrese el primer numero\n"))
num2 = int(input("Ingrese el segundo numero\n"))
num3 = int(input("Ingrese el tercer y ultimo numero\n"))

if num1 == num2 ==num3:
    print(f"la suma de  {num1} con {num2} es: {num1+num2} y su division con {num3} es {(num1+num2)/num3}")