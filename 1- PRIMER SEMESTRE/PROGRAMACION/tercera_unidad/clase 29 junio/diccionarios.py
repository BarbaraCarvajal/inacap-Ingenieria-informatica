import os
os.system("clear")

laboratorios = {
    "lab1": 204,
    "lab2": 205,
    "lab3": 208
}

telefonos = {
    "pancho": 95552437,
    "javier": 9551428,
    "sandra": 95550012
}

x = telefonos
print(x)
x = list(telefonos)
b = list(telefonos.values())
c = list(telefonos.keys())
d = list(telefonos.items())# los tira como lista de tuplas
print(x)
print(b)
print(c)
print(d)

print(telefonos.items())
print(telefonos.keys())
print(telefonos.values())


print(laboratorios)

#x = input("usuario: ").lower()
#print(telefonos[x])

#x= telefonos.get("pancho")
#print(x)

print(telefonos)
telefonos["claudia"] = 9345333
print(telefonos)
telefonos["pancho"] = 123413
print(telefonos)
"""x = input("Usuario: ")
y = input("Telefono: ")

telefonos[x] = y
print(telefonos)

x = input("Ingrese un usuario: ")
print(f"El telefono de {x} es {telefonos[x]}")"""


x = input("Elimine un usuario: ")
del telefonos[x]
print(telefonos)