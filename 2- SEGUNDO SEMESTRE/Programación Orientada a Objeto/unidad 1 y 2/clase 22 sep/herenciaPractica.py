class Persona:

  def __init__(self,apePat, apeMat, nom):
    self.apellidoPaterno = apePat
    self.apellidoMaterno = apeMat
    self.nombre = nom

  def mostrarNombreCompleto(self):
    print(f"{self.nombre} {self.apellidoPaterno} {self.apellidoMaterno} ")

class Estudiante(Persona):
  def __init__(self, apePat, apeMat, nom, prof):
    super().__init__(apePat, apeMat, nom)
    self.profesion = prof

est1 = Estudiante("Carvajal", "Saez", "Barbara","informatica")
est1.mostrarNombreCompleto()
