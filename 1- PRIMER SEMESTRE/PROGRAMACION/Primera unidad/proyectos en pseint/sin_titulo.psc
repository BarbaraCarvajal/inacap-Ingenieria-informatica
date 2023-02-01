Proceso sin_titulo
	definir num, x, contador como enteros;
	Escribir "ingrese el numero a consultar";
	Leer num;
	x = 1;
	contador = 0;
	Mientras x <= num Hacer
		Si num % x = 0 Entonces
			contador = contador + 1;
		FinSi
		x = x+ 1;
	FinMientras
	Si contador = 2 Entonces
		Escribir "El numero ", num, " si es primo";
	SiNo
		Escribir "El numero ",num, " no es primo";
	FinSi
FinProceso
