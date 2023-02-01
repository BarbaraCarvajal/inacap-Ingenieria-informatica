"""
Desarrollar un programa que
solicite la carga de 10 números e imprima la 
suma de los últimos 5 valores ingresados.
"""
print("Ingrese 10 numeros :D")
suma = 0
for x in range(10):
        num = int(input())
        if x >= 5:
            suma = suma + num

print(f"La suma de los ultimos 5 numeros es {suma}")

