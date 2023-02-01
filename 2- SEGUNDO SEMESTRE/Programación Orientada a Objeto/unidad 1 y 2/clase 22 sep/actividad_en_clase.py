# declara una clase llamada familia, definir como atributos el nombre
# del padre, madre y una lista con los nombres de los hijos.
# definir el método str que retorne string con el nombre del padre, madre e hijos

class Familia:
  
  def __init__(self,padre,madre,hijos = []):
    
    self.nombrePadre = padre
    self.nombreMadre = madre
    self.hijos = hijos
  
  def __str__(self):
    cadena = self.nombrePadre+" es el padre, "+self.nombreMadre+" es la madre "

    for x in self.hijos:
      cadena = cadena + x
    return cadena

familia1 = Familia("Camilo", "Bárbara")
print(familia1)