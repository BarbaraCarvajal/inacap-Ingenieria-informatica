# 5- Desarrollar un algoritmo que a partir de una lista lst = [1,2,3,4,5]
# genere una segunda lista lst2 con los valores lst2 =[1,3,6,10,15]

import os
#os.system("clear") #mac
os.system("cls") #windows


lista = [1,2,3,4,5]
lista2 = [1,3,6,10,15]

lista1=([1,2,3,4,5]) 
#lista2=([1,3,6,10,15])
lista2 = []
total=0
for i in lista1:
    total=total+i
    lista2.append(total)
    #print(total,end=",")
print(lista2)
   
   
