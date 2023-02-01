
#Funciones que estan ya importadas en Python

#import math
#import math


x = min (3,-15,20)
print(x)
y = max (30,-2,80)
print(y)

x = pow(4,3) # esto es lo mismo que 4**3
print(x)
y = 4**3
print(y)

a = max("Python")
print(a) #muestra la letra "mayor" del abecedario
print(ord(a)) #muestra el número ascii

#Funciones que si hay que importar 
#print(math.sqrt(2.77)) #función de la raíz 

"""from math import sqrt as raicita #formúla del apodo
print(raicita(2.77))

"""
from math import sqrt as raiz 

l1 = int(input("l1: "))
l2 = int(input("l2: "))
l3 = int(input("l3: "))

p= l1 + l2 + l3
print(p)
s = p/2
a = raiz(s*(s-l1)*(s-l2)*(s-l3))
print(round(a,2)) #redondeo a dos decimales

import calendar
print(calendar)