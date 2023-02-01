lista = [1,2,4,3,3,"gato", "perro", 8, 10, 8, "perro", "pajaritos" ]

print(f"Lista original: {lista}")
nuevaLista = []
for x in lista:
    if x not in nuevaLista:
        nuevaLista.append(x)
print(nuevaLista)

# otra forma:

lista = [1,2,4,3,3,"gato", "perro", 8, 10, 8, "perro", "pajaritos" ]
print(lista)
conjunto = set(lista)
lista = list(conjunto)
print(lista)

# otra forma aún más corta
lista = [1,2,4,3,3,"gato", "perro", 8, 10, 8, "perro", "pajaritos" ]
print(lista)
lista = list(set(lista))
print(lista)

#-------------------------------------
lista1 = 1,4,5,7,8,9,"hola","miau"
lista2 = 1,3,5,6,3,10,"chao", "guau"

