"""Un banco tiene 3 clientes que pueden 
hacer depósitos y extracciones. 
También el banco requiere que al final del día 
calcule la cantidad de dinero que hay depositado.
Lo primero que hacemos es identificar las clases:
Podemos identificar la clase Cliente y la clase Banco.
Luego debemos definir los atributos y los métodos de cada clase:"""

class cliente:

  def __init__(self,nombre,saldo):
    self.nombre = nombre
    self.saldo = saldo

  def depositar(self,deposito):
    self.deposito = deposito
    self.saldo = self.saldo + self.deposito
    print(f"Ud ha depositado: ${self.deposito} - Le quedan en su cuenta: ${self.saldo}")

  def retirar(self,retiro):
    self.retiro = retiro
    self.saldo = self.saldo - self.retiro
    print(f"Ud ha retirado: ${self.retiro} - Le quedan en su cuenta: ${self.saldo}")

  def saldoCliente(self):
    return self.saldo

class banco:
  def __init__(self):
    self.cliente1 = cliente("barb", 10000000)
    self.cliente2 = cliente("cami", 8500000)
    self.cliente3 = cliente("moki", 500000)

  def operar(self):
    self.cliente1.depositar(305000)
    self.cliente2.depositar(305000)
    self.cliente3.depositar(305000)
    self.cliente1.retirar(5000)
    self.cliente2.retirar(2500)
    self.cliente3.retirar(12999)
  
  def depositosTotales(self):
    total = self.cliente1.saldoCliente() + self.cliente2.saldoCliente() + self.cliente3.saldoCliente()
    print(f"Total saldo clientes en Banco: ${total}")

#banco1 = banco()
#banco1.operar()
#banco1.depositosTotales()

"""Problema 2:
Plantear un programa que permita jugar a los dados. 
Las reglas de juego son:
se tiran tres dados si los tres salen con el mismo 
valor mostrar un mensaje que "gano", sino "perdió".
Lo primero que hacemos es identificar las clases:
Podemos identificar la clase Dado y la clase 
JuegoDeDados. Luego los atributos y los métodos de cada clase:"""

import random
class Dados:
  
  
  def tirarDados(self):
    self.numero = random.randint(1,6)

  def mostrarNumero(self):
    print(f"El numero del dado es: {self.numero}")

  def retornarValorDado(self):
    return self.numero

class JuegoDeDados:
  def __init__(self):
    self.juego1 = Dados()
    self.juego2 = Dados()
    self.juego3 = Dados()

  def jugar(self):
    self.juego1.tirarDados()
    self.juego1.mostrarNumero()
    self.juego2.tirarDados()
    self.juego2.mostrarNumero()
    self.juego3.tirarDados()
    self.juego3.mostrarNumero()

  def resultado(self):
    if (self.juego1.retornarValorDado() == self.juego2.retornarValorDado()
     and self.juego1.retornarValorDado() == self.juego3.retornarValorDado()):
      print("Felicidades, haz ganado :D")
    else:
      print("Sigue participando :D")


#jugadera=JuegoDeDados()
#jugadera.jugar()
#jugadera.resultado()
"""
Plantear una clase Club y otra clase Socio.
La clase Socio debe tener los siguientes atributos: 
nombre y la antigüedad en el club (en años). 
En el método __init__ de la clase Socio pedir la carga 
por teclado del nombre y su antigüedad. La clase Club debe 
tener como atributos 3 objetos de la clase Socio.
Definir una responsabilidad para imprimir el nombre 
del socio con mayor antigüedad en el club."""

class Socio:
  def __init__(self):
    self.nombre = input("Ingrese su nombre: ")
    self.antiguedad = int(input("Ingrese su antiguedad en años: "))
  
  
class Club:
  def __init__(self):
    self.socio1 = Socio()
    self.socio2 = Socio()
    self.socio3 = Socio()

  def mayorAntiguedad(self):
    if self.socio1 > self.socio2 and self.socio1 > self.socio3:
      print(f"El socio de mayor edad es: {self.socio1}")
    elif self.socio2 > self.socio1 and self.socio2 > self.socio3:
      print(f"El socio de mayor edad es: {self.socio1}")
    elif self.socio3 > self.socio2 and self.socio3 > self.socio1:
      print(f"El socio de mayor edad es: {self.socio1}")
    else:
      print("Todos los socios tienen la misma cantidad de años en el club")

  def infoSocio(self):
      def __init__(self):
        print(f"Socio {self.nombre} tiene {self.antiguedad} años en el Club")


club1 =Club()
club1.mayorAntiguedad()
