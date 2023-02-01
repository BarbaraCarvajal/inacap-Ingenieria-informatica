from conexion import conexion

def agregarASIG():
    conexion1=conexion()
    cursor1=conexion1.cursor()

    print("Agregar ASIGNATURA")

    codigo=int(input("Ingrese el el codigo de la asignatura: "))
    asignatura=input("Ingrese el nombre de la asignatura: ")
    semestre=int(input("Ingrese el semestre de la asignatura: "))
    

    datos=(codigo,asignatura,semestre)
    sql="insert into asignatura (codigo,asignatura,semestre) values (%s,%s,%s)"

    cursor1.execute(sql,datos)
    
    conexion1.commit()
    print("agregaste una asignatura nueva a la tabla")

def borrarASIG():
    conexion1=conexion()
    cursor1=conexion1.cursor()

    print("BORRAR USUARIO")
    MostrarASIG()

    eliminado=input("Ingrese el codigo de la asignatura a eliminar: ")

    cursor1.execute(f"delete from asignatura where codigo={eliminado}")
    conexion1.commit()

    print("ASIGNATURA  HA SIDO ELIMINADO")

def actualizarASIG():
    conexion1=conexion()
    cursor1=conexion1.cursor()
    
    print("actualizar alumno")

    MostrarASIG()

    seleccion=int(input("ingrese el codigo de la asignatura a actualizar: "))
    
    asignatura=input("ingrese el nombre de la asignatura : ")
    semestre=int(input("ingrese el semestre de la asignatura: "))

    cursor1.execute(f"update asignatura set asignatura = '{asignatura}', semestre= '{semestre}' where codigo='{seleccion}' ")
    conexion1.commit()
    print("ASIGNATURA ACTUALIZADA ")

def MostrarASIG():
    conexion1=conexion()
    cursor1=conexion1.cursor()

    print("Mostrar todos las asignaturas")

    cursor1.execute("select * from asignatura")
    for codigo,asignatura,semestre in cursor1:
        print(codigo,asignatura,semestre)

def consultarASIG():
    conexion1=conexion()
    cursor1=conexion1.cursor()
    
    consulta=input("Ingrese el codigo de la asignatura a buscar: ")
    
    print("AQUI LOS DATOS DE LA ASIGNATURA")
    cursor1.execute(f"select * from asignatura where codigo={consulta}")
    for codigo,asignatura,semestre in cursor1:
        print(codigo,asignatura,semestre)


#agregarASIG()
#MostrarASIG()
#consultarASIG()
#actualizarASIG()
#borrarASIG()