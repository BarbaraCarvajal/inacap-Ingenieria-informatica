Proceso mientras_num_primos
	Definir n,x,contador Como Entero;
	Escribir 'Ingrese un numero';
	Leer n;
	x <- 1;
	contador <- 0;
	Mientras x<=n Hacer
		Si n MOD x=0 Entonces
			contador <- contador+1;
		FinSi
		x <- x+1;
	FinMientras
	Si contador=2 Entonces
		Escribir 'numero ',n,' si es primo';
	SiNo
		Escribir 'El numero ',n,' no es primo';
	FinSi
FinProceso
