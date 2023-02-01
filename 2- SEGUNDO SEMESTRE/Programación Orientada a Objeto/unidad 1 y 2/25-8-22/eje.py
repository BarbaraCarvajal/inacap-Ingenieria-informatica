#clase
class Alumno:
  #definir atributos de la clase y métodos
  def inicializar(self,nom,aPaterno, aMaterno, edad, rut, fono):
    self.nombre = nom
    self.apellidoPaterno = aPaterno
    self.apellidoMaterno = aMaterno
    self.edad = edad
    self.rut = rut
    self.fono = fono
  
  def imprimir(self):
    print("Nombre:           ",self.nombre)
    print("Apellido Paterno: ",self.apellidoPaterno)
    print("Apellido Materno: ",self.apellidoMaterno)
    print("Edad:             ",self.edad)
    print("Rut:              ",self.rut)
    print("Fono:             ",self.fono)

  #Agregar un metodo a la clase que identifique quien es mayor de edad
  def mayorEdad(self):
    if self.edad >= 18:
      print(f"El alumno: {self.nombre} es Mayor de edad, porque tiene {self.edad} años")
    else:
      print(f"El alumno: {self.nombre} es Menor de edad, porque tiene {self.edad} años")


#bloque principal

#creacion de objeto (instanciación)
print("Primer Alumno")
objeto1 = Alumno()             #declarar objeto
objeto1.inicializar("Anselmo", "Correa", "Gómez", 19, "15.456.897-9", 2588720) #instaciar objeto
objeto1.imprimir()
objeto1.mayorEdad()
print()


print("Segundo Alumno")
objeto2 = Alumno()             #declarar objeto
objeto2.inicializar("Adriana", "Rebolledo", "Navarrete", 15, "12.123.456-K", 4448026) #instaciar objeto
objeto2.imprimir()
objeto2.mayorEdad()





