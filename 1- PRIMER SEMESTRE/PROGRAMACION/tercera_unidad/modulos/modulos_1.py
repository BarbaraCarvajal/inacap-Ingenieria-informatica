
import math

# print(dir(math)) #sirve para ver el directorio de funciones disponibles en math
 
#para acceder solo a la función randint del módulo random
#en Python lo podemos expresar con la siguiente sintaxis:

from random import randint

#Para imortar más de una funcionalidad:

from math import sqrt, pow

#para definir un alías a una funcionalidad:

from math import sqrt as raiz, pow as elevar

#Para importar todas las funciones de matemáticas,
#cualquier función que utilice se puede utilizar como sqrt, fctorial,etc.

from math import *

# Sintaxis funciones matemáticas integradas

# Las funciones min() y max() se pueden usar para encontrar
# el valor más bajo o más alto de un iterable:

x = min(5,10,25)
y = max(5,10,25)
print(x,y)

# La función pow() devuelve el valor de un número
# a la potencia dada:

x = pow(4,3)
print(int(x)) # le agregue int para mostrarlo como int(entero)

# Con la función ord() obtenemos el valor ASCII de los carácteres.
# ingresamos el carácter y nos devuelve el número

#ejemplo 1
a = "p"
print(ord(a))

#ejemplo 2 usando también la función max
a = "Python"
a = max(a)
print(ord(a))

# Con la función chr() obtenemos el carácter ASCII asociado al valor.
# o sea aca tenemos q ingresa el "numero" y nos devolvera
# el carácter.

#ejemplo 1
a = 121
print(chr(a))

# El método math.sqrt() devuelve la raíz cuadrada de un número.

import math
x = math.sqrt(64)
print(x)

# La función trunc() devuelve la parte entera de 
# diferentes números:

import math
print(math.trunc(2.77))
print(math.trunc(0.3444))
print(math.trunc(-99.3444))

# Ejercicio: 
# Calcular el área y el périmetro de un triángulo

def area_triangulo():
    lado1 = float(input("Ingrese el primer lado: "))
    lado2 = float(input("Ingrese el segundo lado: "))
    lado3 = float(input("Ingrese el tercer lado: "))

    perimetro = lado1 + lado2 + lado3
    superficie = perimetro/2
    area = math.sqrt(superficie*(superficie-lado1)*(superficie-lado2)*(superficie-lado3))

    print(f"""
    La área del triángulo es: {area:.2f}
    El perímetro es: {perimetro}
    Y la superficie: {superficie}
    """)

#area_triangulo()

# Módulo random, es un módulo incorporado que puede uasr para 
# generar valores aleatorios.

# El método random() devuelve un número flotante
# aleatorio entre 0 y 1:

import random

print(random.random())

# El método randrange() devuelve un elemento seleccionado
# aleatoriamente del rango especificado, se puede
# especificar un paso.

import random 

print(random.randrange(3,9))
# devuelve un número entre 3 (incluido) y 9 (no incluido)

# El método randint() devuelve un elemento seleccionado
# de número entero del rango especificado.

import random

print(random.randint(3,9))
# devuelve un número entre el 3 y el 9 (ambos incluidos)


# El método uniform() devuelve un número flotante
# aleatorio entre los dos números especificados 
# (ambos incluidos)

import random

print(random.uniform(10,60))

# El método choice() devuelve un elemento seleccionado
# aleatoriamente de la secuencia especificada.

import random
x = "12345 saludo" # tiene q ser un string
print(random.choice(x))

# Ejemplos:

# Obtener 3 números con muchos decimales 
# entre 0 y 1

import random

for x in range(3):
    print(random.random())

# Obtener 10 números enteros entre los que 
# pueden aparecer números negativos, positivos
# y el cero.

import random
for x in range(10):
    print(random.randint(-5,15))

# Obtener 25 números que van desde el 3 al 16
# no conciderar el 16
print("----------------")

import random

for x in range(25):
    print(random.randrange(3,16))

# Obtener 3 números flotantes aleatorios entre 100 y 105.

import random

for x in range(3):
    print(random.uniform(100,105))

# Obtener un valor de la secuencia especificada (lista):
# (Una lista se crea con [] separando elementos con coma

import random

lista = ["Barbara", 2022, "camilo", 9.00]
print(random.choice(lista))
