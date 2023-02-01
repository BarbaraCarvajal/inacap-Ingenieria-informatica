
texto1 = "los datos"
texto2 = "movil"
print(texto1[3] + texto2[1])

# in busca si una determinada frase o carácter
# está presente en una cadena.

txt = "Alumno Inacap de programación"
print("programación" in txt)

string_de_ejemplo = "Texto de ejemplo"
primera_palabra = string_de_ejemplo[0:5]
print(primera_palabra)

# len: muestra el largo del string consultado.

mensaje = "hola" + " " + "Mundo" #tambien se cuentan los espacios en blanco
print(len(mensaje))
s = "texto"
largo_del_texto = len(s)
print(largo_del_texto)

# find()
# muestra en que posición 
# empieza el string que se consulta.

mensaje = "hola mundo"
mensaje_1 = mensaje.find("mundo")
print(mensaje_1)

# count() Nos cuenta la cantidad de veces
# en que se repite el string consultado
# en una cadena

s = "palabra"
print(s.count("a"))

txt = "amo las manzanas, las manzanas son mi fruta preferida"
x = txt.count("manzanas", 10,24) #wtf?
print(x)

# replace() reemplaza un carácter por otro
# en una cadena.

s = "palabra"
print(s.replace("pa","tx"))

x = "papapepa"
print(x.replace("pa","tx"))

# upper() transforma todos los carácteres a mayúsculas.

s = "texTo"
print(s.upper())

# lower() transforma todos los carácteres a minúsculas.

s = "TEXTO"
print(s.lower())

# strip() remueve espacios y otros carácteres indeseables
# al principio y final del string.

s = "   PALABRA"
print(s.strip())