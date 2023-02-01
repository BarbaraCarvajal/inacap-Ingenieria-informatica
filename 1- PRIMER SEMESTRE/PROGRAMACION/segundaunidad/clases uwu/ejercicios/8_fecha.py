""" Realizar un programa que pida cargar una fecha cualquiera, 
luego verificar si dicha fecha 
corresponde a Navidad. 
"""

dia = int(input("Ingrese el dia de hoy (1 - 31)\n"))
mes = input("Ingrese el mes\n")

if dia == 25 and mes == "diciembre":
    print("Feliz navidad! Hoy es 25 de Diciembre!!")
elif dia == 25 and mes == "Diciembre":
    print("Feliz navidad! Hoy es 25 de Diciembre!!")
else:
    print("Hoy es {} de {} :c asi que no es navidad, animos!".format(dia,mes))