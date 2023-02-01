from BD.Conectar import Conexion

def Buscar():
    #Esta funcion les puede servir como ayuda para verificar si existe o no un alumno antes de eliminar o actualizar o insertar
    conect=Conexion()
    cursor=conect.cursor()
    try:
        rut=input("Ingrese Rut: ")
        sql="select * from alumnos where rut=%s"
        cursor.execute(sql,(rut,))
        resul=cursor.fetchone()
        if resul is not None:
            print("Rut  Nombre  Apellido    Clave")
            print("{0}   {1}      {2}           {3}".format(resul[0],resul[1],resul[2],resul[3]))
        else:
            print("usuario no existe")
        conect.close()
    except:
        print("ERROR EN LA CONSULTA")
             

def Insertar():
    conect=Conexion()
    cursor=conect.cursor()
    try:
       rut=input("Ingrese Rut: ")
       nombre=input("Ingrese Nombre: ")
       apellido=input("Ingrese Apellido: ")
       clave=input("Ingrese Contraseña: ")
       #En clases usamos esta estructura de sql puesto que me generaba un error al enviar los parametros. Lo que hice fue
       # separar los parametros con un espacio, ojo con eso, y asi pude usar la forma de tuplas en el envio de los parametros.
       #sql="INSERT INTO alumnos(rut,nombre,apellido,clave) values({},'{}','{}','{}','{}')".format(id,nombre1,apellido1,cuenta1,hora)
       sql="INSERT INTO alumnos(rut,nombre,apellido,clave) values(%s,%s,%s,%s)"
       cursor.execute(sql,(rut, nombre, apellido, clave))
       conect.commit()
       conect.close()
    except:
       print("ERROR EN LA CONSULTA")
    

def Listar():
    conect=Conexion()
    cursor=conect.cursor()
    try:
        #sql="select * from usuarios where id=300"
        sql="select * from alumnos"
        cursor.execute(sql)
        resultado=cursor.fetchall()
        for i in resultado:
            print(i)
        conect.close()
    except:
        print("ERROR EN LA CONSULTA")
        return None
    return resultado    

def Actualizar():
    conect=Conexion()
    cursor=conect.cursor()
    try:
        rut=input("Ingrese rut de Alumno: ")
        clave=input("Ingrese nueva Contraseña: ")
        #sql="update alumnos set clave='{}' where id={}".format(cuenta,codigo)
        sql="update alumnos set clave=%s where rut=%s"
        cursor.execute(sql,(clave, rut))
        conect.commit()
        conect.close()
    except:
        print("ERROR EN LA CONSULTA")
    return None
       
def Eliminar():
    conect=Conexion()
    cursor=conect.cursor()
    try:
        rut=input("Ingrese rut de Alumno: ")
        sql="delete from alumnos where rut=%s"
        #OJO aca... fijense que despues del parametro rut usado para identificar el rut a eliminar, va una coma (,)
        #eso le indica a la query que el campo es una tupla.
        cursor.execute(sql,(rut,))
        conect.commit()
        conect.close()
    except:
        print("ERROR EN LA CONSULTA")
    return None       
    