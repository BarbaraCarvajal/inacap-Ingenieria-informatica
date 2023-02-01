import hashlib
from BD.Conexion import DAO

def menuPrincipal():
    continuar = True
    while (continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("\n==== Menu Principal ====\n")
            print("1. Mostrar datos")
            print("2. Ingresar datos")
            print("3. Consultar datos")
            print("4. Eliminar datos")
            print("5. Actualizar datos")
            print("6. Salir")
            opcion = int(input("\nIngrese una opción: "))
            if opcion <1 or opcion>6:
                print("\nOpción incorrecta. Ingrese nuevamente.")
            elif opcion == 6:
                continuar = False
                print("\nGracias por usar nuestro sistema.")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    dao = DAO()
    if opcion == 1:
        autos = dao.mostrarDatos()
        if len(autos)>0:
            mostrarVehículos(autos)
        else:
            print("\nNo hay registros ingresados.")
    
    elif opcion == 2:
         auto = solicitarDatosVehículo()
         dao.ingresarDatos(auto)
    
    elif opcion == 3:
        autos = dao.mostrarDatos()
        idConsultar = solicitarIDConsultar(autos)
        if(idConsultar == ""):
            print("\nID de vehículo no encontrado.")
        else:
            dao.consultarDatos(idConsultar)
   
    elif opcion == 4:
        autos = dao.mostrarDatos()
        if len(autos)>0:
            idEliminar = solicitarIDEliminar(autos)
            if(idEliminar == ""):
                print("\nID de vehículo no encontrado.")
            else:
                dao.borrarDatos(idEliminar)
        else:
            print("\nNo existen elementos para eliminar.")    
    
    elif opcion == 5:
        autos = dao.mostrarDatos()
        if len(autos)>0:
            auto = solicitarIDModificar(autos)
            if auto:
                dao.modificarDatos(auto)
        else:
            print("\nNo existen elementos para modificar.")    
    
    else:
        print("\nOpción no válida")

def mostrarVehículos(autos):
    print("\n Listado de vehículos en la base de datos:\n")
    for auto in autos: 
        datos = "ID: {0} | N° Chasis: {1} | Marca: {2} | Modelo: {3} | Cilidraje(cc): {4} | Precio($): {5} "
        print(datos.format(auto[0], auto[1], auto[2], auto[3], auto[4], auto[5]))
        print()

def solicitarDatosVehículo():
    id = input("\nIngrese el ID del vehículo: ")
    chasis = input("Ingrese el número de chasis del vehículo: ")
    chasisEncriptado = hashlib.sha1(chasis.encode())
    marca = input("Ingrese la marca del vehículo: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    cilindraje = int(input("Ingrese el cilindraje en cc del vehículo: "))
    precio = int(input("Ingrese el precio del vehículo: "))

    auto = (id, chasisEncriptado, marca, modelo, cilindraje, precio)
    return auto

def solicitarIDEliminar(autos):
    mostrarVehículos(autos)
    idEncontrado = False
    idEliminar = int(input("\nIngrese el ID del vehículo que desea eliminar: "))
    for auto in autos:
        if auto[0] == idEliminar:
            idEncontrado = True
            break
    if not idEncontrado:
        idEliminar = ""
    return idEliminar
    
def solicitarIDModificar(autos):
    mostrarVehículos(autos)
    idEncontrado = False
    idModificar = int(input("\nIngrese el ID del vehículo que desea modificar: "))
    for auto in autos:
        if auto[0] == idModificar:
            idEncontrado = True
            break

    if idEncontrado:
        chasis = input("\nIngrese el nuevo número de chasis del vehículo: ")
        chasisEncriptado = hashlib.sha1(chasis.encode()) 
        marca = input("Ingrese la nueva marca del vehículo: ")
        modelo = input("Ingrese el nuevo modelo del vehículo: ")
        cilindraje = input("Ingrese el nuevo cilindraje del vehículo: ")
        precio = input("Ingrese el nuevo precio del vehículo: ")
        auto = (idModificar, chasisEncriptado, marca, modelo, cilindraje, precio)
    
        return auto
    else:
        print("\nID de vehículo no encontrado.")


def solicitarIDConsultar(autos):
    idEncontrado = False
    idConsultar = int(input("\nIngrese el ID del vehículo que desea consultar : "))
    for auto in autos:
        if auto[0] == idConsultar:
            idEncontrado = True
            break
    if not idEncontrado:
        idConsultar = ""
    return idConsultar

#MAIN

menuPrincipal()