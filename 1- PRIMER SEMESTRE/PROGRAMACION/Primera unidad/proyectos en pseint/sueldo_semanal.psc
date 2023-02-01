Proceso sin_titulo
	Definir horas,extras, sueldo Como Entero;
	Escribir 'digite horas trabajadas';
	Leer horas;
	Si horas<=40 Entonces
		Escribir 'el salario semanal es: ',horas*1600;
	SiNo
		extras <- horas-40;
		sueldo<-extras*2000+64000;
		Escribir 'el salario semanal es: ',sueldo,' con ',extras,' horas extras';
	FinSi
FinProceso
