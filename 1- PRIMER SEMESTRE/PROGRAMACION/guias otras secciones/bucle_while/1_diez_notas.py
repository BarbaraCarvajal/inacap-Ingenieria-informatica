"""
Escribir un 
programa que solicite ingresar
10 notas de alumnos y nos informe 
cuántos tienen notas mayores o iguales
a 7 y cuántos menores.
"""

sobre7 = 0
contador=1

while contador <= 10:
    nota = int(input(f"Ingrese la nota del alumno N°{contador}\n"))
    contador+=1
    if nota >= 7:
        sobre7 = sobre7 + 1
print("La cantidad de alumnos que tienen notas igual o sobre 7 son: ",sobre7)