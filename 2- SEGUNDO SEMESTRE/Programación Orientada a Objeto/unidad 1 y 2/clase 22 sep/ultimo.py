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
  def __init__(self, id, marca, modelo, año, kmL = []):
    self.id = id
    self.marca = marca
    self.modelo = modelo
    self.año = año
    self.kmL = kmL
  
  def presentacion(self):
    print(f"""
Datos del Vehiculo
id: {self.id}
marca: {self.marca}
modelo: {self.modelo}
año: {self.año}
kmL: {self.kmL}""")
  def prenderVehiculo(self):
    print(f"El vehiculo {self.marca} esta encendido :D")

  def apagarVehiculo(self):
    print(f"El vehiculo {self.marca} esta apagado :D")

  def acelerarVehiculo(self):
    print(f"El vehiculo {self.marca} esta acelerando :D")

class Auto(Vehiculo):
  def __init__(self, id, marca, modelo, año, kmL, hibrido):
    super().__init__(id, marca, modelo, año,kmL)
    self.hibrido = hibrido

  def presentacion(self):
    super().presentacion()
    print(f"Hibrido: {self.hibrido}")
  
  def abrirMaletero(self):
    print(f"El maletero del auto {self.marca} esta abierto :D")

  def cerrarMaletero(self):
    print(f"El maletero del auto {self.marca} esta cerrado :D")

  def driftear(self):
    print(f"El auto {self.marca} esta drifteando como un campeon :p")

class Moto(Vehiculo):
  def __init__(self, id, marca, modelo, año, kmL, cantidadRuedas):
    super().__init__(id, marca, modelo, año,kmL)
    self.cantidadRuedas = cantidadRuedas

  def presentacion(self):
    super().presentacion()
    print(f"Cantidad de ruedas: {self.cantidadRuedas}")

  def acelerarManualmente(self):
    print(f"La moto {self.marca} esta acelerando :o")

  def activarFrenoMoto(self):
    print(f"La moto {self.marca} esta frenando :o")

  def hacerPirueta(self):
    print(f"La moto {self.marca} esta haciendo piruetas re locas :o")

class Camion(Vehiculo):
  def __init__(self,id, marca, modelo, año, kmL, toneladas):
    super().__init__(id, marca, modelo, año,kmL)
    self.toneladas = toneladas 
    
  def presentacion(self):
    super().presentacion()
    print(f"Toneladas: {self.toneladas}")

  def cargarCarga(self):
    print(f"El camion {self.marca} esta cargando su carga :D")    
  
  def descargarCarga(self):
    print(f"El camion {self.marca} esta descargando su carga :D")   

  def pesarToneladas(self):
    print(f"El camion {self.marca} esta pesando su carga")

  



print("Auto")
autito = Auto(2222, "tesla", "xxl", "2022", [0,0,0], True)
autito.presentacion()
autito.abrirMaletero()
autito.cerrarMaletero()
autito.driftear()
autito.acelerarVehiculo()
autito.prenderVehiculo()
autito.apagarVehiculo()
print()
print("Moto")
motito = Moto(1111, "susuki", "qseyo", 2022, [12,10,0], 2)
motito.presentacion()
motito.prenderVehiculo()
motito.apagarVehiculo()
motito.acelerarVehiculo()
motito.acelerarManualmente()
motito.activarFrenoMoto()
motito.hacerPirueta()
print()
print("Camion")
camioncito = Camion(3333, "cat", "wjaj", 2022, [0,0,0], 10)  
camioncito.presentacion()
