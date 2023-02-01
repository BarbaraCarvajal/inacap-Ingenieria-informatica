import hashlib
import mysql.connector

class Auto:
  def __init__(self,marca,modelo,n_chasis,cilindrado,precio):
    self.marca = marca
    self.modelo = modelo
    self.n_chasis = cilindrado
    self.precio = precio
  
  def conexion(self):
    self.conexion1 = mysql.connector.connect(host = "localhost",
                                             user = "root",
                                             passwd = "",
                                             database = "automoviles",
                                             port = "8080")

  def menu(self):

    def agregarDatos():
