import os
os.system("clear")

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

fecha = (dia,mes,año)
print(type(fecha))

dias_mes = [31,28,31,30,
            31,30,31,31,
            30,31,30,31]

if mes in (1,3,5,7,8,10,12):
    for x in dias_mes:
        d_mes =dias_mes[mes-1]
elif mes == 2:
    d_mes = 28
else:
    d_mes = 30

if dia <d_mes:
    dia = dia +1
else:
    dia = 1
    if mes == 12:
        mes = 1
        año = año + 1

print(f"El día próximo es: {dia,mes,año}")