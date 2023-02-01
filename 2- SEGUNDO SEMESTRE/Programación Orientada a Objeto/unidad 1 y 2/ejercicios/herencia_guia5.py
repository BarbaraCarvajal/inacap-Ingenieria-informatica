"""1. Declarar una clase Cuenta y dos subclases CajaAhorra 
y PlazoFijo. Definir los atributos y métodos comunes entre 
una caja de ahorro y un plazo fijo y agruparlos en la clase Cuenta. 
Una caja de ahorro y un plazo fijo tienen un nombre de titular y un monto. 
Un plazo fijo añade un plazo de imposición en días y una tasa de interés. 
Hacer que la caja de ahorro no genera intereses.
En el bloque principal del programa definir un objeto de la clase 
CajaAhorro y otro de la clase PlazoFijo.
"""




class Cuenta:

  def __init__(self,nombre, monto):
    self.nombre = nombre
    self.monto = monto
  
  def imprimir(self):
    print(f"Cliente: {self.nombre} Dinero en cuenta: ${self.monto}")
  

class CajaAhorro(Cuenta):
  def __init__(self, nombre, monto):
    super().__init__(nombre, monto) 

  def imprimir(self):
    print("Cuenta de caja de ahorro")
    super().imprimir()
  
class PlazoFijo(Cuenta):

  def __init__(self, nombre, monto, plazo, intereses):
    super().__init__(nombre, monto)
    self.plazo = plazo
    self.intereses = intereses
  
  def imprimir(self):
    print("Plazo Fijo")
    super().imprimir()
    print(f"Plazo: {self.plazo}")
    print(f"Intereses: {self.intereses}")
    self.ganancia_de_los_intereses()

  def ganancia_de_los_intereses(self):
    ganancias = self.monto * self.intereses / 100
    print(f"Interes: {ganancias}")

# bloque principal

cajaAhorro1 = CajaAhorro("Barbarita", 5500)
cajaAhorro1.imprimir()

plazofijo1 = PlazoFijo("Mokita", 85990, 25, 0.50)
plazofijo1.imprimir()


  
"""2. Plantear una clase llamada Jugador.
Definir en la clase Jugador los atributos nombre y puntaje, 
y los métodos __init__, imprimir y pasar_tiempo 
(que debe reducir en uno la variable de clase).
Declarar dentro de la clase Jugador una variable de 
clase que indique cuantos minutos falta para el fin de juego 
(iniciarla con el valor 30)
Definir en el bloque principal dos objetos de la clase Jugador.
Reducir dicha variable hasta llegar a cero."""


class Jugador:
    tiempo=30

    def __init__(self, nombre, puntaje):
        self.nombre=nombre
        self.puntaje=puntaje

    def imprimirInfo(self):
        print(f"Nombre: {self.nombre}")
        print(f"Puntaje: {self.puntaje}")
        print(f"Se acaba el juego en {Jugador.tiempo} minutos")

    def pasar_minuto(self):
        Jugador.tiempo=Jugador.tiempo-1


# bloque principal

jugador1=Jugador("Mokita",150)
jugador2=Jugador("Lattechito",80)
while Jugador.tiempo>0:
    jugador1.imprimirInfo()
    jugador2.imprimirInfo()
    jugador1.pasar_minuto()