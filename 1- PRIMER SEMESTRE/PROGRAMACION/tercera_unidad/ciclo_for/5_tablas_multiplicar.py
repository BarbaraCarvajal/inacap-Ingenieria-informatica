"""Calcular e imprimir las tablas de multiplicar, del  
multiplicando 1 al 10. La salida debe entregar 
cada tabla de multiplicar del multiplicador 1 al 10.  
Pista: Utilizar ciclo for anidado. """

for i  in range(0,10):
    i += 1
    print("--------------")
    for x in range(0,10):
        x += 1
        resultado = x * i
        print(f"{i} x {x} = {resultado}")