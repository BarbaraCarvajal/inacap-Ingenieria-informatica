import mysql.connector


def conectar():
    conexion1 = mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="",
                                        database="basededatos1",
                                        port="8080" )
    return conexion1

def listarTablas(conexion1):
    print("***LISTADO DE TABLAS***")
    cursor1= conexion1.cursor()
    cursor1.execute("show tables")
    for tabla in cursor1:
        print(tabla)
    conexion1.close()

def guardarDatos(conexion1):
    print("***GUARDAR DATOS***")
    cursor1= conexion1.cursor()
    sql = "insert into articulos(descripcion, precio) values (%s,%s)"
    nombreProducto=input("INGRESE NOMBRE PRODUCTO: ")
    precioProducto=int(input("INGRESE PRECIO PRODUCTO: "))
    datos=(nombreProducto,precioProducto)
    cursor1.execute(sql,datos)
    conexion1.commit()
    conexion1.close()

def mostrarDatos(conexion1):
    cursor1= conexion1.cursor()
    cursor1.execute("select codigo, descripcion,precio from articulos")
    for cod, nombre, precio in cursor1:
        print(cod,nombre,precio)
    conexion1.close()

#MAIN
while True:
    print("(1)LISTAR TABLAS")
    print("(2)GUARDAR DATOS")
    print("(3)MOSTRAR DATOS")
    print("(0)SALIR")
    opcion=int(input("INGRESE OPCIÓN: "))
    if opcion==1:       
        listarTablas(conectar())
    elif opcion==2:
        guardarDatos(conectar())
    elif opcion==3:
        mostrarDatos(conectar())
    elif opcion==0:
        break
