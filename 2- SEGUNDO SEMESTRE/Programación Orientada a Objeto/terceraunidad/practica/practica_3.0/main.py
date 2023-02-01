from funciones import *

#menu
def menu():
    while True:
        print("""
    MENU
1) VER ALUMNOS
2) AGREGAR ALUMNO NUEVO O Agregar Asignatura
3) MODIFICAR DATOS
4) CONSULTAR DATOS
5) ELIMINAR ALUMNO
6) ENCRIPTAMIENTO DE CLAVES
7) SALIR
 """)
        opcion = int(input("Ingrese su opcion: "))
        if opcion == 1:
            verDatos()  
        elif opcion == 2:
            agregarDatos()
        elif opcion == 3:
            actualizarDatos()
        elif opcion == 4:
            consultarDatos()
        elif opcion == 5:
            eliminarDatos() 
        elif opcion == 6:
            encriptamiento()
        elif opcion == 7:
            print("adios :D")
            break 
        else:
            print("Ingrese una opción correcta >:C")  
            
menu()