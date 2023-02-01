import os
os.system("cls")

# Escribir un programa que guarde en una variable el diccionario
# euro: €"dolar": "$","yen": "¥", y pregunte al usuario por una 
# divisa y muestre su simbolo o un mensaje de aviso si la divisa
#no esta en el diccionario
        

def divisas():
    divisas = {
        "euro": "€",
        "dolar": "$",
        "yen": "¥"
    }

    sw = True
    while sw == True:

        moneda = input("Escribe una divisa: ").lower()

        if divisas.get(moneda):#True or false para saber si esta o no
            print(f"El simbolo de {moneda} es: {(divisas.get(moneda))}")
            sw = False
        else:
            print("La divisa ingresada no se encuentra")
divisas()

# Escribir un programa que pregunte al usuario su nombre, edad,
# direccion y telefono, y lo guarde en un diccionario. Después 
# debe mostrar por pantalla el mensaje <nombre> tiene <edad>, 
# vive en <direccion> y su numero de telefono es <telefono>

def creacion_diccionario():

    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    direccion = input("Ingresa tu dirección: ")
    telefono = input("Ingresa tu telefono: ")

    datos_usuarios = {
        "nombre": nombre,
        "edad": edad,
        "direccion": direccion,
        "telefono": telefono
    }
    print(f"""
{datos_usuarios["nombre"]} 
tiene {datos_usuarios["edad"]} años
vive en {datos_usuarios["direccion"]}
y su numero telefonico es: {datos_usuarios["telefono"]}
""")

#creacion_diccionario()

# Escribir un programa que guarde en un diccionario los precios
# de las frutas de la tabla, pregunte al usuario por una fruta, 
# un numero de kilos y muestre por pantalla el precio de ese
# número de kilos de fruta. Si la fruta no está en el 
# diccionario debe mostrar un mensaje infomando de ello.
"""
fruta precio
platano 980
manzana 500
pera 650
"""

def venta_frutas():

    frutas ={
        "platano": 980,
        "manzana": 500,
        "pera": 650    
    }

    sw = True
    while sw == True:
        pedir_usuario = input("Ingrese el producto a consultar: ").lower()

        if pedir_usuario in frutas:
            kilos = float(input(("Ingrese  los kilos: ")))
            print(f"Valor de {pedir_usuario} ${frutas[pedir_usuario]*kilos}")
            sw = False
        else:
            print(f"No disponemos de {pedir_usuario}, vuelva a intentarlo.")
#venta_frutas()

# Escribir un programa que pregunte una fecha en formato 
# dd/mm/aaaa y muestre por pantalla la misma fecha en formato de
# dd de <mes> de aaaa donde <mes> es el nombre del mes.
def fechas ():
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }

    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))

    if mes in meses:
        print(f"Fecha: {dia}/{meses[mes]}/{año}")
#fechas()

# Escribir un programa que almacene el diccionario con los créditos
# de las asignaturas de un curso {"Matematicas":6, "Fisica":4,
# "Quimica":5} y despues muestre por pantalla los créditos de cada
# asignatura en formato <asignatura> tiene <creditos> créditos,
# donde <asignatura> es cada una de las asignaturas del curso,
#  y <creditos> son sus creditos. Al final debe mostrar también
# el numero total de crditos del curso.

def asignaturas():
    creditos = {
        "matematicas": 6,
        "fisica": 4,
        "quimica": 5
    }

    for x in creditos:
        print(f"La asignatura {x} tiene {creditos[x]} creditos")
#asignaturas()