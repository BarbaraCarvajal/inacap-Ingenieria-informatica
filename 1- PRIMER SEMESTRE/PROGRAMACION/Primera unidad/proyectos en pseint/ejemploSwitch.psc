Proceso ejemploSwitch
	Definir bucle Como Entero;
	Definir sw Como Logico;
	sw <- verdadero;
	bucle <- 1;
	Mientras sw = verdadero Hacer
		Si bucle <=5 Entonces
			bucle <- bucle+1;
			Escribir 'bucle  ';
			sw <- verdadero;
		SiNo
			sw <- falso;
		FinSi
	FinMientras
FinProceso
