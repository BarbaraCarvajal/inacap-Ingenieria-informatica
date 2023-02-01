import os
os.system("clear")

print("------- Toma de ramos inacap -------")
ramos_segundo_semestre = {
    1: "Administracion",
    2: "Funciones y Matrices",
    3: "Programación Orientada a Objeto",
    4: "Base de Datos Relacionales",
    5: "Desarrollo Ágil",
    6: "Sistemas Operativos"
}

def elegir_ramo():
    print("Ramos disponibles para tomar:")
    print()
    #print(f"{ramo:<33}{:<30}".format("Ramo","Clave"))
    print()
    for x,y in ramos_segundo_semestre.items():
        print(f"{y:<35}{x}")
       

elegir_ramo()