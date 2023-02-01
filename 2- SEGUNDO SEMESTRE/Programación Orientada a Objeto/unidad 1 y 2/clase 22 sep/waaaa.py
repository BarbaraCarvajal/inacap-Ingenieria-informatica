
"""
Enunciado
AUTOMOTORA FIAT600
Confeccionar un diagrama de clases, considerando por cada clase: 
Considere crear las clases Auto, Moto, Camión
Crear dos objetos para cada clase
Aplicar herencia según corresponda
Aplicar encapsulación de atributos y visibilidad pública en los métodos
Atributos:
- Clase Auto: Id, marca, modelo, año, km/l(últimos 3 rendimientos), es híbrido?
- Clase Camión: Id, marca, modelo, año, km/l(últimos 3 rendimientos), toneladas
- Clase Moto: Id, marca, modelo, año, km/l(últimos 3 rendimientos),
cantidad de ruedas Cree 3 métodos comunes a las 3 clases y 3 diferenciadores por cada una.
Respete sintaxis estudiada"""

class Vehiculo:
  def __init__(self,id,marca,modelo,año, kmL = []):
    self.id = id
    self.marca = marca
    self.modelo = modelo
    self.año = año
    self.kmL = kmL

  def mostrarDatos(self):
    print(f"""
    ID:     {self.id}
    Marca:  {self.marca}
    Modelo: {self.modelo}
    Año:    {self.año}
    Km:     {self.kmL}""")


  def prender(self):
    print(f"{self.marca} encendido :D")

  def acelerar(self):
    print(f"{self.marca} esta acelerando su velocidad!")
  
  def apagar(self):
    print(f"{self.marca} apagado :D")

class Auto(Vehiculo):
  def __init__(self,hibrido):
    super().__init__(self,id,marca,modelo,año, kmL = []) 
    self.hibrido = False

  def mostrarDatos(self):
    super().mostrarDatos()
  
  def abrirMaletero(self):
    print(f"Maletero del auto {self.marca} abierto :D")
  
  def cerrarMaletero(self):
    print(f"Maletero del auto {self.marca} cerrado :D")
  
  def driftear(self):
    print(f"{self.marca} esta drifteando como un campeón ;D")

class camion(Vehiculo):
  def __init__(self):
    super().__init__(self)
    self.toneladas = toneladas
  
  def cargarCarga(self):
    print(f"El camión {self.marca} está cargando su pedido")
  
  def decargarCarga(self):
    print(f"El camión {self.marca} está descargando su pedido")
  
  def pesarCarga(self):
    peso = float(input("Ingrese el peso de la carga en toneladas"))
    print(f"La carga pesada es de: {peso}")

class moto(Vehiculo):
  def __init__(self):
    super().__init__(self)
    self.cantidadRuedas = cantidadRuedas

  def acelerarManualmente(self):
    print(f"Acelerando la moto {self.marca}")

  def hacerPirueta(self):
    print(f"{self.marca} hizo una grand pirueta :D")

  def activarFrenoMoto(self):
    print("Freno de moto activado")


#auto1 = Auto(3322, "kia", "kia rio", 2018, [100,250,500],False)

vehiculooo = Vehiculo(2222, "kia", "rio", 2015)
vehiculooo.acelerar()
vehiculooo.apagar()


