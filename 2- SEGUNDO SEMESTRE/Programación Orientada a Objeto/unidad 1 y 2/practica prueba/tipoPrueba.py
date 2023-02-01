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

import os
os.system("clear")

class Vehiculo:
  def __init__(self, id, marca, modelo, año, kml = []):
    self.id = id
    self.marca = marca
    self.modelo = modelo
    self.año = año
    self.kmL = kml

  def presentacion(self):
    print(f"""
INFORMACION DEL VEHICULO
id: {self.id}
marca: {self.marca}
modelo: {self.modelo}
año: {self.año}
kmL: {self.kmL}""")
  
  def prenderVehiculo(self):
    print("El vehiculo está encendido")

  def apagarVehiculo(self):
    print("El vehiculo está apagado")

  def acelerarVehiculo(self):
    print("El vehiculo está acelerando")

class Auto(Vehiculo):
  def __init__(self, id, marca, modelo, año, kml, hibrido):
    super().__init__(id, marca, modelo, año, kml)
    self.hibrido = hibrido
  
  def presentacion(self):
    super().presentacion()
    print(f"Hibrido: {self.hibrido}")

  def abrirMaletero(self):
    print("El maletero esta abierto")

  def cerrarMaletero(self):
    print("El maletero esta cerrado")

  def driftear(self):
    print(f"{self.marca} esta drifteando como un campeon :D")


class Camion(Vehiculo):
  def __init__(self, id, marca, modelo, año, toneladas, kmL):
    super().__init__(id, marca, modelo, año, kmL)
    self.toneladas = toneladas

  def presentacion(self):
    super().presentacion()
    print(f"Toneladas: {self.toneladas}")
  
  def cargarCarga(self):
    print(f"El camion {self.marca} esta cargando carga")
  
  def descargarCarga(self):
    print(f"El camion {self.marca} esta descargando su carga")

  def pesarToneladas(self):
    print(f"El camion {self.marca} esta pesando su carga")

class Moto(Vehiculo):
  def __init__(self, id, marca, modelo, año, kmL,cantidadRuedas):
    super().__init__(id, marca, modelo, año,kmL)
    self.cantidadRuedas = cantidadRuedas

  def acelerarManualmente(self):
    print(f"Acelerando manualmente la moto {self.marca}")
  
  def hacerPirueta(self):
    print(f"La moto {self.marca} esta haciendo la media pirueta!")

  def activarFrenoMoto(self):
    print(f"Freno de moto activado")

  def presentacion(self):
    super().presentacion()
    print(f"Cantidad de ruedas: {self.cantidadRuedas}")

### creacion objeto auto
auto2 = Auto(2223, "toyota", "4x4", 2018, [200,300,400], True)
auto2.presentacion()
print("Metodos:")
auto2.abrirMaletero()
auto2.cerrarMaletero()
auto2.driftear()
auto2.prenderVehiculo()
auto2.acelerarVehiculo()
auto2.apagarVehiculo()
print()
### creacion objeto camion

camion1 = Camion(8888, "Mercedes", "20x20", 2020 , 10 ,[100,200,220])
camion1.presentacion()
print("Metodos:")
camion1.prenderVehiculo()
camion1.apagarVehiculo()
camion1.acelerarVehiculo()
camion1.cargarCarga()
camion1.descargarCarga()
camion1.pesarToneladas()

## creacion objeto moto
moto1 = Moto(3333, "honda", "qsy", 2012, [200,300,210], 2)
moto1.presentacion()
print("Metodos:")
moto1.acelerarVehiculo()
moto1.prenderVehiculo()
moto1.apagarVehiculo()
moto1.acelerarManualmente()
moto1.hacerPirueta()
moto1.activarFrenoMoto()
