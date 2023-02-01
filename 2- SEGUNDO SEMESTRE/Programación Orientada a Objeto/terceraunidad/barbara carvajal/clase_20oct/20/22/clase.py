import hashlib

#Encriptación

passEncrip = hashlib.new("sha1",b"123456")
#print(passEncrip.digest()) #digest retorna la cadena cifrada en binario
#print(passEncrip.hexdigest()) #hexdigest retorna la cadena cifrada en hexadecimal

# Otra forma de hacerlo
passEncrip2 = hashlib.sha1()
passEncrip2.update(b"123456")
#print(passEncrip2.digest())


# Forma para hacerlo con input 
contrasena = input("Ingrese su contraseña: ")
contrasenaEncripada = hashlib.sha384(contrasena.encode())

print(f"Forma no encriptada{contrasena}")
print(f"Contraseña encriptada con digest: {contrasenaEncripada.digest()}")
print(f"Contraseña encriptada con hexadecimal: {contrasenaEncripada.hexdigest()}")
print()



