from conexion import conexion
import hashlib


#add
def agregarA():
    conexion1=conexion()
    cursor1=conexion1.cursor()

    print("Agregar alumnos")

    rut=input("Ingrese el rut del alumno: ")
    nombre=input("Ingrese el nombre del alumno: ")
    apellido=input("Ingrese el apellido del alumno: ")
    clave=input("ingrese la clave del alumno: ")

    datos=(rut,nombre,apellido,clave)
    sql="insert into alumnos (rut,nombre,apellido,clave) values (%s,%s,%s,%s)"

    cursor1.execute(sql,datos)
    
    conexion1.commit()
    print("agregaste un alumno+ nuevo a la tabla")



#watch

def MostrarA():
    conexion1=conexion()
    cursor1=conexion1.cursor()

    print("Mostrar todos los alumnos")

    cursor1.execute("select * from alumnos")
    for rut,nombre,apellido,clave in cursor1:
        print(rut,nombre,apellido,clave)

def consultarA():
    conexion1=conexion()
    cursor1=conexion1.cursor()
    
    consulta=input("Ingrese el rut del alumno a consultar: ")
    
    print("AQUI LOS DATOS DEL ALUMNO")
    cursor1.execute(f"select * from alumnos where rut={consulta}")
    for rut,nombre,apellido,clave in cursor1:
        print(rut,nombre,apellido,clave)

#update

def actualizarA():
    conexion1=conexion()
    cursor1=conexion1.cursor()
    
    print("actualizar alumno")

    MostrarA()

    seleccion=input("ingrese el rut del alumno a actualizar: ")
    
    rut=input("ingrese el rut del alumno: ")
    nombre=input("ingrese el nombre del alumno: ")
    apellido=input("ingrese el apellido del alumno: ")
    clave=input("ingrese la clave del alumno: ")

    cursor1.execute(f"update alumnos set rut = '{rut}' ,nombre = '{nombre}', apellido= '{apellido}',clave= '{clave}' where rut='{seleccion}'")
    conexion1.commit()
    print("ALUMNO ACTUALIZADO ")
   
#Erase

def borrarA():
    conexion1=conexion()
    cursor1=conexion1.cursor()

    print("BORRAR USUARIO")
    MostrarA()

    eliminado=input("ingrese el rut del usuario a eliminar: ")

    cursor1.execute(f"delete from alumnos where rut={eliminado}")
    conexion1.commit()

    print("ALUMNO  HA SIDO ELIMINADO")

def encriptarA():
    conexion1=conexion()
    cursor1=conexion1.cursor()

    print("ENCRIPTAR")
    MostrarA()
    
    claveEncript= input("ingrese la clave a encriptar: ")
    claveEncriptada= hashlib.md5(str(claveEncript).encode())
    cursor1.execute(f"update alumnos set clave = '{claveEncriptada}' where clave = '{claveEncript}'")
    print(f"clave encriptada {claveEncriptada.digest()}")
    conexion1.commit()

#borrarA()
#actualizarA()
#consultarA()
#MostrarA()
#agregarA()