"""
Crear una función de nombre “ascii” que recibe como parámetro los caracteres ASCII del listado.
La función lista los códigos y caracteres.
Luego, solicita dos caracteres y valida que estén dentro del listado (ambos). Debe utilizar variable tipo 
switch para la validación correspondiente.
Si estos caracteres no están dentro del listado (ambos), envía un mensaje “¡Ingrese caracteres del
listado!” y vuelve a solicitarlos (ambos). 
Si estos caracteres están (ambos), retorna (return) la suma de sus Códigos ASCII.
Ver salida por pantalla.
"""

def ascii(caracter1,caracter2):
    import os as limpiar
    limpiar.system("clear")
    #import msvcrt as esperar_tecla

    print(f"Caracteres ingresados: {caracter1} y {caracter2}")

    for x in range(60,75):
        if x == ord(caracter1):
            continueP
        if x == ord(caracter2):
            continue
    uno = ord(caracter1) 
    dos = ord(caracter2)
    suma = uno + dos 
    
    print("Presione una tecla para ver la suma...")
    #esperar_tecla.getch()
    return print(suma)

def ingreso_datos():
    print("""
    Código ASCII  Caracter
    60 : <
    61 : =
    62 : >
    63 : ?
    64 : @
    65 : A
    66 : B
    67 : C
    68 : D
    69 : E
    70 : F
    71 : G
    72 : H
    73 : I
    74 : J
    """)

    inicio = ord("<")
    final = ord("J") 
    
    sw = True
    while sw == True:
        primer_caracter = input("Ingrese el primer caracter: ")
        segundo_caracter = input("Ingrese el segundo caracter: ")
        if ord(primer_caracter) >= inicio and ord(primer_caracter) <= final:
            if ord(segundo_caracter) >= inicio and ord(segundo_caracter) <= final:
                sw = False
                ascii(primer_caracter,segundo_caracter)
        else:
            print("Ingrese caractere del listado dado!!")
        

#ingreso_datos()


"""
Crear una función de nombre “dados” que no recibe parámetros.
La función simula 10 lanzamientos de 2 dados e imprime cuantas
 veces los dados sumaron 10.
Ver salida por pantalla
"""

def dados():
    #modulos,imports
    import os as limpiar
    limpiar.system("clear")
    #import msvcrt as esperar_tecla
    from random import randint as azar
    limpiar.system("cls")

    #usar randint: 
    

    #inicializar contadores, acumuladores
    suman_10 = 0
    suma = 0

    #inicio ciclo for
    print("Presione una tecla para lanzar dado...")
    #esperar_tecla.getch()
    for x in range(1,11):
        dado1 = azar(1,6)
        dado2 = azar(1,6)
        print(f"Lanzamiento {x}: ")
        print(f"dado 1: {dado1}")
        print(f"dado 2: {dado2}")
        
        suma = dado1 + dado2
        if suma == 10:
            suman_10 = suman_10 +1
    print(f"Veces en que los dados sumaron 10: {suman_10}")

#codigo main
#dados()

"""
Crear un programa que permita calcular el cuadrado y el cubo de los 5 primeros números enteros que 
siguen a un número ingresado por teclado. Debe utilizar el módulo math para los cálculos respectivos.
"""

def cuadrado_cubo():
    #importar modulos/funciones
    from math import pow as elevar
    import os as limpiar
    limpiar.system("clear")
    #import msvcrt as esperar_tecla

    #pedimos datos
    num = int(input("Ingrese un numero: "))
    for x in range (num,num+5):
        num = num+1
        cuadrado = elevar(num,2) #acá se usa la función pow
        cubo = elevar(num,3) #acá se usa la función pow
        print(f"{num} al cuadrado es: {cuadrado:.0f} y el {num} al cubo es: {cubo:.0f}")
    
    print("Presione una tecla para salir...")
    #esperar_tecla.getch()

# main
#|cuadrado_cubo()

