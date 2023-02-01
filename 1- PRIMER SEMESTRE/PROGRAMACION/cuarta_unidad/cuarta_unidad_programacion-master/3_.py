# 3- Almacene nombres en una lista de n posiciones. Una vez completada
# la lista, implementar una opción que al ingresar una posición
# muestre el dato que contiene. 

import os
os.system("clear") #mac
#os.system("cls") #windows




nombres = []

pregunta = int(input("¿Cuántos nombres ingresará?: "))
for x in range(1,pregunta+1):
    agregar = input(f"{x}: Ingrese un nombre: ")
    nombres.append(agregar)
    #print(nombres) #para comprobar que se agregaron bien los nombres
sw = True
while sw == True:
    posicion = int(input("Ingrese la posición que desea ver: "))
    if posicion in range(len(nombres)):
        print(f"En la posición {posicion} esta: {nombres[posicion-1]}")
        sw = False
    elif posicion != len(nombres):
        print("Ingresó una posición fuera del rango de la lista")

# dentro de los corchetes lo que hicimos fue lo mismo que por ejemplo poner:
# nombres[1] 1 seria la posición que queremos mostrar, en este caso dicha 
# posición la estamos consultando por teclado. 

