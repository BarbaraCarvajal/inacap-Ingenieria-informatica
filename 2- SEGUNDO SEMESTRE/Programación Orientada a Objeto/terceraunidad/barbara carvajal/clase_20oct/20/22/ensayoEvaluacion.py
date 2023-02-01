import hashlib
import mysql.connector

class Conexion():
  def __init__(self):
    self.conexion1 = mysql.connector.connect(host="localhost", 
                                      user="root", 
                                      passwd="", 
                                      database= "ensayo",
                                      port = "8080")
    self.cursor1 = self.conexion1.cursor()

class Automovil(Conexion):
  
  def verTablas(self):
        print("Tablas:")
        cursor1= self.conexion1.cursor()
        cursor1.execute("show tables")
        for tablas in cursor1:
            print(tablas)
        self.conexion1.close()

  def crear(self):
    print("AGREGAR AUTO")
    #cursor1 = self.conexion1.cursor()
    if self.conexion1.is_connected():
      num = int(input("Ingrese cuántos autos ingresará: "))
      for x in range(num):
          #self.cursor1 = self.conexion1.cursor()
          sql = "insert into autos (n_chasis, modelo, marca, cilindrado, precio) values (%s, %s. %s, %s, %s)"
          
          n_chasis = int(input("Ingrese el numero de chasis: "))
          marca = input("Ingrese la marca del auto: ")
          modelo = input("Ingrese el modelo del auto: ")
          precio = int(input(f"Ingrese el precio del auto {marca} modelo {modelo} $"))
          cilindrado = int(input(f"Ingrese el cilindrado del auto {marca} modelo {modelo}: "))
          
          datos = (n_chasis, modelo, marca, cilindrado, precio)
          self.cursor1.execute(sql,datos)
      self.conexion1.commit()
      self.conexion1.close()

    # Mostrar datos
  def leer(self):
    if self.conexion1.is_connected():
      cursor1 = self.conexion1.cursor()
      cursor1.execute("select n_chasis, modelo, marca, cilindrado, precio from autos")
      print("")
      for n_chasis, modelo, marca, cilindrado, precio in cursor1:
          print(f"{n_chasis} - {modelo} - {marca} - {cilindrado} - ${precio} ")




primeraConexion = Automovil()
#primeraConexion.verTablas()
primeraConexion.crear()
#primeraConexion.leer()


















"""class Auto:
    def __init__(self,marca,modelo,n_chasis,cilindrado,precio):
        self.marca = marca
        self.modelo = modelo
        self.n_chasis = n_chasis
        self.cilindrado = cilindrado
        self.precio = precio"""