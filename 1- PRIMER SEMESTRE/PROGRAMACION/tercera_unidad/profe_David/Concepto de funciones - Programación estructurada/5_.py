"""
Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego preguntar 
si quiere calcular y mostrar su perímetro o su superficie. 
"""

def calculos():
    sw = True
    while sw == True:
        pregunta = int(input("¿Desea usar el programa? 1 = sí - 2 = no\n"))
        if pregunta == 1: 
            sw = True
        else:
            print("Muchas gracias, adios!")
            sw = False
    
            lado = float(input("Ingrese la distancia de un lado del cuadrado: "))
            respuesta = int(input("""
            ¿Qué desea hacer?
            Opción 1: Calcular perímetro
            Opción 2: Calcular superficie \n"""))

            if respuesta == 1:
                perimetro = lado*4
                print(f"El perimetro es: {perimetro}")
            elif respuesta == 2:
                superficie = lado**2
                print(f"La superficie del cuadrado es: {superficie}")

calculos()
