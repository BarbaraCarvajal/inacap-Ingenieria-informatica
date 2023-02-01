"""
Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de 
los tres turnos tiene un promedio de edades mayor
"""
print("Ingrese 5 edades de los estudiantes del turno mañana")
suma_edades = 0
for x in range(1,6):
    edad = int(input(f"Edad N° {x} \n"))
    suma_edades = suma_edades + edad
    promedio1 = suma_edades / 5
print(f"Promedio edades turno de mañana: {promedio1}")

print("Ingrese 6 edades de los estudiantes del turno tarde")
suma_edades = 0
for x in range(1,7):
    edad = int(input(f"Edad N° {x} \n"))
    suma_edades = suma_edades + edad
    promedio2 = suma_edades / 6
print(f"Promedio edades turno de tarde: {promedio2}")

print("Ingrese 11 edades de los estudiantes del turno noche")
suma_edades = 0
for x in range(1,12):
    edad = int(input(f"Edad N° {x} \n"))
    suma_edades = suma_edades + edad
    promedio3 = suma_edades / 11
print(f"Promedio edades turno de noche: {promedio3}")

if promedio1 > promedio2 and promedio1 > promedio3:
    print(f"El promedio mayor es el de la mañana con: {promedio1} edad promedio")
elif promedio2 > promedio1 and promedio2 > promedio3:
    print(f"El promedio mayor es el de la tarde con: {promedio2} edad promedio")
elif promedio3 > promedio1 and promedio3 > promedio2:
    print(f"El promedio mayor es el de la noche con: {promedio3} edad promedio")
else:
    print("La edad promedio es la misma en todos los turnos!")



