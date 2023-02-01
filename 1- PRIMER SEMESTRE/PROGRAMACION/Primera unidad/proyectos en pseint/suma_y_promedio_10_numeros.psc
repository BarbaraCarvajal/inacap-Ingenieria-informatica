Proceso suma_y_promedio_10_numeros
	Definir n,suma Como Entero
	Definir promedio Como Real
	
	n <- 0 
	suma <- 0
	promedio <- 0
	x <- 0
	
	Escribir 'Ingrese 10 numeros'
	
	Para x = 1 Hasta 10 Con Paso 1 PASO Hacer
		Leer n
		suma <- suma + n
		promedio <- suma/10
	
	FinPara
	
	Escribir 'Resultados'
	Escribir 'La suma total es: ',suma,' Y el promedio es: ',promedio
FinProceso
