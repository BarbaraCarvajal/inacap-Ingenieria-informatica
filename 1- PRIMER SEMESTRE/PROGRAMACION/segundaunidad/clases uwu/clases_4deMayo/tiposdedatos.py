

print(2**3)
print(2**3.)
b= 2.**3
print(type(b))
print(2.**3.)

print((2**4),(2*4.),(2*4))

a = 3.0
b = 4.0
c = (a**2 + b**2)**0.5 #raiz cuadrada
print("c = ",c)

print(6/3)
print(6/3.)
print(6./3)
print(6./3)

a = 6 
b=3
a/= 2*b #divide 
print(a)

c = c + 3
c += 3
print(c)


b = b /3
b/=3


num1 = int(input("ingrese un numero: \n")) #\n hace que pida el dato abajo y no al lado

sucesor = num1 + 1
antecesor = num1 - 1

print("el sucesor de ",num1, " es: ",sucesor, " y el antecesor es: ",antecesor)
print("El antecesor de {} es: {} y el sucesor de {} es {} ".format(num1, sucesor, num1, sucesor))
print(f"El antecesor de {num1} es: {antecesor} y el sucesor de {num1} es: {sucesor}") #f = format

#esta otra forma de interpretar multiples lineas, de una forma más literal:
print(f"""El antecesor es {antecesor}


y el sucesor es {sucesor}""")
