"""
Un obrero necesita calcular su salario semanal, 
el igual se obtiene de la sig. manera:
• Si trabaja 40 horas o menos se le paga $1600 por hora
• Si trabaja más de 40 horas se le paga $1600 por 
cada una de las primeras 40 horas
y $2000 por cada hora extra.
"""

horas = int(input("¿Cuántas horas trabajó esta semana?\n"))

if horas <= 40:
    print("El salario de esta semana es: $",horas*1600)
elif horas >40:
    extra = horas - 40 
    sueldo = (extra*2000)+(64000)
    print(f"El salario de esta semana, con {extra} horas extras es: ${sueldo}")

# recomendable poner un if con las horas extras
# y luego un else con las horas normales
