"""

3. Dadas las siguientes Listas de Tuplas, escriba las funciones para obtener:
- mas_caro(productos) #Retornará el nombre y precio del producto más caro.
- total_ingresos(ventas, productos) #Retornará el total de ingresos por ventas.
#código, nombre, precio, cantidad de unidades del producto. 
# 
productos = [
(30144, 'Pendrive', 7490, 200), 
(65401, 'Audífonos',22500, 110), 
(68900, 'Teclado', 3990, 305), 
(21988, 'Mouse', 8690, 178), 
(34560, 'Monitor', 64990, 15), 
(86899, 'Webcam', 13990, 10), 
(54544, 'Joystick', 41990, 100), ]
#código, cantidades vendidas. ventas = [
(30144, 40), (21988, 25), (34560, 5),
]
"""
import os
os.system("clear")

#- mas_caro(productos) #Retornará el nombre y precio del producto más caro.
def mas_caro(productos):
    precios_productos = []
    for codigo, nombre, precio, stock in productos:
        precios_productos.append(precio)
        carito = max(precios_productos)
        if carito == precio:
            producto = nombre
            cantidad = stock
    print(f"El precio más caro es ${carito} que corresponde a {producto} y tiene {cantidad}")
#total_ingresos(ventas, productos) #Retornará el total de ingresos por ventas.

def total_ingresos(ventas, productos):
    total = 0
    for codigo, nombre, precio, stock in productos:
        for codigo2, stock2 in ventas:
            if codigo2 == codigo:
                venta = precio * stock2
                total += venta
    print(f"Total de ventas ${total}")

#código, nombre, precio, cantidad de unidades del producto. 
productos = [
(30144, 'Pendrive', 7490, 200), 
(65401, 'Audífonos',22500, 110), 
(68900, 'Teclado', 3990, 305), 
(21988, 'Mouse', 8690, 178), 
(34560, 'Monitor', 64990, 15), 
(86899, 'Webcam', 13990, 10), 
(54544, 'Joystick', 41990, 100), 
]

#código, cantidades vendidas. 
ventas = [
(30144, 40), 
(21988, 25), 
(34560, 5),
]
mas_caro(productos)
total_ingresos(ventas, productos)



