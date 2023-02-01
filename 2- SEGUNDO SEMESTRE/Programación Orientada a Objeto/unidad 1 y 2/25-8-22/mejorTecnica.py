class Empleado:

  def __init__(self):
    self.nombre = input("Ingrese nombre: ")
    self.sueldo = int(input("Ingrese su sueldo: $"))
    self.edad = int(input("Ingrese su edad: "))
  
  def mostrarDatos(self):
    print(f"El trabajador {self.nombre} tiene {self.edad} años y gana ${self.sueldo}")


objeto1 = Empleado()
objeto1.mostrarDatos()


