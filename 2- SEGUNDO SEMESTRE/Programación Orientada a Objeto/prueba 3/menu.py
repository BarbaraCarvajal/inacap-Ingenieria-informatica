from CrudA import *
from CrudASIG import *
from CrudC import *

from time import sleep

def menu():
    while True:
     print("""
    MENU 
   

   1 MOSTRAR TODOS LOS ALUMNOS
   2 CONSULTAR POR UN ALUMNO
   3 MOSTRAR TODAS LAS ASIGNATURA
   4 CONSULTAR POR UNA ASIGNATURA
   5 AGREGAR ALUMNO
   6 BORRAR ALUMNO
   7 MOSTRAR ALUMNOS
   8 SALIR

     """)

     eleccion=input("ingrese su opcion: ")

     if(eleccion=="1"):
       MostrarA()
       sleep (3)
     elif(eleccion=="2"):
        consultarA()
        sleep (3)
     elif(eleccion=="3"):
        MostrarASIG()
        sleep (3)
     elif(eleccion=="4"):
        consultarASIG()
        sleep (2)
     elif(eleccion=="5"):
       agregarA
       sleep (3)
     elif(eleccion=="6"):
        borrarA()
        sleep (3)
     elif(eleccion=="7"):
       MostrarA()
       sleep (3)
     elif(eleccion=="8"):
       print(" HASTA LUEGO")
       sleep (3)
       break
     else:
        print("Ingrese una eleccion correcta ")

menu()


#5 MOSTRAR UN CURSO
#6 AGREGAR ALUMNO A CURSO
#7 ELIMINAR ALUMNO DE CURSO