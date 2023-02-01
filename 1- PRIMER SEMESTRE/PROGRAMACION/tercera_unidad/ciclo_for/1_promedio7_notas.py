"""Calcular  el  promedio  de  un  alumno  que  tiene  
7  calificaciones  en  la  materia  de  Diseño 
Estructurado de Algoritmos.  
Pista: Uso de acumulador."""

suma = 0
print("Diseño Estructurado de Algoritmos")
for x in range(1,8):
    nota = int(input(f"Ingrese la nota N° {x}: "))
    suma = suma + nota
    promedio = suma / 7
print(f"El promedio final de las 7 notas es: {promedio:.2f}")
