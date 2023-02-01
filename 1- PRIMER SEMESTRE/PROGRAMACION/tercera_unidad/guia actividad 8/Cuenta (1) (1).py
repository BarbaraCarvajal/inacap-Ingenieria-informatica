#HACER UN PROGRAMA QUE SIMULE UN CAJERO AUTOMATICO, CON UN SUELDO INICIAL DE 1000 DOLARES
#CON EL SIGUIENTE MENU
# 1. INGRESAR DINERO EN LA CUENTA
# 2. RETIRAR DINERO DE LA CUENTA
# 3. MOSTRAR DINERO DISPONIBLE
# 4. SALIR

saldo=1000

while True:

    print("\t.:MENU:. ")
    print ("1. Ingresar dinero en la cuenta")
    print ("2. Retirar dinero en la cuenta")
    print ("3. Mostrar dinero disponible")
    print ("4. Salir")
    print()
    opcion= int(input("Digite una opcion de menu:"))
    print()
    if opcion==1:
        extra=float(input("cuanto dinero desea ingresar a la cuenta"))
        saldo += extra
        
        print(f"dinero en la cuenta: {saldo}")

    elif opcion==2:
        retirar=float(input("cuanto dinero desea retirar a la cuenta"))
        if retirar>saldo:
            print("No tiene esa cantidad de nimero")
        else:
                saldo-=retirar
                print(f"Dinero en la cuenta: {saldo}")
    elif opcion==3:
        print(f"Dinero de la cuenta: {saldo}")
    elif opcion==4:
        print("Gracias por utilizar su cajero automatico")
        break
    else:
        print("error, se equivoco opcion de menu")