
"""
2. La siguiente Lista representa 
los asientos de una sala de cine, donde “0” 
indica asiento disponible y “X” asiento ocupado.
cine = [ 
["X","X","X","0","0"], 
["X","X","X","X","0"], 
["X","0","X","0","X"], 
["X","X","X","X","0"], 
["0","0","X","0","0"],
]
Escriba las siguientes funciones, para obtener:
- asientos_disponibles(cine) #Retornará si la 
sala tiene o no asientos disponibles. 
La función retorna True si existen asientos 
disponibles y False si no los hay.
- porcentaje_disponible(cine) 
#Retornará en porcentaje la disponibilidad de la sala.
"""
import os
os.system("clear")

cine = [ 
["X","X","X","0","0"], 
["X","X","X","X","0"], 
["X","0","X","0","X"], 
["X","X","X","X","0"], 
["0","0","X","0","0"],
]

def asientos_disponibles(cine):
    print("0" in cine[0][0:6])

asientos_disponibles(cine)

"""def porcentaje_disponible(cine):
    total = 25
    disponibles = 0
    ocupados = 0
    for x in cine:
        for i in x:
            if x == "0":
                disponibles += 1
            elif x == "X":
                ocupados += 1
    print(f"Existen {disponibles} asientos disponibles, y {ocupados} asientos ocupados.")

"""


def porcentaje_disponible(sala):
    cantidad_asientos = 0
    cantidad_disponible = 0
    for fila in sala:
        for asiento in fila:
            if asiento == 'O':
                cantidad_disponible+=1
            cantidad_asientos+=1
    return round(cantidad_disponible/cantidad_asientos,1)

print(porcentaje_disponible(cine))