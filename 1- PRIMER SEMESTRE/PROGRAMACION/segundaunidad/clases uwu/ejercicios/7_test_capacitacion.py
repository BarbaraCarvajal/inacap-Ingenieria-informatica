
"""
Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente
información: cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente. Se pide confeccionar un programa que ingrese los dos datos por teclado e informe el nivel del mismo según el porcentaje de respuestas correctas que ha obtenido, y sabiendo que:
Nivel máximo: porcentaje >= 90%
Nivel medio: porcentaje >=75 y <90%
Nivel regular: porcentaje >= 50 y <75
Fueradenivel: Porcentaje<50%.
"""

preguntas = float(input("¿Cuántas preguntas le hicieron?"))
correctas = float(input("¿Cuántas fueron correctas?"))
porcentaje = correctas * 100 / preguntas

if porcentaje >= 90:
    print("El porcentaje ",porcentaje,"% Es Nivel maximo")
elif porcentaje >= 75 and porcentaje <90:
    print("El porcentaje ",porcentaje,"% Es Nivel medio")
elif porcentaje >= 50 and porcentaje <75:
    print("El porcentaje ",porcentaje,"% Es Nivel regular")
elif porcentaje <50:
    print("El porcentaje ",porcentaje,"% Fuera de nivel :c ")

