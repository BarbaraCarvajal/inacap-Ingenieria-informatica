"""Mostrar los números de la serie (1, 2, 5, 26, ...) 
que sean menores a 1000.  
Pista: Utilizar operador potencia."""
x = 1
while x < 1000:
    print(x)
    x = x**2 +1
    