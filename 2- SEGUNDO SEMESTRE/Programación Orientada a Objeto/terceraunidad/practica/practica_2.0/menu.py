
from funciones import *

#menu

def menu():
    while True:
        print("""
    MENU
    1) ver alumnos
    2) agregar alumno nuevo
    3) modificar datos de alumno
    4) consultar datos de alumno
    5) eliminar alumno
    6) salir
    """)
        opcion = int(input("Ingrese su opcion: "))
        if opcion == 1:
            verDatos()
        elif opcion == 2:
            agregarDatos()
        elif opcion == 3:
            modicarDatos()
        elif opcion == 4:
            consultarDatos()
        elif opcion == 5: 
            eliminarDatos()
        elif opcion == 6:
            print("Adios :D")
            break
        else:
            print("Ingrese una opcion dentro de las dadas! estupido >:C")
            
menu()


