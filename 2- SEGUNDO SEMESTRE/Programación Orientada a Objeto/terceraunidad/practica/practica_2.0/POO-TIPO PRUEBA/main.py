from menu import Menu
from CONSULTAS.crud import *



while True:
    opc= Menu()   
    if opc==1:
        print("Listar Alumnos")
        Listar()
           
    elif opc==2:
        print("Agregar Alumno")
        Insertar()
      
    elif opc==3:
        print("Modificar Alumnos")
        Actualizar()
    elif opc==4:
        print("Eliminar Alumnos")
        Eliminar()
    elif opc==5:
        print("Buscar Alumnos")
        Buscar()
    elif opc==6:
        print("Salir")
        break
     
            