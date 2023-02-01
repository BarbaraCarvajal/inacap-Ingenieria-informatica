"""
La siguiente tabla muestra los niveles 
que obtienen por su puntuación los clientes 
de una empresa. Pueden convertir los puntos en dinero, 
que en cada nivel es de $10.000
multiplicado por la puntuación del nivel.
Nivel Puntuación
Gold 1a5 
Preferente 6 a 14
VIP 15 o más
De acuerdo con lo anterior, 
cree un programa que lea la puntuación del usuario 
y muestre por pantalla su nivel de calificación, así como 
la cantidad de dinero que recibirá para sus compras.
"""

puntuacion = int(input("Ingrese su puntuación\n"))

if puntuacion >=1 and puntuacion <=5:
    puntos = puntuacion * 10000
    print(f"Su calificacion es de cliente GOLD\nSu puntuación es de {puntuacion} así que obtiene ${puntos}")
elif puntuacion >=6 and puntuacion <=14:
    puntos = puntuacion * 10000
    print(f"Su calificacion es de cliente PREFERENTE\nSu puntuación es de {puntuacion} así que obtiene ${puntos}")
elif puntuacion >=15:
    puntos = puntuacion * 10000
    print(f"Su calificacion es de cliente VIP\nSu puntuación es de {puntuacion} así que obtiene ${puntos}")
else:
    print("No tienes suficientes puntos")