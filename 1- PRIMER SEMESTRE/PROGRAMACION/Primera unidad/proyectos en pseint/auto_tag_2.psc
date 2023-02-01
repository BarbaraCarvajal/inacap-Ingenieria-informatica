Proceso auto_tag_2
	Definir categoria,tarifa Como Caracter;
	Definir precio Como Entero;
	Escribir 'Ingrese la categoria de su vehiculo';
	Leer categoria;
	Si categoria='auto' O categoria='camioneta' Entonces
		Escribir 'Ingrese n si es un dia normal o f si es sin de semana';
		Leer tarifa;
		Si tarifa='n' Entonces
			precio <- 2000;
		SiNo
			Si tarifa='f' Entonces
				precio <- 3000;
			SiNo
				Escribir 'ingrese una tarifa valida';
			FinSi
		FinSi
	SiNo
		Si categoria='moto' Entonces
			Escribir 'Ingrese n si es un dia normal o f si es fin de semana ';
			Leer tarifa;
			Si tarifa = "n"; Entonces
				precio <- 600;
			SiNo
				Si tarifa = "f"; Entonces
					precio = 900;
				SiNo
					Escribir "ingrese tarifa valida";
				FinSi
			FinSi
		SiNo
			Si categoria='bus' O categoria='camion' Entonces
				Escribir "Ingrese n si es un dia normal o f si es un fin de semana";
				Leer tarifa;
				Si tarifa = "n"  Entonces
					precio <- 3500;
				SiNo
					Si tarifa = "f"; Entonces
						precio = 5200;
					SiNo
						Escribir "Ingrese tarifa valida";
					FinSi
				FinSi
			SiNo
				Escribir 'porfis ingresar categoria valida';
			FinSi
		FinSi
	FinSi
	Escribir 'Total $',precio;
FinProceso
