import os 
os.system("clear")



cosas = ("amarillo", 34, "kawaii", ("lol", 13))
for x in cosas:
    print(x)



"""

tupla = ("auto", 34, "casa")
print(tupla)
print(type(tupla))

print(tupla[1])
print(tupla[1:3])




frutas = ("manzana", "plátano", "frambuesa")
print(frutas)
print(type(frutas))
y = list(frutas)
print(type(frutas))
y[1] = "frutilla"
print(type(frutas))
x = tuple(y)
print(x) # o frutas
print(type(x))


cosas = ("casa", "auto", "avion", "manzana", "gato", "perrito", "platano")

#print(cosas[2:5])
indice1 = int(input("Indice 1: "))
indice2 = int(input("Indice 2: "))
print(cosas[indice1:indice2])





cod = int(input("ingrese un codigo: "))
prod = str(input("Ingrese un producto: "))
pre = int(input("Ingrese precio: "))
stock = (cod,prod,pre)
print(stock)
print(type(stock))



palabras = ("casa", "auto", "avion")
v1,v2,v3 = palabras
print(v1)
if "auto" in palabras:
    print("si, 'auto' está en la tupla palabras")


x = input("consulta: ")
if x in palabras:
    print(f"{x} si esta en la tupla")
else:
    print(f"{x} no esta en la tupla")

"""