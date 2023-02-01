""" Escribir un programa que pida ingresar
la coordenada de un punto en el plano, 
es decir dos valores enteros x e y (distintos a cero).
Posteriormente imprimir en pantalla en que cuadrante 
se ubica dicho punto. (1º Cuadrante 
si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)
"""


x = int(input("Ingrese la coordenada del punto X\n"))
y = int(input("Ingrese la coordenada del punto Y\n"))

if x>0 and y>0:
    print(f"La coordenada {x} y la {y} estan en el primer cuadrante")
elif x>0 and y<0:
    print(f"La coordenada {x} y la {y} estan en el segundo cuadrante")
elif x<0 and y<0:
    print(f"La coordenada {x} y la {y} estan en el tercer cuadrante")
elif x<0 and y>0:
    print(f"La coordenada {x} y la {y} estan en el cuarto cuadrante")
elif x==0 and y==0:
    print(f"La coordenada {x} y la {y} estan en el eje 0")
else:
    print("Porfis ingresar un numero valido")