#import mysql.connector
from conectar import conexion



#create
def agregarDatos():
    conexion1 = conexion()
    cursor = conexion1.cursor()
    
    print("Ingrese datos del alumno")
    rut = input("Ingrese su rut: ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    clave = int(input("Ingrese su clave: "))
    
    sql = "insert into alumnos(rut,nombre,apellido,clave) values (%s,%s,%s,%s)"
    datos = (rut, nombre, apellido, clave)
    cursor.execute(sql,datos)
    
    conexion1.commit()
    #cursor1.close()
    print("Alumno agregado con exito al sistema :D")
    

#read
def verDatos():
    conexion1 = conexion()
    cursor = conexion1.cursor()
    
    print("Datos de la tabla alumnos:")
    cursor.execute("select * from alumnos")
    # iteramos en la consulta de sql:
    for rut, nombre, apellido, clave in cursor:
        print(rut, nombre, apellido, clave)
    
def consultarDatos():
    conexion1 = conexion()
    cursor = conexion1.cursor()
    verDatos()
    
    consulta = input("Ingrese el rut del alumno que quiere consultar: ")
    cursor.execute(f"select * from alumnos where rut = {consulta}")
    print("datos del alumno: ")
    
    for rut, nombre, apellido, clave in cursor:
        print(f"RUT: {rut}, NOMBRE: {nombre}, APELLIDO: {apellido}, CLAVE: {clave}")
        
#update
def modicarDatos():
    conexion1 = conexion()
    cursor = conexion1.cursor()
    print("Modificación de datos")
    verDatos()
    dato = input("Ingrese el rut del alumno que desea modificar: ")
    
    print("Ingrese datos nuevos del alumno")
    rut = input("Ingrese su rut: ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    clave = int(input("Ingrese su clave: "))
    
    cursor.execute(f"update alumnos set rut = '{rut}', nombre = '{nombre}', apellido = '{apellido}', clave = '{clave}' where rut ={dato}")
    conexion1.commit()
    print("Datos actualizados con exito! :D")
    
#delete  
def eliminarDatos():
    conexion1 = conexion()
    cursor = conexion1.cursor()
    verDatos()
    print("Eliminar datos: ")
    dato = input("Ingrese el rut del alumno que desea eliminar:  ")
    cursor.execute(f"delete from alumnos where rut = {dato}")
    conexion1.commit()
    print("Alumnos eliminado del sistema con exito :D")
    

    


