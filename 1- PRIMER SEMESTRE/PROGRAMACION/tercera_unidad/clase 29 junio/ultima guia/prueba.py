import os
os.system("clear")


lista = []
for x in range(5):
    valores = input(f"{x+1}) Ingrese valores a la lista: ").lower()
    lista.append(valores)
    

def mostrarLista(lista):
    for x in lista:
        print(x,end="-")


def eliminar_valor(lista):
    print("Esta es la lista: ")
    mostrarLista(lista)
    print()
    valor = input("¿Qué valor desea eliminar?: ")
    lista.remove(valor)
    print(f"Lista actualizada: {lista}")





#mostrarLista(lista)
eliminar_valor(lista)