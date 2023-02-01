"""7. Cree un Diccionario que contenga claves y los valores como como Tuplas, luego obtenga a 
través de funciones distintas estadísticas (sueldo más bajo, edad más alta, promedio de 
sueldos, etc). La función debe recibir los datos como parámetros.
Ejemplo: Clave=nombre de empleado, Valores=edad, sueldo.
empleado = {
 “Carlos”:(19, 250000),
 “Marcela”:(25, 350000),
 }"""
import os 
os.system("clear")

def sueldo_mas_bajo(empleado):
    sueldo_bajo = []
   
    for edad, sueldo in empleado.values():
        sueldo_bajo.append(sueldo)
    masBajo = min(sueldo_bajo)
    print(f"El sueldo más bajo es de ${masBajo}")

def sueldo_mas_alto(empleado):
    sueldo_alto = []
   
    for edad, sueldo in empleado.values():
        sueldo_alto.append(sueldo)
    masAlto = max(sueldo_alto)
    print(f"El sueldo más alto es de ${masAlto}")

def edad_mas_alta(empleado):
    edades = []
    for edad, sueldo in empleado.values():
        edades.append(edad)
    masAlta = max(edades)
    print(f"La edad mayor es de: {masAlta}")

def edad_mas_baja(empleado):
    edades = []
    for edad, sueldo in empleado.values():
        edades.append(edad)
    masBaja = min(edades)
    print(f"La edad menor es de: {masBaja}")

def promedio_sueldos(empleado):
    sueldos = []
    for edad, sueldo in empleado.values():
        sueldos.append(sueldo)
    suma = sum(sueldos)

    promedio = suma/len(sueldos)
    print(f"El promedio de sueldo es: ${promedio}")

def promedio_edades(empleado):
    promedio_edad = []
    for edad, sueldo in empleado.values():
        promedio_edad.append(edad)
    promedio_edad = sum(promedio_edad)/len(promedio_edad)
    print(f"La edad promedio es de {promedio_edad}")

def trabajador(empleado):
    x = input("Ingrese el nombre del trabajador: ").title()
    for nombres in empleado.keys():
        if x == nombres:
            print(f"El empleado {nombres} sí se encuentra en nuestros sistemas")
            acceder_datos = empleado.get(nombres)
            print(f"El empleado {nombres} tiene {acceder_datos[0]} y gana ${acceder_datos[1]}")
         
def agregarTrabajador(empleado):
    nombre = input("Ingrese el nombre del empleado: ").lower()
    edad = input(f"Ingrese la edad de {nombre}: ")
    sueldo = input(f"Ingrese el sueldo de {nombre}: $")

    empleado[nombre] = (edad,sueldo) #metodo para agregar a un diccionario

    print()
    print(f"Nuevo empleado agregado con exito!")
    print(f"""
    Nombre: {nombre}
    Edad:   {edad}
    Sueldo: {sueldo}""")

def mostrarTrabajadores(empleado):
    for x in empleado:
        print(x)

def eliminarTrabajador(empleado):
    nombre = input("Ingrese el trabajador que desea eliminar: ").lower()
    if nombre in empleado:
        del empleado[nombre]
        print(f"{nombre} ha sido eliminado con exito de nuestros sistemas")
        print("Lista de empleados actualizada:")
        mostrarTrabajadores(empleado)
    else:
        print("Ese trabajador no esta en nuestro sistema")

def modificarDatos(empleado):
    print("Trabajadores que puede editar sus datos:")
    mostrarTrabajadores(empleado)
    nombre = input("Ingrese el nombre del trabajador que desea modificar: ")
    opcion = int(input("¿Qué dato desea modificar? nombre = 1 edad = 2 sueldo = 3  "))
    if opcion == 1:
        print(f"nombre original: {nombre}")
        nuevoNombre = (f"Ingrese el nombre actualizado: ")
        empleado.update(nuevoNombre)



empleado = {
    "Carlos":   (19, 250000),
    "Marcela":  (30, 350000),
    "Mokita":   (20, 650000),
    "Aurora":   (25, 750000),
    "Latte":    (23, 450000)
}

#menu
sw = True
while sw == True:
    opcion = int(input(("""
***OPCIONES***
1) VER SUELDO MÁS ALTO
2) VER SUELDO MAS BAJO
3) VER EDAD MAYOR
4) VER EDAD MENOR
5) VER PROMEDIO DE EDADES
6) VER PROMEDIO DE SUELDO
7) CONSULTAR POR TRABAJADOR ESPECIFICO SEGUN SU NOMBRE
8) AGREGAR A UN TRABAJADOR
9)VER LISTADO DE TRABAJADORES 
10)ELIMINAR A UN TRABAJADOR
11) MODIFICAR UN DATO DEL TRABAJADOR
12) SALIR
Ingrese su opcion:  """)))
    if opcion == 1:
        sueldo_mas_alto(empleado)
    elif opcion == 2:
        sueldo_mas_bajo(empleado)
    elif opcion == 3:
        edad_mas_alta(empleado)
    elif opcion == 4:
        edad_mas_baja(empleado)
    elif opcion == 5:
        promedio_edades(empleado)
    elif opcion == 6:
        promedio_sueldos(empleado)
    elif opcion == 7:
        trabajador(empleado)
    elif opcion == 8:
        agregarTrabajador(empleado)
    elif opcion == 9:
        mostrarTrabajadores(empleado)
    elif opcion == 10:
        eliminarTrabajador(empleado)
    elif opcion == 11:
        modificarDatos(empleado)
    elif opcion == 12:
        print("Muchas gracias, chaito")
        sw = False
    
