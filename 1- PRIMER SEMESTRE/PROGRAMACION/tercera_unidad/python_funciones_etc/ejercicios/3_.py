"""Escribir un programa que ingrese un numero entero mayor que cero 
(debe validar este ingreso) y muestre los 
divisores de ese número de manera decreciente. 
Ejemplo: número 75, divisores: 75, 25, 15, 5, 3, 1. """


def divisores(num):
    if num>0:
        for x in range(num,0,-1):
            if num%x == 0:
                print(x) 

divisores(75)

               
              
