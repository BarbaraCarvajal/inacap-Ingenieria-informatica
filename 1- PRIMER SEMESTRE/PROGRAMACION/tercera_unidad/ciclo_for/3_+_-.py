"""Leer 20 números enteros e imprimir cuantos son positivos, 
cuantos negativos y cuantos neutros. 
Pista: Uso de condicional if anidado y contadores. """
neutros = 0
negativos = 0
positivos = 0
for x in range(1,21):
    num = int(input(f"Ingrese el número {x}: "))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        neutros += 1
print(f"""
    **Totales**
    Positivos: {positivos}
    Negativos: {negativos}
    Neutros: {neutros}
""")