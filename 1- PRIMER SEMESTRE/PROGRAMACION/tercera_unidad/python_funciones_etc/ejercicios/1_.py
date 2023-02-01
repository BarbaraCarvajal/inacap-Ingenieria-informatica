"""Crear  una  función  que  permita  evaluar  
2   valores  enteros  ingresados  por  teclado, 
 inicio  y  final  de  una 
secuencia, luego muestre todos los valores que hay entre 
esos dos límites ingresados (ambos valores inclusive) 
separados por guión. Utilice ciclos while y variable tipo switch, 
validando que el valor final de la secuencia sea 
mayor que el inicial. """


def largo_secuencia():
    sw = True
    numero1 = int(input("Ingrese el primer valor: "))
    while sw == True:
        numero2 = int(input("Ingrese el segundo valor: "))
        if numero2 >= numero1 and numero2 !=  numero1:
            sw=False
        for x in range(numero1,numero2+1):
            print(x, end= " - ")

largo_secuencia()

#practicar el pedir el sw al usuario
