
"""
Se ingresan tres notas de un alumno, 
si el promedio es mayor o igual a siete
mostrar un mensaje "Promocionado".
"""
suma=0
x=1
nota=0
while x <= 3 :
    nota = int(input("Ingrese la nota"))
    suma = suma + nota
    x = x + 1
promedio = suma/3
print("El promedio de notas es: ",promedio)

if promedio >= 7:
    print("Felicidades haz sido promocionado! con tu: ",promedio)