import os
os.system("cls")
#1

cine = [
 ["X","X","X","0","0"],
 ["X","X","X","X","0"],
 ["X","0","X","0","X"],
 ["X","X","X","X","0"],
 ["0","0","X","0","0"],
]




def disponible (fila,columna,cine):
    if fila <= 5 and columna <= 5:
        for cine[0][fila] in cine:
            for columna in cine [0][fila]:
                if"0" in columna:
                    return True
                elif "x" in columna:
                    return False
def espacio(p,cine):
    disponible=0
    for x in range(len(cine)):
        for i in cine[x]:
            if i =="0":
                disponible +=1
    if disponible>= p:
        return True
    else:
        return False
fila=int(input("fila"))
columna=int(input("columna"))
p=input("")
cine=input("")
disponible(fila,columna,cine)
espacio(p,cine)


print()

#2

temp = {
    "Valparaíso": (9,28),
    "Quilpué": (10,24),
    "Villa Alemana":(7,30),
    "Los Andes": (5,22),
    "La Calera": (9,23),
    "Limache": (4,29),
 }


def informe_clima(fecha,temp):
    for x in range (1):
        print(f"Tiempo {fecha[0]}-{fecha[1]}-{fecha[2]}")

    for ciudad,temp in temp.items():
        if temp[1] > 27:
            print(f"{ciudad.upper()}: max{temp[1]} y min {temp[0]}")
        else:
            print(f"{ciudad}:max{temp[1]} y min {temp[0]}")

fecha=27,12,2021
informe_clima(fecha,temp)


    
print()


            
#3

def conteo_letras(texto):
    dic_vocales ={}
    for i in texto:
        dic_vocales[i] = 1
    return dic_vocales
                       

frase = input("Ingresa una frase: ")
def letras(frase):
    letras = {}
    for x in frase:
        if x not in letras:
            letras[x] = 1
        elif x == " ":
            del letras[x]
        else:
            letras[x] += 1
    print(letras)
    
letras(frase)
def vocales(frase):
    print(frase)
    vocales = {"a":0, "e":0, "i":0, "o":0, "u":0 }
    for x in frase:
        if x in vocales:
            vocales[x] += 1
    print(vocales)