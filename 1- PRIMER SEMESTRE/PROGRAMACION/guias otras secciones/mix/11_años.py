"""
Escribir un programa
que permita al usuario 
ingresar dos años y luego imprima todos
los años en ese rango, que sean bisiestos y
múltiplos de 10. Nota: para que un año sea bisiesto debe 
ser divisible por 4 y no debe ser divisible por 100, excepto 
que también sea divisible por 400
"""

año1 = int(input("Ingrese el primer año \n"))
año2 = int(input("Ingrese el segundo año \n"))

for año in range(año1,año2):
    if año % 4 == 0:
        if año % 100 != 0 or año % 400 == 0:
            print(año)


"""
(x / 10 == 0):
if(x /4 == 0) :
if (not x%100 == 0 ):
if x/400 == 0:
print(x)"""