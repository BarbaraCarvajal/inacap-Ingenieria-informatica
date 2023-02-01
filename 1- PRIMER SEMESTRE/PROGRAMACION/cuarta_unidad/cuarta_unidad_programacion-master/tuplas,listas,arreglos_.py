
import os
os.system("cls")

# Tuplas, no se pueden eliminar, actualizar ni agregar
# Se pueden mostrar y buscar elementos

tupla = (4,"hola", 5, 6.56, [1,2,3], 4)


#print(4 in tupla)
#print(tupla.index("hola"))
#print(tupla.count(4))

num=[4,7,9,2]
#print(num[3])
datos=[["uno", 2, 3],["a", "b", "c"]]
#print(datos[1][2])

from numpy import array
temp=array([5,100,25,34,0,3])
print(temp[0])
print(temp[1])
print(temp[2])
print(temp[3])
print(temp[4])
print(temp[5])
temp1=array([[1,2,3],[4,5,6],[7,8,9]])
print(temp1[0,2])

list1 = [ 1, 7, 87, 9, 45]
print(list1[:])
print(list1[2:4])

"""Longitud de lista
Para determinar cuántos elementos tiene una lista, use la 
función len(): """

colores=['azul', 'rojo', 'verde', 'amarillo'] 
print(len(colores))

"""Acceder/Modificar valor 
i-enésimo
Es posible modificar el valor i-enésimo elemento, 
accediendo con el índice correspondiente:"""

colores1=["azul", "rojo", "verde", "amarillo"] 
print(colores1)
colores1[1]="negro"
resultado =['azul', "negro", "verde", "amarillo"]
print(resultado)

a = list("holi")
b = list(range(10))
print(a)
print(b)

"""
Operaciones sobre listas
Longitud de lista
Para determinar cuántos elementos tiene una lista, use la 
función len(): 
"""

colores=['azul', 'rojo', 'verde', 'amarillo'] 
print(len(colores)) 

