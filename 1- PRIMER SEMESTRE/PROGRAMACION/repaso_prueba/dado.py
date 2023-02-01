import os, time
os.system("clear")
from random import randint as aleatorio

print("Tirar dado...")
for x in range(1,4):
    print(x)
    time.sleep(0.5)

tirar_dado = aleatorio(1, 6)
print("El dado ha sido lanzado")

sw = True
while sw == True:
    num = int(input("¿Qué número es?\n"))
    if num == tirar_dado:
        print("Felicidades! Sí es el número!!")
        sw = False
    elif num > tirar_dado:
        print("El número es menor...")
    elif num < tirar_dado:
        print("El número es mayor...")
    
        
