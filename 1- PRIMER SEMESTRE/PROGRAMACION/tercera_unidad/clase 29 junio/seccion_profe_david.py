nombre = []
edad = []

def guardarDatos():
    valor = input("ingrese nombre: ")       
    nombre.append(valor)
    valorEdad = int(input("ingrese edad: "))
    edad.append(valorEdad)

def mostrarDatos():
    for i in range(len(nombre)):
        print(f"{nombre[i]}\t{edad[i]}")

def buscarDato(nombreBuscar):
    if nombreBuscar in nombre:
        print("dato encontrado")
        return True
    else:
        print("dato no encontrado")
        return False
def editarDatos():
    valorEditar = input("ingrese nombre a editar: ")
    if buscarDato(valorEditar)==True:
        posicion = nombre.index(valorEditar)
        nombre[posicion] = input("ingrese nuevo nombre ")
def eliminarDatos():
    valorEliminar = input("ingrese nombre a eliminar: ")
    if buscarDato(valorEliminar)==True:
        nombre.remove(valorEliminar)
        print("dato eliminado")
    else:
        print("dato no eliminado")

while True:
    print('''********
    MENÚ PRINCIPAL
********
(1) MOSTRAR DATOS
(2) GUARDAR DATOS
(3) EDITAR DATOS
(4) ELIMINAR DATOS
(0) SALIR
    ''')
    opcion = int(input("ingrese opción: "))
    if opcion==1:
        mostrarDatos()
    elif opcion==2:
        guardarDatos()
    elif opcion==3:
        editarDatos()
    elif opcion==4:
        eliminarDatos()
    elif opcion==0:
        print("ADIOS")
        break