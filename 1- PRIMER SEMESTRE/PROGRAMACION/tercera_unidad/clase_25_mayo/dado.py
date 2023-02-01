from random import randint as dado


sw = False
num = dado(1,6) #1,6 es el rango exacto que se usara, literalmente desde el 1 al 6
print("el dado fue lanzado")

#sw = interruptor, parte "encendido", pero en este caso el ciclo pide que 
# sea falso para que se repita, si no es asi, se sale del ciclo.

while not sw : 
    adivina =int(input("¿Qué número es?: "))
#partimos comparando los valores.
    if num > adivina:
        print("... el número es mayor...")
    elif num < adivina:
        print("... el número es menor...")
       
    else: 
        print(f"SII has acertado! el numero es: {num}")
        sw = True
print("Gracias por jugar")

