
def contador_a():
    cant_a = 0

    valor = input("Ingrese una frase")
    valor = valor.lower()
    for x in valor:
        if "a" in x:
            cant_a +=1
        return cant_a

print(f"La cantidad de letras 'a' es: {contador_a()}")