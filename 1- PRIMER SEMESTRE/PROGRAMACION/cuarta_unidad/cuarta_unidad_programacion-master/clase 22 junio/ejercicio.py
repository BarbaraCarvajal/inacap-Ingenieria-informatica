import os, random
os.system("clear")

#randint #choise
def coordenadas():
    letras = list("ABCDEFGHIJ")
    letras = tuple(letras)
    #print(letras)

    num = list(range(1,6))
    

    print("coordenadas:")
    for x in range(3):
        random1 = random.choice(letras)
        random2 = num[random.randint(0, 4)]
        #random2 = random.randint(1,5)
        print(str(random1)+str(random2),end=" ")
coordenadas()

