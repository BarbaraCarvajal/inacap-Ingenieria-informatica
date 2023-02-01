
def puntuacion(clase):
    return sum(clase)/len(clase)
 

primero_medio = [7,9,8,0,4,2]
print(puntuacion(primero_medio))

segundo_medio = [7,9,8,5,6,7,]
print(puntuacion(segundo_medio))

tercero_medio = [7,9,8]
print(puntuacion(tercero_medio))

"""def puntuacion2():
    curso = input("CURSO: ")
    cant_alumnos = int(input("CANTIDAD ALUMNOS: "))
    for x in range(cant_alumnos):
        """

