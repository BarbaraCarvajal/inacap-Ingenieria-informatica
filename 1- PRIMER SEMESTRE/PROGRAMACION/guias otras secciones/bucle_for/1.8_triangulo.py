"""
Confeccionar un programa que lea n pares de datos,
cada par de datos corresponde a la medida de la base y 
la altura de un triángulo. 
El programa deberá informar:
a) De cada triángulo la medida de su base, su altura y
su superficie.
b) La cantidad de triángulos cuya superficie es mayor a 12.
"""
mayor_12 = 0
cantidad = int(input("¿los datos de cuántos triangulos ingresará? \n"))

for x in range (cantidad):
    base = float(input("Ingrese la base del triangulo\n"))
    altura = float(input("Ingrese la altura del triangulo\n"))
    superficie = (base * altura) / 2
    print(f"La base del triangulo {x} es {base} y su altura es {altura}, por ende su superficie es: {superficie}")
    if superficie > 12:
        mayor_12 = mayor_12 + 1
print(f"La cantidad de triangulos con uns superficie superior a 12 son: {mayor_12}")   
