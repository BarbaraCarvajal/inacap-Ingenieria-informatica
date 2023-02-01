sw = True

print("Ingrese una letra, si quiere parar ingrese una vocal")
while sw == True:
    letra = input("letra: ")
    letra = letra.lower()
    if letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u":
        sw=True
    else:
        sw =False
print("Adios")