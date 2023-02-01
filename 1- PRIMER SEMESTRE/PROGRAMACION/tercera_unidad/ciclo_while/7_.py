"""while  anidado:  Ingresar  números  por  teclado,
  hasta  que  el  usuario  conteste  que  no  desea 
continuar ingresando (respuesta “n”) y en ese momento 
muestra el total de números que ingresó. 
Se aporta ejemplo de parte del código
 que debe modificar y/o completar.  

cont=0  
Mientras respuesta=“s” hacer  
Escribir “Ingrese número “,cont Leer num;  
Escribir “¿Desea ingresar otro número (s/n)? ”  
Leer respuesta;  
Mientras respuesta!=“s” hacer  
Escribir “Ingresar respuesta correcta”  
Leer respuesta 
FinMientras 
 FinMientras"""


sw = False
while not sw:
    respuesta = input("Desea continuar? (S/N)\n")
    respuesta = respuesta.upper()
    print(f"Respuesta: {respuesta}")
    if respuesta != "S" and respuesta != "N":
        print("Ingrese respuesta valida!")
        sw = False
    elif respuesta == "N":
        break
    else:
        sw = False