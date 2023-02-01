
import json
import requests
from urllib import request

pagina = request.urlopen(f"https://rickandmortyapi.com/api/character")
datos = pagina.read().decode("utf-8")

print("-"*100)

lista = json.loads((datos))
print(type(lista))

cadena2= json.dumps(lista) # dumps permire convertir una lista a string
print(type(cadena2))
print(cadena2)

print("-"*100)

identificador = int(input("Ingrese el id del personaje que desea ver: "))
url = f"https://rickandmortyapi.com/api/character/{identificador}"
r = requests.get(url)
j = r.json()

print(f"DATOS PRINCIPALES DE {j['name']}")
print(f"ID: {j['id']}")
print(f"NOMBRE: {j['name']}")
print(f"STATUS: {j['status']}")
print(f"GENDERO: {j['gender']}")
print(f"ORIGENES: {j['origin']['name']}")





