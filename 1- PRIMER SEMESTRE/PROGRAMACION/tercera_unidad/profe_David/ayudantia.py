"""import os
os.system("clear") # cls para windows
#genera un limpiado de pantalla"""


def guardarDatos(num1,num2,num3):
    if num1 < num2 and num2 < num3:
        print(f"{num1},{num2},{num3}")
    elif num1 < num2 and num3 < num2:
        print(f"{num1},{num3},{num2}")
    elif num1 < num3 and num3 < num2:


    elif num2 < num3 and num3<num1:
        print(f"{num2},{num3},{num1}")
    elif num2 < num3 and num1 < num3:
        print(f"{num2},{num1},{num3}")


    elif num3 < num1 and num1 < num2:
        print(f"{num3},{num1},{num2}")
    elif num3 < num1 and num2 < num1:
        print(f"{num3},{num2},{num1}")
    elif 

    else:
        print(f"Todos los numeros son iguales: {num1},{num2},{num3}")

num1 = int((input("Primer número: ")))
num2 = int((input("Segundo número: ")))
num3 = int((input("Tercer número: ")))
guardarDatos(num1,num2,num3)


