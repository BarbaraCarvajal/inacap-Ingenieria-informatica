import os
os.system("clear")

productos = [
    (41419, "fideo",         450,     110),
    (70717, "cuaderno",      900,     119),
    (78714, "Jabon",         730,     708),
    (30877, "Desodorante",   2190,    279),
    (50809, "Lápiz",         500,     155),
    (75466, "Galleta",       235,     100),
]
suma = 0
for cod, producto, precio, stock in productos:
        suma = suma + int(stock)
print(f"La suma de stock es: {suma}")

for x in productos:
    print(x)

print()

productos.append((707001,"lechuga",450,9))#agregamos un nuevo producto

for x in productos:
    print(x)
suma = 0
for cod, producto, precio, stock in productos:
        suma = suma + int(precio) * stock
print(f"Ganancia total es: ${suma}")
precio = list(precio)
print(f"El producto más caro es: {min(precio)}")