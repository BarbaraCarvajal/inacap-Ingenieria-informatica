# 1. A partir de su serie/película o temática favorita, 
# busque listado Json para ser consumido datos desde la url respectiva: 
# 2. Desde Python desplegar en modo lista los registros recuperados mostrando todos los datos.
# 3. Retornar el registro correspondiente a partir de la captura por teclado de un Id,  
# nombre o username a elección


import json
from urllib import request
import requests #instalar request en la terminal: pip install requests



        

def lista():
    pagina = request.urlopen(f"https://rickandmortyapi.com/api/character")
    datos = pagina.read().decode("utf-8")

    print("-"*100)
    lista = json.loads((datos))
    print(type(lista))
    print(lista)
    print("-"*100)
    

#consultas
def id_consulta():
    id_dado = int(input("Ingrese el id por el cual quiere consultar [1 al 827] : "))
    url_api = f"https://rickandmortyapi.com/api/character/{id_dado}"
    r =requests.get(url_api)
    j = r.json()
    
    print()
    print(f"Datos de {j['name']}")
    print(f"ID: {j['id']}")
    print(f"NOMBRE: {j['name']}")
    print(f"STATUS: {j['status']}")
    print(f"GENDERO: {j['gender']}")
    print(f"ORIGENES: {j['origin']['name']}")
    

        
def menu():
    
    while True:
        print()
        print("MENU")   
        print("OPCION 1 = VER JSON EN FORMATO LISTA")
        print("OPCION 2 = CONSULTAR POR ID DE PERSONAJE")
        print("OPCION 3 = SALIR")
        print()
        opcion = int(input("Ingrese su opción: "))
        if opcion == 1:
            lista()
        elif opcion == 2:
            id_consulta()
        elif opcion == 3:
            print("Hasta luego :D")
            break

    
menu()