Proceso alturas
	Definir cantAltura Como Entero
	Definir altura,promedio Como Real
	
	promedio <- 0
	cantAltura <- 0
	altura = 0
	
	Escribir 'Hola, cuantas alturas ingresara?'
	Leer cantAltura
	Escribir 'Ingrese las ',cantAltura,' alturas (ejemplo: 1.50)'
	Para x<-1 Hasta cantAltura Hacer
		Leer altura
		promedio <- promedio+altura/cantAltura
		

	FinPara
	Escribir 'La altura promedio de ',cantAltura,' personas es de: ',promedio
	
FinProceso
