"""Leer  15  números  negativos,  convertir  cada  número  a  medida  que 
 lo  ingresa  en  positivos  e 
imprimirlo, si ingresa uno positivo
 no imprime el número y solicita el siguiente.  
Pista: Uso de operador multiplicación. """

for x in range(1,16):
    num= int(input(f"#{x} Ingrese un número negativo: "))
    if num < 0:
        num = num *-1
        print(num)
    else:
        print(f"Ingresó un número que ya es positivo {num}, continuemos con el siguiente")
        continue
