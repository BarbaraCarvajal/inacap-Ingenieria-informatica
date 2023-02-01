# serialización: convertir un objeto de python (lista,tupla,diccionario) en un string 

# deserialiazación: convertir un string en un objeto de python (lista, tupls, diccionario)

import json

cadena = """
  [
    {
      "codigo": "1",
      "descripcion": "papas",
      "precio": "12"
    },
    {
      "codigo": "2",
      "descripcion": "queso cabra",
      "precio": "5000"
    }
  ]

"""

print(type(cadena))
print(cadena)
print("-"*120)
lista = json.loads((cadena)) # loads permite deserializar el string 
print(type(lista))
print(lista)
print("-"*120)
cadena2= json.dumps(lista) # dumps permire convertir una lista a string
print(type(cadena2))
print(cadena2)

