

cant = int(input("Ingrese la cantidad: "))
print(cant)

lista = []
for x in range(cant):
  lista.append(int(input(f"{x+1})Ingrese el numero: ")))
print(lista)