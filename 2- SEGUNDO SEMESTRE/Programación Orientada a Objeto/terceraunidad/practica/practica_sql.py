import mysql.connector

class Conexion():
  def __init__(self):
    self.conexion1 = mysql.connector.connect(host="localhost", 
                                      user="root", 
                                      passwd="", 
                                      database= "basededatos1",
                                      port="8080" ) 
    self.cursor1 = self.conexion1.cursor()
    

  def leer(self):
    if self.conexion1.is_connected():
      cursor1 = self.conexion1.cursor()
      cursor1.execute("select codigo, descripcion, precio from articulos")
      print("CODIGO - ARTICULO - PRECIO")
      for cod,art,pre in cursor1:
          print(f"{cod} - {art} - ${pre}")

  def crear(self):
    print("AGREGAR PRODUCTO")
    #self.cursor1 = self.conexion1.cursor()
    if self.conexion1.is_connected():
      num = int(input("Ingrese cuántos productos ingresará: "))
      
      for x in range(num):
          #self.cursor1 = conexion1.cursor()
          sql = "insert into articulos(descripcion, precio) values (%s, %s)"
          descripcion = input("Ingrese el producto: ")
          precio = float(input("Ingrese el precio: $"))
          datos = (descripcion, precio)
          self.cursor1.execute(sql,datos)
      self.conexion1.commit()
      self.conexion1.close()
      
      
primeraConexion = Conexion()
primeraConexion.leer()
primeraConexion.crear()






