
def muchas_cosas():

    import os, time
    os.system("clear")
    from random import randint as aleatorio
    #import msvcrt (sólo en windows)
    print("Buscando 2 letras al azar...entre la A y la Z")

    for x in range(1,4):
        print(x)
        time.sleep(0.5)
        
    inicio = ord("a")
    final = ord("z")

    for x in range(1,3): #repetiremos 2 veces el código
        letra = chr(aleatorio(inicio, final))
        print(f"{x} la letra aleatoria es: {letra}")
muchas_cosas()