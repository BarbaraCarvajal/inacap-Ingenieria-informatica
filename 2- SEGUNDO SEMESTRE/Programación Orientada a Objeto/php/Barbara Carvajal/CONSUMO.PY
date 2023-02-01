from urllib import request
import json

pagina = request.urlopen("http://localhost/phppython/retornardatos.php")
datos = pagina.read().decode("utf-8")

print(datos)
print("__"*100)

lista = json.loads(datos)
print(lista)

lista = json.loads(datos)
print(lista)

for x in lista:
    print(f"{x ['codigo']} {x['descripcion']:50} {x[descri]}")