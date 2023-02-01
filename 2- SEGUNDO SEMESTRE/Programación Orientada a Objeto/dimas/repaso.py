
def crearUsuario():
 
  usuario = input("Ingrese el nombre de su usuario: \n")
  print("Ingrese una contraseña de 4 digitos")
  clave = []
  for x in range(4):
    digito = input(int())
    if digito >= 0 and digito <= 9:
      clave.append(digito)
  print(clave)


    

print("Bienvenidos a mi CRUD 🐱")
print("____MENU____")

print("""
1) Crear usuario
2) Iniciar sesión
3) Salir
""")
opcion = int(input("Ingrese su opcion:\n"))

if opcion == 1:
  crearUsuario()