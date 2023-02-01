def letras_aleatorias():

    import os
    os.system("clear")
    from random import randint as aleatorio

    inicio = ord("a")
    final = ord("z")

    #lo imprimiremos 2 veces
    for x in range(1,3):
        letras = chr(aleatorio(inicio, final))
        print(f"Las letras aleatorias son: {letras}")
        
letras_aleatorias()