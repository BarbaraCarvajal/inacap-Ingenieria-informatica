import mysql.connector

#funcion para que se conecte
def conexion():
    conexion1 = mysql.connector.connect(host = "localhost",
                                        user = "root",
                                        passwd = "",
                                        db = "inacap",
                                        )
    return conexion1

conexion()