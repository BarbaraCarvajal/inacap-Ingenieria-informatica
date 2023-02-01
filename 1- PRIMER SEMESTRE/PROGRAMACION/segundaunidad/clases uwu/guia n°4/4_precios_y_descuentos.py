"""
Crear un programa que imprima el nombre de un artículo,
clave, precio original y su precio con descuento. 
El descuento lo hace en base a la clave, si la clave 
es 1 el descuento es del 10% y si la clave es 2 el 
descuento es de 20% (solo existen dos claves).
"""

producto = input("Ingrese el articulo\n")
precio_original = int(input("Ingrese el precio\n"))
descuento = int(input("Ingrese el codigo de descuento\n"))

if descuento == 1:
    final = precio_original -(precio_original * 0.10)
    print(f"El precio final de {producto} es: ${int(final)}, precio original {precio_original}, descuento realizado: {int(precio_original-final)}")
elif descuento ==2:
    final = precio_original -(precio_original * 0.20)
    print(f"El precio final de {producto} es: ${int(final)}, precio original {precio_original}, descuento realizado: {int(precio_original-final)}")