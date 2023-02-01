Proceso deNegativo_a_positivo
	
	Definir num, x, numPositivo Como Entero;
	num=0;
	
	
	
	Para x = 1 Hasta 15 Hacer
		
	Escribir "Ingrese un número NEGATIVO";
	leer num;
	
	si num <0 Entonces
	
	numPositivo=num*(-1);
	
	Escribir "El numero ",num " en positivo ahora es: ",numPositivo;
		sino 
	Escribir "Porfa ingrese un numero negativo";
	
		FinSi

		FinPara
	
FinProceso
