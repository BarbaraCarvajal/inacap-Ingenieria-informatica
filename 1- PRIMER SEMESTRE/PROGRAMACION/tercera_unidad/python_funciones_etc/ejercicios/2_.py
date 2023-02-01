"""Crear un programa que permita determinar si un año ingresado
 es bisiesto o no. Un año es bisiesto si es múltiplo 
de cuatro, pero excluyendo aquellos que son múltiplos de 100 
pero no de 400. El programa solicita un año, lo 
evalúa y valida si desea ingresar otro año (s/n), 
al indicar “n” termina su ejecución. """

def año_bisiesto_o_no():
    sw = True
    while sw == True:
        respuesta = input(("Desea saber si un año es bisiesto? N/S\n").lower())
        if respuesta == "s":
            año = int(input("Ingrese un año: "))
            if año%4 == 0 and (año%100 !=0 or año%400 ==0):
                print("El año es bisiesto")
            else:
                print("El año no es bisiesto")
        elif respuesta == "n":
            print("Muchas gracias, adioooos :3")
            sw = False
        else:
            print("Respuesta incorrecta")

año_bisiesto_o_no()

def año_bisiesto_o_no(año):
    sw = True
    while sw == True:
        respuesta = input(("Desea saber si un año es bisiesto? N/S\n").lower())
        if respuesta == "s":
            #año = int(input("Ingrese un año: "))
            if año%4 == 0 and (año%100 !=0 or año%400 ==0):
                print("El año es bisiesto")
            else:
                print("El año no es bisiesto")
        elif respuesta == "n":
            print("Muchas gracias, adioooos :3")
            sw = False
        else:
            print("Respuesta incorrecta")

año_bisiesto_o_no(1900)