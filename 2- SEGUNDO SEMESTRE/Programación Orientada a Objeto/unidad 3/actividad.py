import json
from urllib import request

pagina = request.urlopen("https://rickandmortyapi.com/api/character/2")
datos = pagina.read().decode("utf-8")

print("-"*100)
lista = json.loads((datos))
print(type(lista))
print("-"*100)

for i in lista:
  print(i)
"""
consulta = input("Ingrese el nombre por el cuál quiere consultar: ").capitalize()
for x in lista:
  if (x['username']) == consulta:
    print("ID: ",x['id'])
    print("NAME: ",x['name'])
    print("USERNAME: ",x['email'])
    print("STREET: ",x['address']['street'])
    print("SUITE: ",x['address']['suite'])
    print("CITY: ",x['address']['city'])
    print("ZIPCODE: ",x['address']['zipcode'])
    print("LAT: ",x['address']['geo']['lat'])
    print("LNG: ",x['address']['geo']['lng'])
    print("phone:",x['phone'])
    print("website:",x['website'])
    print("company name:",x['company']['name'])
    print("catchPhrase:",x['company']['catchPhrase'])
    print("bs:",x['company']['bs'])
    print()
    
    

   
    
"""