Proceso hermanoMayor
	Definir edad1, edad2, dif como enteros;
	
	Escribir "Ingrese la edad del primer hermano";
	Leer edad1;
	
	escribir "Ingrese la edad del segundo hermano";
	Leer edad2;
	
	dif= edad1 - edad2;
	
	si edad1>edad2 Entonces
		Escribir "La edad del Primer hermano ingresado es la mayor, se diferencian por: ",dif, " años";
	FinSi
	
	Si edad2>edad1 entonces;
		Escribir "La edad del Segundo hermano ingresado es la mayor, se diferencian por: ",dif, " años";
	FinSi
		
	Si edad1=edad2 Entonces
		Escribir "Los hermanos tienen la misma edad: ",edad1;
	FinSi
	
FinProceso
