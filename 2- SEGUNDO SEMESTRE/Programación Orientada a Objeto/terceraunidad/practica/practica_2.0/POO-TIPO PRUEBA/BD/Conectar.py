import mysql.connector
def Conexion():
    try:
        con=mysql.connector.connect(host="localhost",database="TipoPrueba",port="3306",username="root",password="Inacap2022")
        print("Conectado")
        return con
    except:
        print("Error de conexion")
     

Conexion()