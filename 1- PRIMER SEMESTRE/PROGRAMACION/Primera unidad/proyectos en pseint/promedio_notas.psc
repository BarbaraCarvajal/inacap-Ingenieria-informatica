Proceso promedio_notas
	Definir nota, x, promedio, sumaNotas, cantNotas como real;
	Definir nombre Como Caracter;
	
	Escribir "Ingrese su nombre";
	leer nombre;
	
	Escribir "Ingrese la cantidad de notas que ingresará";
	leer cantNotas;
	
	sumaNotas=0;
	
	Para x = 1 Hasta cantNotas Hacer
	
		Escribir "Ingrese nota";
		leer nota;
		
		sumaNotas = sumaNotas+nota;
		
	FinPara
	
	promedio= sumaNotas/cantNotas;
	Escribir "El promedio de ",nombre, " es: ",promedio," nota redondeada es: ",redon(promedio);
	
FinProceso
