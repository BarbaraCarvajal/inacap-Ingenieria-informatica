"""Leer 10 números enteros y obtener su cubo y su cuarta, 
solo utilizando multiplicaciones.  
Pista: Uso de acumuladores y operador multiplicación. """

for x in range(1,11):
    num = int(input(f"Ingrese el N° {x}: "))
    cubo = num*num*num
    cuarta = num*num*num*num
    print(f"El cubo de {num} es: {cubo} y su cuarta es: {cuarta}")