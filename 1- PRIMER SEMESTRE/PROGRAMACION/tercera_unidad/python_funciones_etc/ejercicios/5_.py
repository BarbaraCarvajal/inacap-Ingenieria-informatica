"""Crear un programa que devuelva los caracteres 
ASCII de los códigos el 97 al 100 (a-d)."""

def ascii_1(num1,num2,num3,num4):
        for x in range(num1,num4+1):
            print(chr(x))

ascii_1(97,98,99,100)
