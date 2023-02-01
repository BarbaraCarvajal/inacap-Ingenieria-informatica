import mysql.connector

def conexion():
    conexion1=mysql.connector.connect(user="root",password="",database="inacap",host="localhost",port="3306")
    print("conecto")
    return conexion1

conexion()