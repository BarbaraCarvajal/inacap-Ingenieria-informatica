

def division(a,b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:
        print("No se puede dividir por 0 ")

division(20, 8) 