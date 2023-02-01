
""" 
gatitos = {
    "nombre" : "mokita"
    " edad : 3",
}
print(gatitos)

"""

totalSuma = 0
cantidadAlumnos = 0
promedioEdad = 0
for i in range(5):
    nombre = input("ingrese nombre")
    edad = int(input("ingrese una edad"))
    
    totalSuma = totalSuma + edad
    cantidadAlumnos = cantidadAlumnos + 1
    promedioEdad = cantidadAlumnos/5

print(f"Total de alumnos: "{cantidadAlumnos} " Edades sumadas: "{totalSuma} " Y el promedio de edad es: "{promedioEdad})
