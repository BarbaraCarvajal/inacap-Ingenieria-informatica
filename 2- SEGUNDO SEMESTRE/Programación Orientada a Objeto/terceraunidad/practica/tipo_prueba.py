"""Enunciado
Ensayo Evaluación II
Confeccionar una clase que administre una empresa de Automóviles. 
Se debe almacenar:
Marca, Modelo, número de chasis (encriptado), cilindrado, precio
Debe mostrar un menú con las siguientes opciones: 
- Agregar datos - Mostrar Datos - Consulta datos según el número de chasis
Eliminar registro según número de chasis - Finalizar programa.
Utilice el paradigma orientado a objetos y conecte a BD MySql 
FORMATO DE ENTREGA
Script en Python
Script de BDpt de BD"""

import mysql.connector

class Auto:
    def __init__(self):
        self.marca = input("Ingrese la marca del auto: ")
        self.modelo = input("Ingrese el modelo del auto: ")
        self.chasis = int(input("Ingresse el numero de chasis: "))
        self.cilindrado = int(input(f"Ingrese el cilindrado del {self.marca}"))
        self.precio = int(input(f"Ingrese el precio del auto {self.marca}"))

    def conexion(self):

        self.conexion1 = mysql.connector.connect(host="localhost", 
                                        user="root", 
                                        passwd="", 
                                        database= "practicaPrueba",
                                        port="8080" ) 
        #cursor1 = conexion1.cursor()

    def agregarAuto(self):
        
        print("AGREGAR AUTO")
        cursor1 = self.conexion1.cursor()
        sql = "insert into automovilesPrueba(marca, modelo, chasis, cilindrado, precio) values (%s, %s. %s, %s, %s)"
        datos = (self.marca, self.modelo, self.chasis, self.cilindrado, self.precio)
        cursor1.execute(sql,datos)
        self.conexion1.commit()
        self.conexion1.close()
        
        print("Auto agregado con exito.")

auto1 = Auto()
auto1.agregarAuto()

"""def __init__(self, marca,modelo,chasis,cilindrado, precio):
            super().__init__(marca,modelo,chasis,cilindrado, precio)
    """