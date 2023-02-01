Proceso numero_mayor
	definir n1, n2, n3 Como Entero;
	
	Escribir "Ingrese el primer numero";
	leer n1;
	
	Escribir "Ingrese el segundo numero";
	leer n2;
	
	Escribir "Ingrese el tercer numero";
	leer n3;
	
	si n1 = n2 y n2 = n3 y n3 = n1 Entonces
		Escribir "Todos los numeros son iguales";
	SiNo
		si n1 > n2 y n1 > n3 Entonces
			Escribir "El numero mayor es el primero, o sea: ",n1;
		SiNo
			si n2 > n1 y n2 >n3 Entonces
				Escribir "El numero mayor es el segundo, o sea: ",n2;
					SiNo
						Escribir "El numero mayor es el tercero, o sea: ",n3;
			FinSi
		FinSi
	FinSi
	
FinProceso
