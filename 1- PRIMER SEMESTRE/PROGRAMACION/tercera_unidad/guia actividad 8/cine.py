"""Un cine ofrece diversos tipos de películas, 
según el siguiente menú:  
Ø Estreno ($4.200)   
Ø Infantil ($2.500)   
Ø 3D ($5.500)   
Ø Documentales ($1.800)   
Ø Finalizar 
Determinar el monto total obtenido por concepto de venta de entradas. 
El menú se debe repetir hasta que se ingrese la opción de finalizar."""
while True:
    print("-----------------------")
    print(" Sistemas de ventas ")
    print("-----------------------")
    print("Menú")
    opcion = int(input("""
    1 - Estreno       $4.200
    2 - Infantil      $2.500
    3 - Pelicula 3D   $5.500
    4 - Documentales  $1.800
    5 - Salir      \n"""))
    #contadores 
    estreno = 0
    infantil = 0
    peli_3d = 0
    docu = 0
    #dinero
    estreno_1= 0
    infantil_2=0
    peli_3d_3=0
    docu_4 = 0

    if opcion == 1:
            estreno += 1
            estreno_1 = estreno *4200
    elif opcion == 2:
            infantil +=1
            infantil_2 = infantil*2500
    elif opcion == 3:
            peli_3d +=1
            peli_3d_3 = peli_3d*5500
    elif opcion == 4:
            docu +=1
            docu_4 = docu*1800
    elif opcion == 5:
        print(f"""
    Total de ventas de hoy: 
    Peliculas {estreno} y {estreno_1}""")
    break
    