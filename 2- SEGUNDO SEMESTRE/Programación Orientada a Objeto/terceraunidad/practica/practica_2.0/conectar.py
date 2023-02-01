import mysql.connector

def conexion():
    conexion1 = mysql.connector.connect(host = "localhost",
                                                user = "root",
                                                passwd = "",
                                                db = "colegio1")
    return conexion1

conexion()