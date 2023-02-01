


def maximo(*lista):
    maxi = lista[0]
    for x in lista[1:]:
        if x > maxi:
            maxi = x
    return maxi

print(maximo(12,32,322,0.1))

