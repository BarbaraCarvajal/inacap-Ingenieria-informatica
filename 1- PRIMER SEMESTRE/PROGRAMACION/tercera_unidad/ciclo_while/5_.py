""""
Lea dos valores, inicio y final de una secuencia, luego muestre todos los 
valores que hay entre esos  dos  límites  ingresados  (ambos  valores  inclusive).  
Debe  validar  que  el  valor  final  de  la 
secuencia sea mayor que el inicio.  
Pista: Variable sw de tipo lógico.  
"""

sw = True
num_inicial = int(input("Ingrese el numero inicial de al secuencia\n"))
while sw == True:
    num_final =  int(input("Ingrese el numero final de al secuencia\n"))
    if num_final <= num_inicial:
        sw = True
    else:
        for x in range(num_inicial,num_final+1):
            print(x)
        sw=False