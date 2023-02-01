from conexion import conexion
import hashlib

#create
def agregarDatos():
    conexion1 = conexion()
    cursor1 = conexion1.cursor()
    
    while True:
        print("""
Opciones: 
1) AGREGAR ALUMNO NUEVO
2) AGREGAR ASIGNATURA
3) SALIR
""")
        opcion = int(input("Ingrese su opcion"))
        if opcion == 1:
        
            print("Ingrese los datos del alumno: ")
            rut = input("Ingrese el rut: ")
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            clave = int(input("Ingrese su clave: "))
            
            sql = "insert into alumnos(rut, nombre, apellido, clave) values (%s, %s, %s, %s)"
            datos = (rut,nombre,apellido,clave)
            cursor1.execute(sql,datos)
            
            conexion1.commit()
            #cursor1.close() 
            print("Alumno ingresado correctamente :D")
        elif opcion == 2:
            nombre = input("Ingrese el nombre de la asignatura: ")
            codigo = input(f"Ingrese el codigo de la asignatura {nombre}: ")
            semestre = int(input("Ingrese el numero de semestre: "))
            
            sql = "insert into asignaturas(codigo, nombre, semestre) values (%s, %s, %s)"
            datos = (codigo,nombre,semestre)
            cursor1.execute(sql,datos)
            conexion1.commit()
        elif opcion == 3:
            print("Adios")
            break
        else:
            print("Ingrese la opcion correcta")
#read
def verDatos():
    conexion1 = conexion()
    cursor1 = conexion1.cursor()
    
    print("Datos de la tabla alumnos")
    cursor1.execute("select * from alumnos")
    for rut,nombre,apellido,clave in cursor1:
        print(rut,nombre,apellido,clave)

def consultarDatos():
    
    conexion1 = conexion()
    cursor1 = conexion1.cursor()
    verDatos()
    
    consulta = input("Ingrese el rut del alumnno a consultar: ")
    cursor1.execute(f"select * from alumnos where rut = {consulta}")
    print("Datos del alumno: ")
    for rut,nombre,apellido,clave in cursor1:
        print(f"RUT: {rut} NOMBRE: {nombre} APELLIDO: {apellido} CLAVE: {clave}")

#update
def actualizarDatos():
    conexion1 = conexion()
    cursor1 = conexion1.cursor()
    print("Modificacion de datos :D")
    verDatos()
    dato = input("Ingrese el rut del alumno a actualizar: ")
    
    print("Ingrese los nuevos datos del alumno: ")
    rut = input("Ingrese el rut: ")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    clave = int(input("Ingrese su clave: "))

    cursor1.execute(f"update alumnos set rut = '{rut}', nombre = '{nombre}', apellido = '{apellido}', clave = '{clave}' where rut = '{dato}'")
    conexion1.commit()
    print("Datos actualizados :D ")

#delete
def eliminarDatos():
    conexion1 = conexion()
    cursor1 = conexion1.cursor()
    print("Elminar datos")
    verDatos()
    
    dato = input("Ingrese el rut del alumno que desea eliminar :D ")
    cursor1.execute(f"delete from alumnos where rut = {dato}")
    conexion1.commit()
    print("Alumno eliminado con exito :D")

def encriptamiento():
    conexion1 = conexion()
    cursor1 = conexion1.cursor()
    print("ENCRIPTAMIENTO")
    verDatos()
    clavePreg = int(input("Ingrese la clave que desea encriptar: "))
    claveActualizada = hashlib.md5(str(clavePreg).encode())
    cursor1.execute(f"update alumnos set clave = '{claveActualizada}' where clave = '{clavePreg}'")
    print(f"clave encriptada: {claveActualizada.digest()}")
    conexion1.commit()



    