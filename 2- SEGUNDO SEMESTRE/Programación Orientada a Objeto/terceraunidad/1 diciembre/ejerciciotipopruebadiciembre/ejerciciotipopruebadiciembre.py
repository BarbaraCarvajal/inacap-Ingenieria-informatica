import json
from urllib import request

sitio=request.urlopen("http://api.tvmaze.com/search/shows?q=golden%20girls")
datos= sitio.read().decode("utf-8")
lista = json.loads(datos)
#print(lista)
def imprimirlista(lista):
    for i in lista:
        print("ID:    " ,i['show']['id'])
        print("NOMBRE:" ,i['show']['name'])
        print("URL:   " ,i['show']['url'])
        print("LENGUAJE",i['show']['language'])
        print('*'*50)


    
    

def consultarlista(lista):
    consulta = input('Ingrese el username:  ')
    print('*'*30)
    for a in lista:
        if consulta == a['show']['name']:
            print("ID:    " ,a['show']['id'])
            print("NOMBRE:" ,a['show']['name'])
            print("URL:   " ,a['show']['url'])
            print("LENGUAJE",a['show']['language'])
            print('*'*30)
    else:
        print("-"*20)
        print(" EL DATO NO EXISTE ")
        print("-"*20)




#MAIN
while True:
    print("BIENVENIDO AL MENU, ELIGE UNA OPCION")
    print("--------------------------------------------")
    print("(1) VER LA LISTA")
    print("(2) PREGUNTAR POR DATOS")
    print("(0) SALIR")
    
    opcion=int(input("INGRESE OPCIÓN: "))
    if opcion==1:       
        imprimirlista(lista)
    elif opcion==2:
        consultarlista(lista)
    elif opcion==0:
        print(" ")
        print("- - -> USTED A SALIDO DEL SISTEMA <- - - ")
        break