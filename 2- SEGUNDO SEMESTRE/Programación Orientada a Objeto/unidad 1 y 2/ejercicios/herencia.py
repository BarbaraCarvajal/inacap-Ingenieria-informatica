"""Problema 1:
Plantear una clase Persona que contenga 
dos atributos: nombre y edad. 
Definir como responsabilidades la carga 
por teclado y su impresión.
En el bloque principal del programa 
definir un objeto de la clase persona y 
llamar a sus métodos.
Declarar una segunda clase llamada 
Empleado que herede de la clase Persona y
 agregue un atributo sueldo y muestre si 
 debe pagar impuestos (sueldo superior a 3000)
También en el bloque principal del 
programa crear un objeto de la clase Empleado.
Auto "es un" Vehiculo
Circulo "es una" Figura
Mouse "es un" DispositivoEntrada
Suma "es una" Operacion"""

class Persona():
  def __init__(self):
    self.nombre = input("Ingrese su Nombre: ")
    self.edad = int(input("Ingrese su edad: "))


  def imprimir(self):
    print(f"Tu nombre es {self.nombre} y tienes {self.edad} años")

persona1 = Persona()
persona1.imprimir()

class Empleado(Persona):
  def __init__(self):
    super().__init__() 
    self.sueldo=float(input("Ingrese el sueldo:"))
  

  def imprimir(self): 
    super().imprimir() 
    print("Sueldo:",self.sueldo)

  def impuestos(self):
    if self.sueldo > 3000:
      print("Tiene que pagar impuestos")
    else:
      print("No tiene que pagar impuestos")

trabajador = Empleado()   
trabajador.imprimir()
trabajador.impuestos()