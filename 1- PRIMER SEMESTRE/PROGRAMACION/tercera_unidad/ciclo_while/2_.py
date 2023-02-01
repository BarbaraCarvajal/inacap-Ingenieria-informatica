"""Solicite  ingresar  letras  hasta  que  se  ingrese  
una  vocal  (a,e,i,o,u).  Utilice  una  variable  tipo 
interruptor o bandera (switch), 
para controlar la salida del ciclo.  
Pista: Condicional con operador lógico and. """

#opción 1 uwu
"""letrita = " " 
while letrita != "a" and letrita != "e" and letrita != "i" and letrita != "o" and letrita != "u":
    letrita = input("Ingrese una letra que no sea vocal \n")
    letrita = letrita.lower()
print("Ingresó una vocal, adios")"""

#opción 2

sw = True
while sw == True:
    letra = input("Ingrese una letra que no sea vocal \n")
    if letra != "a" and letra != "e" and letra != "i" and letra != "o" and  letra != "u":
        sw = True
    else:
        print("Ingresó una vocal, adios uwu")
        sw = False
