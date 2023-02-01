from random import randint
import os
#os.system("clear") #mac
os.system("cls") #windows


# 2- LLenar una lista de 10 posiciones con números aleatorios entre 1 y 100, como 
# salida debe mostrar los números aleatorios del arreglo ordenados de menor a mayor. 

numeros_aleatorios = [] # Inicializamos la lista vacia

#luego la llenamos con valores: 
for x in range(1,11):
    azar= randint(1,100) # creamos una variable donde agregaremos valores de forma aleatoria
    numeros_aleatorios.append(azar) #usamos la función "append" que va agregando valores al final de la lista

print(f"Lista de numeros al azar: {numeros_aleatorios}")
numeros_aleatorios.sort() # acá ordenamos la lista con ".sort()"
print(f"Lista ordenada de menor a mayor: {numeros_aleatorios}") # y acá la imprimimos ya ordenada
