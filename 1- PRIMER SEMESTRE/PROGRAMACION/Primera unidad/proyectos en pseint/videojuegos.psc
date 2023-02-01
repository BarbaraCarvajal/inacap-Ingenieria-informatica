Proceso videojuegos
	Definir edad Como Entero;
	Escribir 'Bienvenido a Videojuegos Barbarita';
	Escribir 'Por favor ingrese su edad';
	Leer edad;
	Si edad<=4 Entonces
		Escribir 'El cliente tiene ',edad,' años por lo cual entra gratis!';
	SiNo
		Si edad>4 Y edad<=18 Entonces
		Escribir 'El cliente tiene ',edad,' años por lo cual debe pagar $5.000';
		SiNo
			Si edad>18 y edad<=99 Entonces
				Escribir 'El cliente tiene ',edad,' Por lo cual debe cancelar $10.000';
			SiNo
				si edad>99 Entonces
					Escribir "Wow que viejo! Entrada gratis para ud! :D";
				FinSi
		FinSi
	FinSi
FinSi	
	
	
FinProceso
