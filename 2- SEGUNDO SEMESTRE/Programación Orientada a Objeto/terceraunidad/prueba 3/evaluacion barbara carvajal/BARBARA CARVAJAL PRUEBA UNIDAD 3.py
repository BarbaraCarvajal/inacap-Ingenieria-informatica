import hashlib
import mysql.connector


class Celulares():

    #metodo constructor:
    #conexion:
    def __init__(self):
        self.conexion1 = mysql.connector.connect(host = "localhost",
                                                user = "root",
                                                passwd = "",
                                                db = "evaluacion")
  
    #metodos
    def agregarDatos(self):
        cursor1 = self.conexion1.cursor()
        print("Agregar nuevo celular al sistema")
        self.marca = input("Ingrese marca: ")
        self.modelo = input("Ingrese el modelo: ")
        self.numero_serie = int(input("Ingrese numero de serie: "))
        while True:
            precio = int(input("Ingrese el precio: $ "))
            if precio >0 :
                self.precio = precio
                break
            else:
                print("Porfavor ingresar un valor mayor a $0.")

        datos = (self.marca, self.modelo, self.numero_serie, self.precio)
        cursor1.execute(f"insert into celulares(marca, modelo, numero_serie, precio) values {datos}")
        self.conexion1.commit()
        print("Celular Agregado con exito!")
        #self.conexion1.close() 

    def mostrarDatos(self):
        cursor1 = self.conexion1.cursor()
        print("Celulares en nuestro sistema")
        cursor1.execute(f"select * from celulares")
        for marca, modelo, numero_serie, precio in cursor1:
            print(marca, modelo, numero_serie, precio)

    def consultarDatos(self):
        cursor1 = self.conexion1.cursor()
        self.mostrarDatos()
        print("Consulta de datos")
        dato = input("Ingrese el numero de serie que desea consultar: ")
        cursor1.execute(f"select * from celulares where numero_serie = {dato}")

        print(f"Datos rescatados segun el codigo {dato}")
        for marca, modelo, numero_serie, precio in cursor1:
            print(marca, modelo, numero_serie, precio)

    def modificacionDeDatos(self):
        cursor1 = self.conexion1.cursor()
        self.mostrarDatos()
        print("Modificar datos")
        dato = input("Ingrese el numero de serie del celular que quiere modificar: ")
        print("Actualice los datos a continuacion: ")
        self.marcanueva = input("Ingrese la marca del celular: ")
        self.modelonuevo = input(f"Ingrese el modelo del {self.marcanueva}: ")
        self.numero_serienuevo = int(input(f"Ingresse el numero de serie del celular {self.marcanueva} {self.modelonuevo}: "))
        
        while True:
            precio = int(input(f"Ingrese el precio del celular {self.marcanueva} {self.modelonuevo} $"))
            if precio >0 :
                self.precionuevo = precio
                break
            else:
                print("Porfavor ingresar un valor mayor a $0.")
        cursor1.execute(f"update celulares set marca = '{self.marcanueva}', modelo = '{self.modelonuevo}', numero_serie = '{self.numero_serienuevo}', precio = '{self.precionuevo}' where numero_serie = {dato}")
        self.conexion1.commit()
        print("Celular actualizado con exito ")
    
    

    def eliminarRegistro(self):
        cursor1 = self.conexion1.cursor()
        print("Eliminacion de registros")
        while True:
            print("""
Desea eliminar 1 solo registro o todos los registros del sistema?

Opción 1 = Deseo eliminar solo 1 registro.
Opción 2 = Deseo eliminar todos los registros del sistema.
Opción 3 = Me arrepentí de eliminar algun registro.
""")
            respuesta = int(input("Ingrese su respuesta: "))
            if respuesta == 1:
                self.mostrarDatos()
                print()
                registro = int(input("Ingrese el numero de serie del celular que desea eliminar"))
                cursor1.execute(f"delete from celulares where numero_serie = {registro}")
                self.conexion1.commit()
                print("Celular eliminado del sistema")
                break
            elif respuesta == 2:
                cursor1.execute("truncate table celulares")
                self.conexion1.commit()
                print("Todos los celulares eliminados")
                break
            elif respuesta == 3:
                print("No se eliminará ningún registro.")
                break
            else:
                print("Porfavor ingresar una opción valida.")


    def encriptamiento(self):
        cursor1 = self.conexion1.cursor()
        self.mostrarDatos()
        num = (input("Ingrese el numero de serie del celular que desea encriptar"))
        actualizado = hashlib.sha1(num.encode())
        cursor1.execute(f"update celulares set numero_serie = '{actualizado}' where numero_serie = {num}")
        print("Numero de serie encriptado con exito :D ")
        print(f"Numero de serie encriptada: {actualizado.digest()}")

    def menu(self):
       while True:
        print("""
___MENU___
1- Agregar celular
2- Mostrar celulares
3- Consultar celular según el número de serie
4- Modificación de datos del celular
5- Eliminar registro según número de serie
6- Encriptar un numero de serie
7- Finalizar programa.
""")
        opcion = int(input("Ingrese su opción: "))
        if opcion == 1:
            self.agregarDatos()
        elif opcion == 2:
            self.mostrarDatos()
        elif opcion == 3:
            self.consultarDatos()
        elif opcion == 4:
            self.modificacionDeDatos()
        elif opcion == 5:
            self.eliminarRegistro()
        elif opcion == 6:
            self.encriptamiento()    
        elif opcion == 7:
            print("Muchas gracias, hasta luego :D")
            self.conexion1.close()
            break
        else:
            print("Ingrese una opción correcta.")


#main
celular1 = Celulares()
celular1.menu()

