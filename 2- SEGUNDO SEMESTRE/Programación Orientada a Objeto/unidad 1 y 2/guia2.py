class Socio:
    def __init__(self):
        self.nombre = input("ingrese nombre: ")
        self.antiguedad = int(input("ingrese antiguedad"))
    
    def imprimir(self):
        print(f"{self.nombre} tiene una antiguedad de {self.antiguedad}")
    
    def retornarAntiguedad(self):
        return self.antiguedad

class Club:
    def __init__(self) :
        self.socio1 = Socio()
        self.socio2 = Socio()
        self.socio3 = Socio()
    
    def mayorAntiguedad(self):
        print("socio mayor antiguedad: ")
        if (self.socio1.retornarAntiguedad()>self.socio2.retornarAntiguedad() and self.socio1.retornarAntiguedad()>self.socio3.retornarAntiguedad()):
            self.socio1.imprimir()
        else:
            if (self.socio2.retornarAntiguedad()>self.socio3.retornarAntiguedad()):
                self.socio2.imprimir()
            
            else:
                self.socio3.imprimir()

#main
club = Club()
club.mayorAntiguedad()
        


