"""Problema 1:
Implementaremos una clase llamada Persona que tendrá 
como atributo (variable) su nombre y dos métodos (funciones), 
uno de dichos métodos inicializará el atributo nombre y 
el siguiente método mostrará en la pantalla el contenido del mismo.
Definir dos objetos de la clase Persona."""
import os
os.system("clear")


class Persona: 

  def inicializar(self,nom):
    self.nombre = nom
  
  def imprimir(self):
    print(f"Nombre: {self.nombre}")


#bloque principal

#persona1 = Persona()
#persona1.inicializar("Bárbara")
#persona1.imprimir()

#persona2 = Persona()
#persona2.inicializar("Camilo")
#persona2.imprimir()

###

"""Problema 2:
Definir una clase Cliente que almacene un 
código de cliente y un nombre.
En la clase Cliente definir una variable
 de clase de tipo lista que almacene todos 
 los clientes que tienen suspendidas sus cuentas corrientes.
Imprimir por pantalla todos los datos de clientes y
 el estado que se encuentra su cuenta corriente.
"""

class Cliente:
  suspendidos=[]

  def __init__ (self,nombre,codigo):
    self.nombre = nombre
    self.codigo = codigo
  
  def imprimir(self): 
    print("Codigo:",self.codigo) 
    print("Nombre:",self.nombre) 
    self.esta_suspendido()

  def esta_suspendido(self):
    if self.codigo in Cliente.suspendidos:
      print("Esta suspendido") 
    else:
      print("No esta suspendido") 
    print("_____________________________")

  def suspender(self): 
    Cliente.suspendidos.append(self.codigo)

cliente1 = Cliente("Barbarita", 1313)
cliente2=Cliente("Camilin",2343)
cliente3=Cliente("Diego",2322)
cliente4=Cliente("Pedro",3333)

cliente3.suspender() 
cliente4.suspender()
cliente1.imprimir() 
cliente2.imprimir() 
cliente3.imprimir() 
cliente4.imprimir()

print(Cliente.suspendidos)
##









  