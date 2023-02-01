
"""
1. Plantear una clase Club y otra clase Socio.
La clase Socio debe tener los siguientes atributos: nombre y la antigüedad en el club (en 
años).
En el método __init__ de la clase Socio pedir la carga por teclado del nombre y su 
antigüedad.
La clase Club debe tener como atributos 3 objetos de la clase Socio.
Definir una responsabilidad para imprimir el nombre del socio con mayor antigüedad en el 
club."""

class Socio:
    def __init__ (self):
        self.nombre = input("Ingrese el nombre del socio: ")
        self.años = int(input("Ingrese la antigüedad en años del socio: "))
    
    def mostrarDatos(self):
        print(f"Socio {self.nombre} tiene {self.años} años de antiguedad como socio.")

    def mostrarAntiguedad(self):
        return self.años

class Club:
    def __init__(self):
        self.socio1 = Socio()
        self.socio2 = Socio()
        self.socio3 = Socio()

    def mayorAntiguedad(self):
        if self.socio1.mostrarAntiguedad() > self.socio2.mostrarAntiguedad() and self.socio1.mostrarAntiguedad() > self.socio3.mostrarAntiguedad():
            return f"{self.socio1.mostrarDatos()} por ende, es el de mayor antiguedad!"
        elif self.socio2.mostrarAntiguedad() > self.socio1.mostrarAntiguedad() and self.socio2.mostrarAntiguedad() > self.socio3.mostrarAntiguedad():
            return f"{self.socio2.mostrarDatos()} por ende, es el de mayor antiguedad!"
        elif self.socio3.mostrarAntiguedad() > self.socio2.mostrarAntiguedad() and self.socio3.mostrarAntiguedad() > self.socio1.mostrarAntiguedad():
            return f"{self.socio3.mostrarDatos()} por ende, es el de mayor antiguedad!"

        else:
            print(f"{self.socio1.nombre}, {self.socio2.nombre} y {self.socio3.nombre} tienen la misma cantidad de años de experiencia! :D")
        

club = Club()
club.mayorAntiguedad()