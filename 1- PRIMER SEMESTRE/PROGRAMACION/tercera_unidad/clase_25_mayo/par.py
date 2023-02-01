#crear funcion q muestre si un num ingresado es par

def num_par(num):
    if num%2 == 0:
        print("El número ingresado es par")
    else:
        print("El numero no es par")
num = int(input("Ingrese número"))
num_par(num)
