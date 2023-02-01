Proceso tablas_multiplicar
	Definir num, tabla,inicio Como Entero;
	
	
	Escribir "Ingrese la tabla de multiplicar que desee ver";
	leer tabla;
	
		para inicio = 1 hasta 10 Hacer
			Escribir inicio, " x ", tabla, " = ",inicio*tabla;
		FinPara
		
	Escribir "Toque cualquier tecla para borrar todo :p";
	Esperar Tecla;	
	Borrar Pantalla;
FinProceso
