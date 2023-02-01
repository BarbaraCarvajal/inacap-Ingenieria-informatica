Proceso mientras_vocales
	Definir letra Como Caracter;
	Definir sw Como Logico;
	sw <- verdadero;
	Mientras sw=verdadero Hacer
		Escribir 'Ingrese una vocal';
		Leer letra;
		Si letra<>'a' Y letra<>'A' Y letra<>'e' Y letra<>'E' Y letra<>'i' Y letra<>'I' Y letra<>'o' Y letra<>'O' Y letra<>'u' Y letra<>'U' Entonces
			sw <- falso;
			Escribir "Ingresó una letra que no es una vocal, adios";
		SiNo
			sw <- verdadero;
		FinSi
	FinMientras
FinProceso
