"""
Se ingresan un conjunto de alturas de personas por teclado.
Mostrarla altura promedio de las personas.
"""


acumulador = 0
x = 1
cantidad = int(input("¿Cuántas alturas ingresará?\n"))
while x <= cantidad:
    altura = float(input(f"Ingrese la {x} altura\n"))
    x = x+1
    acumulador = acumulador + altura

promedio = acumulador / cantidad
print(f"La altura promedio de {cantidad} personas es: {promedio}")
