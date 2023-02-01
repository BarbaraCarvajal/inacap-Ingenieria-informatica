import json
from urllib import request


pagina = request.urlopen("http://localhost/productos/productos.php")
datos = pagina.read().decode("utf-8")
print(datos)

print("_"*100)
lista = json.loads(datos) #convertimos el string a una lista
for x in lista:
  print(f"{x['codigo']} {x['descripcion']:25} {x['precio']}")