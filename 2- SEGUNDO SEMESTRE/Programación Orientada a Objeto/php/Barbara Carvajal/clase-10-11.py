# apis servicio pre existente 

import json

# ARCHIVO JSON
cadena = """
    [{
        "codigo" : "1",
        "descripcion": "Queso",
        "precio": "5000"
    },
    {
        "codigo" : "2",
        "descripcion": "Queso Cabra",
        "precio": "6500"
    }]

"""

#print(cadena)

listaDiccionario = json.loads(cadena)
#print(diccionario)

for x in listaDiccionario:
    print(x)


