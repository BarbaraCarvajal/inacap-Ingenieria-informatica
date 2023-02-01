Proceso calculadora
	Definir num1,num2,resultado Como Real;
	Definir op Como Caracter;
	Escribir 'Calculaora';
	Escribir 'Ingrese la operacion que desea realizar ';
	Escribir 'suma = + ';
	Escribir 'Resta = -';
	Escribir 'Division = /';
	Escribir 'Multiplicacion = *';
	Leer op;
	Escribir 'Ingrese el primer numero';
	Leer num1;
	Escribir 'Ingrese el segundo numero';
	Leer num2;
	Si op='+' Entonces
		resultado <- num1+num2;
	Sino
		Si op='-' Entonces
			resultado <- num1-num2;
		Sino
			Si op='/' Entonces
				Si num2<>0 Entonces
					resultado <- num1/num2;
				Sino
					Escribir 'NO SE PUEDE DIVIIR POR 0!! Precione cualquie tecla para salir ';
					esperar tecla;
					borrar pantalla;
				FinSi
			Sino
				Si op='*' Entonces
					resultado <- num1*num2;
				Sino
					Escribir 'Operador no valido';
				FinSi
			FinSi
		FinSi
	FinSi
	Escribir 'La clav es: ',op;
	Escribir 'El resultado de ',num1,op,num2,' es: ',resultado;
	
FinProceso

