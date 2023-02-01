import mysql.connector,hashlib
#conexion
class conexion:
    def __init__(self):
        self.conexion1 = mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="",
                                        database="bd1")
        self.cursor1 = self.conexion1.cursor()
    def close(self):
        self.conexion1.close()

#clase automoviles
class automoviles:
    def __init__(self):
        self.conexion1 = mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="",
                                        database="automoviles")
        self.cursor1 = self.conexion1.cursor()

    def agregar_datos(self):
        x = int(input("cuantos automoviles quiere ingresar: "))
        for i in range (x):
            print(f"auto n°{i+1}")
            chasis=input("ingrese el numero de chasis del automovil: ")
            marca= input("ingrese marca del automovil: ")
            modelo = input("ingrese modelo del automovil: ")
            cilindrado = input("ingrese cilindrado del automovil: ")
            precio=int(input("ingrese precio: $"))
            sql = "insert into autos (numero_chasis,marca,modelo,precio,cilindrado) values (%s,%s,%s,%s,%s)"
            datos =(chasis,marca,modelo,precio,cilindrado)
            self.cursor1.execute(sql,datos)
        self.conexion1.commit()

    def mostrar_datos(self):
        self.cursor1.execute("select * from autos")
        for tabla in self.cursor1:
            print(tabla)
    
    def consultar_datos(self):
        chasis=input("ingrese n° correspondiente a su automovil: ")
        dato=(chasis,)
        sql="select * from autos where numero_chasis = %s "
        self.cursor1.execute(sql,dato)
        self.conexion1.commit()
        
    #def modificar_datos(self):

    # def eliminar_registro(self):
    
    # def finalizar_programa(self):
    def close(self):
        self.conexion1.close()

datos1 = automoviles()

# datos1.agregar_datos()
# datos1.mostrar_datos()
datos1.consultar_datos()
datos1.close()