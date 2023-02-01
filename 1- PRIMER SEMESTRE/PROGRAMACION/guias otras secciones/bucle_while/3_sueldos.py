"""En una empresa trabajan n empleados cuyos
sueldos oscilan entre $100y $500, 
realizar un programa que lea los 
sueldos que cobra cada empleado e informe 
cuántos empleados cobran entre $100 y $300 y 
cuántos cobran más de $300. Además el programa 
deberá informar el importe que gasta la empresa 
en sueldos al personal."""



x = 1
sueldoPromedio = 0
sueldoAlto = 0
total = 0

cantidad = int(input("¿Cuántos sueldos ingresará?\n"))
while x <= cantidad:
        sueldo = int(input(f"Ingrese el sueldo del trabajador N°{x}\n"))
        total = total + sueldo
        x = x + 1
        if sueldo >= 100 and sueldo <=300:
            sueldoPromedio = sueldoPromedio +1
        elif sueldo >300 and sueldo <=500:
            sueldoAlto = sueldoAlto +1
            
print(f"Cantidad de trabajadores con sueldos entre $100 y $300: {sueldoPromedio}")
print(f"Cantidad de trabajadores con sueldos sobre $300 y hasta  $500: {sueldoAlto}")
print(f"Total en sueldos: $ {total}")