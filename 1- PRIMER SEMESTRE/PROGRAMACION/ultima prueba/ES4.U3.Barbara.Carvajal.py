import os
from posixpath import split
os.system("clear")

"""1. (20 puntos) La siguiente Lista representa los asientos de una sala de cine, donde “0” indica asiento
disponible y “X” asiento ocupado.
cine = [
 ["X","X","X","0","0"],
 ["X","X","X","X","0"],
 ["X","0","X","0","X"],
 ["X","X","X","X","0"],
 ["0","0","X","0","0"],
]
Escriba las siguientes funciones, para obtener:
- disponible(fila,columna,cine) #Recibe la sala del cine y debe retornar True si el asiento de
la fila y columna (ingresados por teclado) está disponible y False en caso contrario. Si se
ingresa una fila o columna que no existen deberá retornar “Fila no existe” o “Columna no
existe”.
- espacio(p,cine) #Recibe un entero con la cantidad de personas que quieren ver una
película (puede ser variable esa cantidad) y la sala del cine; debe retornar True si hay
espacio suficiente para todos o False en caso contrario.
"""
"""
def asientos_disponibles(cine):
    for x in cine:
        if "0" in x:
            return print(True)
        else:
            return print(False)

"""
def disponible(fila,columna,cine):
    if fila <= 5  and columna <= 5:
        for cine[0][fila] in cine:
            for columna in cine[0][fila]:
                if "0" in columna:
                    return True
                elif "X" in columna:
                    return False
    else:
        return("Fila no existe")       
   
def espacio(p,cine):
    disponible = 0
    for x in range(len(cine)):
        for i in cine[x]:
            if i == "0":
                disponible += 1
    if disponible >= p:
        return True
    else:
        return False

cine = [
 ["X","X","X","0","0"],
 ["X","X","X","X","0"],
 ["X","0","X","0","X"],
 ["X","X","X","X","0"],
 ["0","0","X","0","0"],
]

print("Ejercicio #1")
fila = int(input("Ingrese la Fila: "))
columna = int(input("Ingrese la Columna: "))
print(disponible(fila,columna,cine))
print()
p= int(input("¿Cuántas entradas desea? "))
print(espacio(p,cine))
print()


"""2. (30 puntos) El siguiente Diccionario “temp” contiene las temperaturas máximas y mínimas de
algunas ciudades de la V Región. Las claves son las ciudades y los valores son Tuplas de las
temperaturas (mínima, máxima).
temp = {
“Valparaíso”: (9,28),
“Quilpué”: (10,24),
“Villa Alemana”:(7,30),
“Los Andes”: (5,22),
“La Calera”: (9,23),
“Limache”: (4,29),
 }
Escriba la función informe_clima((27,07,2021), temperatura), que reciba como parámetros la
fecha de hoy (en forma de Tupla) y el Diccionario de temperaturas. La función debe imprimir
como resultado un informe del tiempo con la fecha de hoy y deben aparecer en mayúsculas las
ciudades en que la temperatura máxima fue superior a 27."""

# ciudad, minimo, maximo
temp = {
    "Valparaíso":       (9,28), 
    "Quilpué":          (10,24),
    "Villa Alemana":    (7,30),
    "Los Andes":        (5,22),
    "La Calera":        (9,23),
    "Limache":          (4,29),
 }
def informe_clima(fecha, temp):
    for x in range(1):
       print(f"Informe del tiempo: {fecha[0]}-{fecha[1]}-{fecha[2]}")
        
    for ciudad, temperaturas in temp.items():
        if temperaturas[1] > 27:
            print(f"{ciudad.upper()}: max {temperaturas[1]} y min {temperaturas[0]}")
        else:
            print(f"{ciudad}: max {temperaturas[1]} y min {temperaturas[0]}")

fecha = (13,10,2022)
print("Ejercicio #2")
print()
informe_clima(fecha,temp)
print()

""" 3. (20 puntos) Escriba la función cuenta(frase), 
que retorne un diccionario con las vocales y la
cantidad de veces que aparecen en una frase, 
además imprimir el total de palabras que contiene
la frase. Debe considerar lo siguiente:
 La frase debe ser ingresa por el usuario.
 Las apariciones en mayúsculas como en minúsculas de las vocales.
 No tomar en cuenta las vocales con tilde y si la vocal no aparece debe estar de igual manera
en el diccionario con valor cero."""


def cuenta(frase):
    diccionario = {"a":0, "e":0, "i":0, "o": 0, "u":0}
    
    for x in frase.lower():
        if x in diccionario:
            diccionario[x] += 1
    contarPalabra = frase.split()    
    print(f"Cantidad de palabras en la frase: '{frase}': {len(contarPalabra)}")
    print(diccionario)


print("Ejercicio #3 ")
frase = input("Ingrese una frase: ")
cuenta(frase)

