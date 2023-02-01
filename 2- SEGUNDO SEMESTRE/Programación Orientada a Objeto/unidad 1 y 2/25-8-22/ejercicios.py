"""1. Crear una clase que represente un punto en el plano cartesiano y tenga los siguientes
métodos: inicializar los valores de x e y los cuales llegan como parámetros, imprimir en qué
cuadrante se encuentra dicho punto"""

class Cartesiano:
  def __init__(self,valorY, valorX):
    self.y = valorY
    self.x = valorX
  
  def cuadrante(self, y, X):
    if self.y > 0 and self.x > 0:
      print(f"El punto ({self.y},{self.x}) estan en el primer cuadrante  ")

    elif self.y < 0 and self.x > 0:
      print(f"El punto ({self.y},{self.x}) estan en el segundo cuadrante  ")

    elif self.y < 0 and self.x < 0:
      print(f"El punto ({self.y},{self.x}) estan en el tercer cuadrante  ")

    elif self.y > 0 and self.x < 0:
      print(f"El punto ({self.y},{self.x}) estan en el primer cuadrante  ")

num1 = float(input("Ingrese el valor de Y: "))
num2 = float(input("Ingrese el valor de X: "))

print()
plano = Cartesiano(num1,num2)
plano.cuadrante(num1, num2)
print()

"""2. Crear una clase que represente un Cuadrado y tenga los siguientes métodos: inicializar el
valor del lado llegando como parámetro al método __init__ (definir un atributo llamado
lado), imprimir su perímetro y su superficie."""

print()
print("***_Perimetro y Superficie_***")
print()
class Cuadrado():
  def __init__(self):
    self.lado = float(input("Ingrese el lado: "))

  def informacion(self):
    print(f"El perimetro del lado es: {(self.lado * 4)} y su superficie es: {(self.lado**2)}")


primerCuadrado = Cuadrado()
primerCuadrado.informacion()


"""3. Implementar la clase Operaciones. Se deben cargar dos valores enteros por teclado en el
método __init__, calcular su suma, resta, multiplicación y división, cada una en un método,
imprimir dichos resultados."""

print()
print("***_Calculadora_***")
print()
class Operaciones():
  def __init__(self):
    self.valor1 = int(input("Ingrese el primer numero: "))
    self.valor2 = int(input("Ingrese el segundo numero: "))
  
  
  def calcular(self):
      print(f"La suma de: {self.valor1} + {self.valor2} es: {self.valor1+self.valor2}" )
      print(f"La resta de: {self.valor1} - {self.valor2} es: {self.valor1-self.valor2}" )
      print(f"La multiplicacion de: {self.valor1} * {self.valor2} es: {self.valor1*self.valor2}" )
      print(f"La division de: {self.valor1} / {self.valor2} es: {(self.valor1/self.valor2):.2f}" )
    

objeto1 = Operaciones()
objeto1.calcular()


