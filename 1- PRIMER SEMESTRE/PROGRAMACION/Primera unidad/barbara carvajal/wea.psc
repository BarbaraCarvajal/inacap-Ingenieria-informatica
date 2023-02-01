Proceso par_o_impar
	Definir num,impares,pares Como Entero;
	Definir sw Como Logico;
	pares <- 0;
	impares <- 0;
	sw <- verdadero;
	num <- 1;
	Mientras sw=verdadero Hacer
		Mientras num<=25 Hacer
			Si num=2 O num=4 O num=6 O num=8 O num=10 O num=12 O num=14 O num=16 O num=18 O num=20 O num=22 O num=24 Entonces
				pares <- pares+1;
				num <- num+1;
				sw <- verdadero;
			Sino
				impares <- impares+1;
				num <- num+1;
				sw <- falso;
			FinSi
		FinMientras
	FinMientras
	Escribir 'La cantidad de pares es: ',pares;
	Escribir 'La cantidad de impares es: ',impares;
FinProceso
