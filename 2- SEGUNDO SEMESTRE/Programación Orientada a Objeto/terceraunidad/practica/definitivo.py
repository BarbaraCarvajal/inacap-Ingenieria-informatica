import mysql.connector


class conexion:
  def __init__(self):
      self.conexion1 = mysql.connector.connect(host="localhost", 
                                                user="root", 
                                                passwd="", 
                                                database= "practicaPrueba",
                                                port="8080" ) 
      #cursor1 = conexion1.cursor()
      return conexion1

class auto(conexion):

    def __init__(self):
        print("AGREGAR AUTO")
        self.marca = input("Ingrese la marca del auto: ")
        self.modelo = input("Ingrese el modelo del auto: ")
        self.chasis = int(input("Ingresse el numero de chasis: "))
        self.cilindrado = int(input(f"Ingrese el cilindrado del {self.marca}"))
        self.precio = int(input(f"Ingrese el precio del auto {self.marca}"))
        
        cursor1 = self.conexion1.cursor()
        sql = "insert into articulos(marca, modelo, chasis, cilindrado, precio) values (%s, %s. %s, %s, %s)"
        datos = (self.marca, self.modelo, self.chasis, self.cilindrado, self.precio)
        cursor1.execute(sql,datos)
        self.conexion1.commit()
        self.conexion1.close()
        
        print("Auto agregado con exito.")
        
    def verTablas(self):
        print("Tablas:")
        
        cursor1= self.conexion1.cursor()
        cursor1.execute("show tables")
        for tablas in cursor1:
            print(tablas)
        self.conexion1.close()

  
        


auto1 = auto()
auto1.verTablas()