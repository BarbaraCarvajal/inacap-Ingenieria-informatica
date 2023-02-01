import mysql.connector

## conexion

def conexion():
    conexion1 = mysql.connector.connect(host= "localhost",
                                        user = "root",
                                        passwd= "",
                                        database="basededatos1",
                                        port="8080")
    return conexion1
    

## listar tablas de una base de datos
def verTablas(conexion1):
    print("Tablas:")
    cursor1= conexion1.cursor()
    cursor1.execute("show tables")
    for tablas in cursor1:
        print(tablas)
    conexion1.close()


## insertar fila o registro en tabla

def crear(conexion1):
    print("AGREGAR PRODUCTO")
    cursor1 = conexion1.cursor()
    num = int(input("Ingrese cuántos productos ingresará: "))
    
    for x in range(num):
        cursor1 = conexion1.cursor()
        sql = "insert into articulos(descripcion, precio) values (%s, %s)"
        descripcion = input("Ingrese el producto: ")
        precio = float(input("Ingrese el precio: $"))
        datos = (descripcion, precio)
        cursor1.execute(sql,datos)
    conexion1.commit()
    conexion1.close()

## recuperar datos
def leer(conexion1):
    cursor1 = conexion1.cursor()
    cursor1.execute("select codigo, descripcion, precio from articulos")
    print("CODIGO - ARTICULO - PRECIO")
    for cod,art,pre in cursor1:
        print(f"{cod} - {art} - ${pre}")
    conexion1.close()

## eliminar o modificar registros

## delete
def eliminar(conexion1):
    cursor1 = conexion1.cursor()
    #leer(conexion1)
    print("ELIMINAR PRODUCTO")
    num = int(input("Ingrese el codigo del articulo que desea eliminar: "))
    cursor1.execute(f"delete from articulos where codigo = {num}") #borrrar registro
    print(f"El articulo codigo {num} ha sido eliminado con exito")
    conexion1.commit()

## update
def actualizar(conexion1):
    
    cursor1 = conexion1.cursor()
    #leer(conexion1)
    codigo = int(input("Ingrese el codigo del articulo que desee modificar: "))
    dato = int(input(
"""Qué dato desea actualizar?
presione 1 para modificar descripcion
presione 2 para modificar precio """))
    if dato == 1:
        articulo = input("Ingrese el nombre del articulo: ")
        cursor1.execute(f"update articulos set descripcion = {articulo} where codigo = {codigo}") #modificar regristro
        conexion1.commit()
        conexion1.close()
    elif dato == 2:
        precioNuevo = int(input("Ingrese el precio nuevo:"))
        cursor1.execute(f"update articulos set precio = {precioNuevo} where codigo = {codigo}") #modificar registro
        conexion1.commit()
        conexion1.close()
    else:
        print("Opcion ingresada incorrecta")
        conexion1.close()


    
def menu(conexion1):
    while True:
        print("""
(1) VER TABLAS DE LA BASE DE DATOS
(2) VER PRODUCTOS DE LA TABLA ARTICULOS
(3) AGREGAR PRODUCTOS
(4) ELIMINAR PRODUCTOS
(5) MODIFICAR ARTICULO
(6) SALIR
""")
        opcion = int(input("Ingrese su opción: "))
        if opcion == 1:
            verTablas(conexion())
        elif opcion == 2:
            leer(conexion())
        elif opcion == 3:
            crear(conexion())
        elif opcion == 4:
            eliminar(conexion())
        elif opcion == 5:
            actualizar(conexion())
            
        elif opcion == 6:
            print("Muchas gracias por usar nuestro programa :D")
            break
        else:
            print("Porfavor ingresar una opción correcta")





menu(conexion())





