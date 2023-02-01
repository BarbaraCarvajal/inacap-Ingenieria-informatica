import os
os.system("clear")

nombres=[]
edades= []
for x in range(3):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
    edad = int(input(("ingrese la edad: ")))
    edades.append(edad)

print(f"Lista nombres {nombres}")
print(f"Lista edades {edades}")


def mostrarDatos():
    for x in range(len(nombres)):
        print(f"{nombres[x]} tiene {edades[x]}")

def eliminarDatos():
    delete = input("¿que dato desea eliminar? ")

def actualizarDatos():
    dato = input(("¿Que dato desea actualizar?: Nombre = 1 - Edad = 2"))
    if dato == 1:
        nombreNuevo = input("Ingrese el nombre nuevo: ")
        nombres.remove(nom)


mostrarDatos()