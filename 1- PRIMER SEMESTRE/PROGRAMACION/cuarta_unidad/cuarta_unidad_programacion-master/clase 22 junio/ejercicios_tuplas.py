import os
from math import sqrt as raiz, pow as elevado
os.system("clear")

def distancia(p1,p2):
    x1,y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    return raiz(elevado(dx,2) + elevado(dy, 2))
    #elevado(elevado(dx,2) + elevado(dy, 2),0.5)

a = (2,3)
b = (7,15)
print(distancia(a, b))


persona = ("pancho",1234-4, (14,5,1990))
nombre,rut,(d,m,a)= persona
print(f"{nombre} nacio en {a}")


# ejercicio tipo prueba!!
a = ("analista", "programador", "inacap")
x,y = ((27,3),9)
v = (x,a)
print(v)
print(v[1][1])

alumnos = [
    ("pancho", "valparaiso", "200003393-4", "civil"),
    ("javier", "viña", "324324243-4", "electrica"),
    ("monica", "santiago", "2313131-4", "enfermeria")
]

for nombre,ciudad,rut,carrera in alumnos:
    print(f"{nombre},con rut {rut} estudia ,{carrera}, y es de {ciudad}")

print(alumnos[1][3],alumnos[0][3],alumnos[2][3])
if alumnos[0][3] == "civil":
    print("Felicidades, será un civil")