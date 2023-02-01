""" Requerir al usuario que 
ingrese un número entero positivo
e imprimir todos los números correlativos entre 
el ingresado por el usuario y uno 
menos del doble del mismo. """

num = int(input("Ingrese un numero\n"))
final = (num*2)
for x in range(num,final): print(x)