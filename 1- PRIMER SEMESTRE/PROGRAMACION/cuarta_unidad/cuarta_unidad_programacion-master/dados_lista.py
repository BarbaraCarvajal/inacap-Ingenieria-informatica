import os as limpiar
limpiar.system("clear")
#import msvcrt as esperar_tecla
from random import randint as azar

suman_10 = 0
suma = 0
lista_dado1 = []
lista_dado2 = []

#inicio ciclo for
print("Presione una tecla para lanzar dado...")
#esperar_tecla.getch()
for x in range(1,11):
    dado1 = azar(1,6)
    dado2 = azar(1,6)
    print(f"Lanzamiento {x}: ")
    print(f"dado 1: {dado1}")
    print(f"dado 2: {dado2}")
    lista_dado1.append(dado1)
    lista_dado2.append(dado2)
    suma = dado1 + dado2
    if suma == 10:
        suman_10 = suman_10 +1
    for x in range(lista_dado1):
        if suma == 10:
            
print(f"Veces en que los dados sumaron 10: {suman_10}")


