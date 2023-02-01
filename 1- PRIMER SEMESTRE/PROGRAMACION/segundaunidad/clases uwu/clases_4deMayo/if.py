#ingrese un numero entero, si es positivo y ademas es par envie un mensaje que diga
# aceptado o rechazado

num = int(input("Ingrese un número \n"))

if num > 0 and num%2==0:
    print("Aceptado")
else:
    print("Rechazado")

