Proceso auto_tag
	Definir auto,categoria,camioneta,tarifa Como Caracter;
	Definir precio Como Entero;
	Escribir 'Ingresar la categoria de su vehiculo';
	Escribir 'Opciones: ';
	Escribir 'Auto o Camioneta ';
	Escribir 'Moto';
	Escribir 'Camion o Bus';
	Leer categoria;
	Si categoria='auto' O categoria='camioneta' Entonces
		Escribir '¿Tarifa normal (n) o de fin de semana (f) ?';
		Leer tarifa;
		Si tarifa='n' Entonces
			precio <- 2000;
		SiNo
			Si tarifa='f' Entonces
				precio <- 3000;
			FinSi
		FinSi
	SiNo
		Si categoria='moto' Entonces
			Escribir '¿Tarifa normal (n) o de fin de semana (f) ?';
			Leer tarifa;
			Si tarifa='n' Entonces
				precio <- 600;
			SiNo
				Si tarifa='f' Entonces
					precio <- 900;
				FinSi
			FinSi
		SiNo
			Si categoria='camion' O categoria='bus' Entonces
				Escribir '¿Tarifa normal (n) o de fin de semana (f) ?';
				Leer tarifa;
				Si tarifa='n' Entonces
					precio <- 3500;
				SiNo
					Si tarifa='f' Entonces
						precio <- 5200;
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
	Escribir 'Total $',precio;
FinProceso
