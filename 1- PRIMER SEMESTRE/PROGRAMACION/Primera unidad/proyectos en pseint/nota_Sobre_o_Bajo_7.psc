Proceso nota_Sobre_o_Bajo_7
	definir nota, notaAlta, notaBaja como real;
	nota = 0;
	notaBaja = 0;
	notaAlta = 0;
	Escribir "Ingresar las 10 notas";
	Para x<-1 Hasta 10 Hacer
		Leer nota
		Si nota >= 7 Entonces
			notaAlta = notaAlta + 1
		SiNo
			notaBaja = notaBaja + 1
		FinSi
	FinPara
	Escribir "La cantidad de notas iguales o sobres 7 son: ",notaAlta, " Y las bajo 7 son ",notaBaja;
FinProceso
