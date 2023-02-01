"""
Problema 2: 
Confeccionar una aplicación que solicite la carga de dos valores enteros y muestre su 
suma. 
Repetir la carga e impresión de la suma 5 veces. 
Mostrar una línea separadora después de cada vez que cargamos dos valores y su suma.
"""

def sumatoria():
    respuesta = int(input("¿Cuántas sumas desea realizar?: "))
    for x in range(1,respuesta+1):
        num1 = int(input("Primer valor: "))
        num2 = int(input("Segundo valor: "))
        suma = num1 + num2
        print(f"{x}- La suma entre {num1} y {num2} es: {suma}")
        print("----------------------------------------------")
    print("Muchas gracias, hasta luego")
sumatoria()