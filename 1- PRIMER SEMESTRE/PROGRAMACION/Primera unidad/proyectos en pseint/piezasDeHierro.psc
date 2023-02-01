Proceso piezasDeHierro
	definir cant_piezas, piezasAptas como entero;
	definir long como real;
	piezas = 0
	piezasAptas = 0
	Escribir "Hola! ¿Cuantas piezas va a ingresar?";
	Leer cant_piezas
	Escribir "Ingrese la longitud de las piezas de hierro";
	Para x<-1 Hasta cant_piezas Hacer
		Leer long
		Si long >= 1.20 y long <= 1.30 Entonces
			Escribir "Pieza apta ";
			piezasAptas = piezasAptas + 1
		SiNo
			Escribir "Pieza NO apta";
		FinSi
	FinPara
	Escribir "**************";
	Escribir "Piezas aptas:  ",piezasAptas;
FinProceso
