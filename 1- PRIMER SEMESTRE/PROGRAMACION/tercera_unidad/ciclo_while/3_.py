"""Obtener el promedio de edades de un grupo (n) de personas. 
Se deben solicitar las edades y 
terminar el proceso cuando se ingrese una edad igual a 0, 
para finalmente mostrar el promedio 
o el mensaje “No ingresó ninguna edad” 
en el caso de ingresar como primera edad un cero.  
Pista: Uso de acumuladores.  """


edad = 0
suma_edad = 0
x = 0

cantidad = int(input("¿Cuántos valores ingresará?"))
while x <= cantidad-1:
    edad = int(input("Ingrese una edad: "))
    suma_edad = suma_edad + edad
    x += 1
    
    if edad == 0:
        #cantidad = cantidad -1
        print("No ingresó ninguna edad")
promedio = suma_edad/cantidad
print(f"El promedio de edad es: {promedio:.2f}")

