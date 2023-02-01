

# 1 Definir una función max() que tome como argumento dos números 
# y devuelva el mayor de ellos. (Es cierto que python tiene una función max() 
#incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def max_num(n1,n2):
    if n1 == n2:
        return print("Los numeros no pueden ser iguales")
    elif n1 > n2:
        return print(n1)
    else:
        return print(n2)
max_num(5,50)


# 2 Definir una función max_de_tres(), que tome tres números
# como argumentos y devuelva el mayor de ellos.

def max_de_tres(n1,n2,n3):
    if n1 == n2:
        return print("Los numeros no pueden ser iguales")
    elif n1 > n2 and n1 > n3:
        return print(n1)
    elif n2 > n1 and n2> n3:
        return print(n2)
    else:
        return print(n3)
max_de_tres(44554,-222,4343)
"" 
# 3 Escribir una función que tome un carácter y devuelva 
# True si es una vocal, de lo contrario devuelve False.

def is_vocal(caracter):
    lista_vocales = ['a','e','i','o','u']
    if caracter in lista_vocales:
        return True
    else:
        return False

print(is_vocal('a'))

# 4 Escribir una función sum() y una función multip() 
# que sumen y multipliquen respectivamente todos los números de una lista.
# Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def suma(lista):
    resultado = 0
    for x in lista:
        resultado += x
    print(resultado)

suma([1,2,3,]) 

def multiplicacion(lista):
    resultado2 = 1
    for x in lista:
        resultado2 *= x
    print(resultado2)

multiplicacion([1,2,3,4])


# 5 Definir una función inversa() que calcule 
# la inversión de una cadena. Por ejemplo la cadena 
# "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa(cadena):
    cadena = cadena[::-1]
    return print(cadena)

inversa("hola como estas")


# 6 Definir una función es_palindromo() que reconoce palíndromos 
# (es decir, palabras que tienen el mismo aspecto escritas invertidas), 
# ejemplo: es_palindromo ("radar") tendría que devolver True.

def es_palindromo():
    palabra = input("Ingrese la palabra: ")
    if palabra == palabra[::-1]:
        return print(True)
    else:
        return print(False)

#es_palindromo()


# 7 Definir una función superposicion() que tome dos listas y 
# devuelva True si tienen al menos 1 miembro en 
# común o devuelva False de lo contrario. 
# Escribir la función usando el bucle for anidado.

def superposicion(lista1,lista2):
    for x in lista1:
        for i in lista2:
            if x == i:
                return True
    
    return False 
print('Superposicion:')
print(superposicion([1,2,3],[7,2,5]))

 # 8 Definir una función generar_n_caracteres()
 # que tome un entero n y devuelva el caracter multiplicado por n. 
 # Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generar_n_caracteres(num,caracter):
        print(caracter*num)


generar_n_caracteres(5,"*")

# 9 Definir un histograma procedimiento() que tome una 
# lista de números enteros e imprima un histograma en la pantalla. 
# Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente"""""

def procedimiento(lista):
    for x in lista:
        print(x*"*")

procedimiento([3,4,3])