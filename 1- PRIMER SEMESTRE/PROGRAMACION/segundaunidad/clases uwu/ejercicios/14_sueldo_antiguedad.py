""" De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un 
programa que lea los datos de entrada e informe: 
a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, 
otorgarle un 
aumento del 20 %, mostrar el sueldo a pagar. 
b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un 
aumento de 5 %. 
c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios. 

"""

nombre = input("Ingrese el nombre del operario \n")
sueldo = int(input("Ingrese el sueldo de {}\n".format(nombre)))
antiguedad = int(input("Ingrese los años de antiguedad de {}\n".format(nombre)))

print("Datos recolectados: \n Nombre: {}\n Sueldo: ${}\n Antiguedad:{} \n".format(nombre,sueldo,antiguedad))

if sueldo <500 and antiguedad >= 10:
    aumento = sueldo +(int(sueldo * 20/ 100))
    print("Sueldo actualizado de {} es: $ {}".format(nombre,aumento))
elif sueldo <500 and antiguedad< 10:
    aumento = sueldo + (int(sueldo*5/100))
    print("Sueldo actualizado de {} es: $ {}".format(nombre,aumento))
elif sueldo >=500 :
    print("no hay aumento")