import mysql.connector
import hashlib

"""Debe mostrar un menú con las siguientes opciones: 
1- Agregar datos
2- Mostrar Datos
3- Consulta datos según el número de chasis
4- Modificación de datos
5- Eliminar registro según número de chasis
6- Finalizar programa."""

class Auto():
  #conectar
  def __init__(self):
    self.conexion1 = mysql.connector.connect(host = "localhost",
                                            port = "8080",
                                            user = "root",
                                            passwd = "",
                                            db = "practicaPrueba")
  
  
        
  #metodos
  def agregarDatos(self):
    cursor1 = self.conexion1.cursor()
    
    self.codigo = int(input("Ingrese el codigo: "))
    self.marca = input("Ingrese la marca del auto: ")
    self.modelo = input("Ingrese el modelo del auto: ")
    self.chasis = (input("Ingresse el chasis: "))
    self.cilindrado = int(input(f"Ingrese el cilindrado del {self.marca}: "))
    self.precio = int(input(f"Ingrese el precio del auto {self.marca}: "))

    self.chasisEncriptado = hashlib.sha1(self.chasis.encode())
    
    datos = (self.codigo, self.marca, self.modelo, self.chasisEncriptado, self.cilindrado, self.precio)
    cursor1.execute(f"insert into automovilesPrueba(precio, marca, modelo, chasisEncriptado, cilindrado, precio) values {datos}")
    self.conexion1.commit()

    #self.conexion1.close()
    # Forma para hacerlo con input 
    # contrasena = input("Ingrese su contraseña: ")
    # contrasenaEncripada = hashlib.sha384(contrasena.encode())
    # print(f"Contraseña encriptada con digest: {contrasenaEncripada.digest()}")

  
  
  def mostrarDatos(self):
    cursor1 = self.conexion1.cursor()
    cursor1.execute("SELECT * FROM AUTOMOVILESPRUEBA")
    print("AUTOMOVILES")
    for codigo, marca, modelo,chasis,cilindrado, precio in cursor1:
      print(codigo, marca, modelo,chasis,cilindrado, precio)
    #self.conexion1.close()

  def consultarDatos(self):
    cursor1 = self.conexion1.cursor()
    self.mostrarDatos()
    print()
    datoAconsultar = int(input("Ingrese el codigo a consultar: "))
    cursor1.execute(f"select * from automovilesprueba where codigo = {datoAconsultar}")
    for codigo, marca, modelo,chasis,cilindrado, precio in cursor1:
      print(marca, modelo,chasis,cilindrado, precio)
    #self.conexion1.close()
  
  def eliminarDatos(self):
    cursor1 = self.conexion1.cursor()
    self.mostrarDatos()
    print()
    datoAeliminar = int(input("Ingrese el codigo del auto para eliminarlo: "))
    cursor1.execute(f"delete from automovilesprueba where codigo = {datoAeliminar}")
    print(f"El automovil con el chasis {datoAeliminar} ha sido eliminado con exito")
    self.conexion1.commit()
    #self.conexion1.close()

  def modificarDatos(self):
    cursor1 = self.conexion1.cursor()
    self.mostrarDatos()
    modificar = int(input("Ingrese el chasis a modificar: "))
    print("Actualice los datos a continuacion: ")
    self.marca = input("Ingrese la marca del auto: ")
    self.modelo = input("Ingrese el modelo del auto: ")
    self.chasis = int(input("Ingresse el numero de chasis: "))
    self.cilindrado = int(input(f"Ingrese el cilindrado del {self.marca}"))
    self.precio = int(input(f"Ingrese el precio del auto {self.marca}"))

    self.chasisEncriptado = hashlib.sha384(self.chasis.encode())

    actualizacion = self.marca, self.modelo, self.chasisEncriptado, self.cilindrado, self.precio

    cursor1.execute(f"update automovilesprueba set {actualizacion} where codigo = {modificar} ")
    self.conexion1.commit()
    #self.conexion1.close()

  def menu(self):
    while True:
      print("""
___MENU___
1- Agregar datos
2- Mostrar Datos
3- Consulta datos según el número de chasis
4- Modificación de datos
5- Eliminar registro según número de chasis
6- Finalizar programa.
""")
      opcion = int(input("Ingrese su opción: "))
      if opcion == 1:
        self.agregarDatos()
      elif opcion == 2:
        self.mostrarDatos()
      elif opcion == 3:
        self.consultarDatos()
      elif opcion == 4:
        self.modificarDatos()
      elif opcion == 5:
        self.eliminarDatos()
      elif opcion == 6:
        print("Muchas gracias, hasta luego :D")
        self.conexion1.close()
        break
      else:
        print("Ingrese una opción correcta.")





auto1 = Auto()
auto1.menu()



#auto1.agregarDatos()
#auto1.mostrarDatos()
#auto1.consultarDatos()
#auto1.modificarDatos()
#auto1.eliminarDatos()

#import hashlib

#Encriptación

"""passEncrip = hashlib.new("sha1",b"123456")
#print(passEncrip.digest()) #digest retorna la cadena cifrada en binario
#print(passEncrip.hexdigest()) #hexdigest retorna la cadena cifrada en hexadecimal

# Otra forma de hacerlo
passEncrip2 = hashlib.sha1()
passEncrip2.update(b"123456")
#print(passEncrip2.digest())


# Forma para hacerlo con input 
contrasena = input("Ingrese su contraseña: ")
contrasenaEncripada = hashlib.sha384(contrasena.encode())

print(f"Forma no encriptada{contrasena}")
print(f"Contraseña encriptada con digest: {contrasenaEncripada.digest()}")
print(f"Contraseña encriptada con hexadecimal: {contrasenaEncripada.hexdigest()}")
print()

def actualizar(conexion1):
    
    cursor1 = conexion1.cursor()
    #leer(conexion1)
    codigo = int(input("Ingrese el codigo del articulo que desee modificar: "))
    dato = int(input(
Qué dato desea actualizar?
presione 1 para modificar descripcion
presione 2 para modificar precio ))
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
        conexion1.close()"""