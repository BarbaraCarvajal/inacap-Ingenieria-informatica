Proceso cubo_y_cuadrado
	Definir num, cubo, cuadrado, x Como Entero;
	cubo <- 0;
	cuadrado <- 0;
	Escribir 'Ingrese un numero';
	Leer num;
	x <- x+1;
	Para x<-num+1 Hasta num+5 Hacer
		num = num + 1;
		cuadrado <- num^2;
		cubo <- num^3;
		Escribir 'El cuadrado de ',num,' es: ',cuadrado,' y el cubo es ',cubo;
	FinPara
FinProceso

