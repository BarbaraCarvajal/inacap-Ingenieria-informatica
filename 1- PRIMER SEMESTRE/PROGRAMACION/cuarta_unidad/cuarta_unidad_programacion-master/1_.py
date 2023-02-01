

# 1- Crear una lista (arreglo de datos) de n posiciones, llénela con nombres
# de personas  y como salida debe mostrar los nombres almacenados y la posición
# correspondiente. Utilice ciclos para los procesos anteriores. 


nombres = []
cantidad = int(input("¿Cuantos datos desea ingresar?: "))
for x in range(cantidad):
    ingresar = input(f"{x+1}- Ingrese los nombres para la lista: ")
    nombres.append(ingresar)
    
print(nombres) # imprime normal la lista, tal cual esta escrita

for x in nombres: # imprime la lista como en un listado
    print(x)
index = -1 # inicializamos "index" en -1 para que parta en 0 
for x in nombres:
    index = index+1
    print(f"La posición de {x} es: {index}")

