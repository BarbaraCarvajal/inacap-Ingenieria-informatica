Proceso mientras_edades
	Definir edad,cont,sumaEdades Como Entero;
	Definir sw Como Logico;
	Definir promedio Como Real;
	cont <- 0;
	sumaEdades <- 0;
	promedio <- 0;
	edad <- 0;
	sw <- verdadero;
	Mientras sw=verdadero Hacer
		Escribir 'Ingrese una edad';
		Leer edad;
		Si edad>0 Entonces
			cont <- cont+1;
			sumaEdades <- sumaEdades+edad;
			promedio <- sumaEdades/cont;
		SiNo
			Escribir 'Porfis ingresar una edad sobre 0';
			sw <- falso;
		FinSi
	FinMientras
	Si cont>0 Entonces
		Escribir 'El promdedio de edades es de: ',promedio;
	FinSi
FinProceso
