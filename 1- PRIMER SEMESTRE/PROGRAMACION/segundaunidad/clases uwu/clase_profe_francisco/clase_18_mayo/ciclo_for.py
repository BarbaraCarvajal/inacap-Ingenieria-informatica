""""
for i in range(3):
    print(i)
print()
for i in range(1,5,2):
    print(i)
"""

"""for x in range(3):
    print("\n" +"a", end = "")
    for j in range(3):
        print("b", end="")
print("\n" + "Hecho"+ "\n")"""

    #Esto serviria para hacer un reloj por ejemplo de horas,minutos y segundos.

#import os -> Primero hay que llamar la funcion
#os.system -> es para limpiar pantalla
"""
for x in "banana":
    print(x)
    print(x,end="")"""

# EL programa tiene que recibir un mensaje por 
#teclado, el programa tiene 
# que recibir cualquier tecla y 
#tiene que arrojar cuantas veces esta la letra
#en esa frase


frase = input("Ingrese frase \n")
letra = input("Ingrese una letra \n")
total_letra = 0
for i in frase:
    if i == letra:
        total_letra += 1
print(f"La letra [{letra}] se repite [{total_letra}] veces")