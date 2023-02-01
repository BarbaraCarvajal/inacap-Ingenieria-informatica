Proceso sin_titulo
	Definir sueldo,n_empleados,sueldo_bajo,sueldo_alto, total_sueldos Como Entero
	sueldo_bajo <- 0
	sueldo_alto <- 0
	n_empleados <- 0
	total_sueldos = 0;
	Escribir 'Cuantos sueldos ingresara?'
	Leer n_empleados
	Escribir 'Por favor ingresar los sueldos de los empleados'
	Para x<-1 Hasta n_empleados Hacer
		Leer sueldo
		total_sueldos = total_sueldos + sueldo
		Si sueldo>=100 Y sueldo<=300 Entonces
			sueldo_bajo <- sueldo_bajo+1
		SiNo
			Si sueldo>300 y sueldo <=500 Entonces
				sueldo_alto <- sueldo_alto+1
			SiNo
				Escribir 'Porfavor ingrese un valor valido, presione cualquier tecla para salir'
				Esperar Tecla
				Borrar Pantalla
			FinSi
		FinSi
	FinPara
	Escribir 'La cantidad de sueldos altos son: ',sueldo_alto,' Y los sueldos bajos son: ',sueldo_bajo
	Escribir "Total sueldos: ", total_sueldos;
FinProceso
