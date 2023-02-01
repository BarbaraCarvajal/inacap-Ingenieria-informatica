import os
os.system("clear")


ruedas = {
    "auto" : 4,
    "bicicleta": 2,
    "triciclo": 3
}
print(ruedas)
print(len(ruedas))

#IMPORTANTE!!!!
for x,y in ruedas.items():
    print(f"Las ruedas de {x} son {y}")

for x in ruedas.values():
    print(x)
x = "auto" in ruedas
print(x)

x= input("Ingrese un metodo de transporte a consultar: ") 
if x in ruedas:
    print(f"El transporte {x} existe")
else:
    print(f"El transporte {x} no existe")


