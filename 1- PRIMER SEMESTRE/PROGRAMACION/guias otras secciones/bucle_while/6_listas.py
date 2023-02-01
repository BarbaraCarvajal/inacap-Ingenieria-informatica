"""
Realizar un programa que permita cargar dos listas de 15 valores
cada una. 
Informar con un mensaje cual de las dos listas tiene un valor 
acumulado mayor
(mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más 
estructuras repetitivas en un algoritmo.
"""
x = 1
suma1 = 0
while x <=15:
    valor = int(input(f"valor numero: {x} \n"))
    x += 1
    suma1 = suma1 + valor
y = 1
suma2 = 0
while y <=15:
    valor2 = int(input(f"valor numero: {y} \n"))
    y += 1
    suma2 = suma2 + valor2
if suma1 > suma2:
    print(f"La suma mayor es de la primera lista: {suma1}")
elif suma1 == suma2:
    print("Las dos sumas dan lo mismo")
else: 
    print(f"La suma mayor es de la segunda lista: {suma2}")