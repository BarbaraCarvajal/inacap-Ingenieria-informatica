class Persona:
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido

  #El str se encarga de los prints
  def __str__(self):
    cadena = self.nombre+" "+self.apellido
    return cadena

  

persona1 = Persona("Barbara", "Carvajal")
print(persona1)

#no se puede impimir un objeto directamente en un print
# persona1 = Persona("Barbara", "Carvajal")
# print(persona1)