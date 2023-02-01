"""
Escribir un programa que pida ingresar coordenadas (x,y) 
que representan puntos en el plano.
Informar cuántos puntos se han ingresado en el primer,
segundo, tercer y cuarto cuadrante. Al comenzar el programa 
se pide que se ingrese 
la cantidad de puntos a procesar.
"""

cantidad  = int(input("¿cuántas coordenadas ingresará?"))

for x in range (0,cantidad):
    print(f"Ingrese el eje x e y a de la  coordenada N° {x+1} continuación")
    x = float(input())
    y = float(input())
    x += 1
    if x >0 