""" nombre = input("Ingrese su nombre \n")
print("Su nombre es: {}".format(nombre))

edad = (input("cual es su edad"))

contador = 0
acumulador = 0
contador += 1
acumulador += contador """

sumaSueldo = 0
contadorSueldo = 0
sueldo1 = int(input("Ingrese su sueldo trabajador n°1 \n"))
sumaSueldo+= sueldo1 #acumulador
contadorSueldo += 1 #contador
sueldo2 = int(input("Ingrese su sueldo trabajador n°2 \n"))
sumaSueldo+= sueldo2 #acumulador
contadorSueldo += 1 #contador

print("El total de sueldos de los {} trabajadores es: {}  \n".format(contadorSueldo,sumaSueldo))


