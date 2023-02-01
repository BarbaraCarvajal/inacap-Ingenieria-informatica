


class Conexion:
    def __init__(self, conexion1):
        conexion1 = mysql.connector.connect(host="localhost",user="root",passwd="",database="basededatos1")
        return conexion1

class verTablas(Conexion):
    def __init__(self, conexion1,)

