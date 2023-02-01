Proceso positivos_y_negativos
	Definir n, x, neutros, negativos, positivos Como Entero;
	
	neutros=0;
	positivos=0;
	negativos=0;
	
	
	
	Para x=1 Hasta 20 con paso 1 Hacer
		
		Escribir "ingrese un numero";
		leer n;
		
		si n = 0 Entonces
			neutros = neutros + 1;
		SiNo
			si n > 0 Entonces
				positivos= positivos+1;
			sino 
				si n<0 Entonces
					negativos=negativos+1;
				FinSi
			FinSi
		FinSi
		
	FinPara
	
	Escribir "La cantidad de numeros positivos son: ",positivos;
	Escribir "La cantidad de numeros negativos son: ",negativos;
	Escribir "La cantidad de numeros neutros son: ",neutros;

FinProceso
