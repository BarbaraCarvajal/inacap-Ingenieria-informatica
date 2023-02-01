Proceso tienda
	Definir precio, desc, clave Como real;
	definir producto Como Caracter;
	
	Escribir "Bienvenid@, ingrese el producto que desea llevar";
	leer producto;
	Escribir "Ingrese el precio del producto";
	leer precio;
	Escribir "Ingrese el codigo de descuento: 1 o 2 ";
	leer clave;
	Si clave = 1 Entonces
		desc=precio-(precio*0.1);
		Escribir "Ud lleva: ",producto " Y el total de la compra es: $",desc " con un 10% de descuento, precio original: $",precio;

	SiNo
		Si clave = 2 Entonces
			desc=precio-(precio*0.2);
			Escribir "Ud lleva: ",producto " Y el total de la compra es: $",desc " con un 20% de descuento, precio original: $",precio;
		SiNo
			Escribir "Codigo erroneo";
		Fin Si
	Fin Si
	
FinProceso
