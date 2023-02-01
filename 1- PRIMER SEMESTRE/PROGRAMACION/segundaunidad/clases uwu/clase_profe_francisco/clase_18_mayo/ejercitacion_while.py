
"""

sw = False
while not sw:
    salir = input("Desea continuar? (s/n)\n")
    respuesta=salir.lower()
    if respuesta =="s":
        sw= True 

"""


respuesta=True

while respuesta == True:
    respuesta= (input("Desea continuar?\n"))
    respuesta= respuesta.lower()
    print(f"RESPUESTA: {respuesta}")
    if respuesta == "s" or respuesta=="n":
        if respuesta == "s":
            respuesta=True
        else:
            print("Adiooooos")
    else:
        respuesta=True
        print("Ingrese s o n!!")

print("-----------------------------------------")
#otra opcion:
sw = False
while not sw:
    salir = input("Desea continuar? (S/N")
    rpta = salir.lower()
    print(rpta)
    if rpta != "s" and rpta !="n":
        print("Ingrese respuesta correcta")
        sw = False 
    elif rpta == "n":
        break
    else:
        sw = False
        