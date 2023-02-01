"""
7. Cree un Diccionario que contenga claves y los 
valores como como Tuplas, luego obtenga a través de 
funciones distintas estadísticas (sueldo más bajo, 
edad más alta, promedio de sueldos, etc). 
La función debe recibir los datos como parámetros.
Ejemplo: 
Clave=nombre de empleado, Valores=edad, sueldo.
empleado = {
“Carlos”:(19, 250000),
“Marcela”:(25, 350000), }
"""

empleado = {
    "Carlos" :  (19, 250000),
    "Marcela":  (25, 350000),
    "Gyriam":   (21, 10000000),
    "Cristofer":(26, 100000),
    "Barbara":  (28, 500000),
    "Reinaldo": (22, 650000),
    "Luis":     (23, 550000)
    }

def datos(empleado):
    name = input("Ingrese el nombre a consultar: ").title()
    for nombre in empleado.keys():
        if name == nombre:
            print(f"El empleado {name} esta en la lista")
            acceder_datos = empleado.get(name)
            #print(acceder_datos)
            print(f"{name} tiene {acceder_datos[0]} y gana ${acceder_datos[1]}")

def agregarTrabajador(empleado):
    print("Agregar trabajadores: ")
    continuar=True
    while continuar:
        agregar=input("Ingrese Nombre: ")
        edad=int(input("Edad: "))
        sueldo=int(input("Sueldo: "))

        empleado[agregar]=edad,sueldo

        continuar=input("quieres anadir mas info  s/n") == "s"
    

datos(empleado)
agregarTrabajador(empleado)