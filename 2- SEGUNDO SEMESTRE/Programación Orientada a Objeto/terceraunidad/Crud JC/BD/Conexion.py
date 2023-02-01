import mysql.connector

class DAO():
    def __init__(self):
        self.conexion=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            db = "empresa")

    def mostrarDatos(self):
        cursor = self.conexion.cursor()
        cursor.execute("select * from auto")
        resultados = cursor.fetchall()
        return resultados

    def ingresarDatos(self, auto):
        cursor = self.conexion.cursor()
        sql = "insert into auto (id, chasis, marca, modelo, cilindraje, precio) values ({0}, '{1}', '{2}', '{3}', {4}, {5})"
        cursor.execute(sql.format(auto[0], auto[1], auto[2], auto[3], auto[4], auto[5]))
        self.conexion.commit()
        print("\nAuto ingresado correctamente.")
        print()

    def borrarDatos(self, idEliminar):
        cursor = self.conexion.cursor()
        sql = "delete from auto where id = {0}"
        cursor.execute(sql.format(idEliminar))
        self.conexion.commit()
        print("\nAuto eliminado correctamente")
        print()
    
    def modificarDatos(self, auto):
        cursor = self.conexion.cursor()
        sql = "update auto set id = {0}, chasis = '{1}', marca = '{2}', modelo = '{3}', cilindraje = {4}, precio = {5}  where id = {0} "
        cursor.execute(sql.format(auto[0], auto[1], auto[2], auto[3], auto[4], auto[5]))
        self.conexion.commit()
        print("\nAuto modificado correctamente")
        print()
    
    def consultarDatos(self, idConsultar):
        cursor = self.conexion.cursor()
        sql = "select * from auto where id = {0}"
        cursor.execute(sql.format(idConsultar))
        for auto in cursor:
            print(f"\nID: {auto[0]} | Chasis: {auto[1]} | Marca: {auto[2]} | Modelo: {auto[3]} | Cilindraje(cc) {auto[4]} | Precio($) : {auto[5]}")
