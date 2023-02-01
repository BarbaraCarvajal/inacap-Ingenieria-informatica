"""
La siguiente fórmula permite determinar si un año es bisiesto:
=IF(OR(MOD(A1,400)=0,AND(MOD(A1,4)=0,MOD(A1,100)<>0))
Cree el programa que permita realizar el cálculo respectivo. 
Debe interpretar la fórmula para código Python.
Datos de prueba;
Si el valor de A1 es: 1992
2000
1900
La fórmula devuelve: Año bisiesto
Año bisiesto
No es un año bisiesto
"""

año = int(input("Ingrese un año\n"))

if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año NO es bisiesto")