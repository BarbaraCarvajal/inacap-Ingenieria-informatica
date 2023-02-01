"""
Realizar un programa que lea los lados de n triángulos, e informar:
a) De cada uno de ellos, qué tipo de triángulo es: 
equilátero (tres lados iguales), isósceles (dos lados iguales), 
o escaleno (ningún lado igual)
b) Cantidad de triángulos de cada tipo.
"""
equilatero = 0
isosceles = 0
escaleno = 0

cantidad = int(input("¿La información de cuántos triangulos ingresará?\n"))

for x in range(cantidad):
    primer_lado = float(input("Lado uno: \n"))
    segundo_lado = float(input("Lado dos: \n"))
    tercer_lado = float(input("Lado tres: \n"))
    if primer_lado == segundo_lado  and primer_lado == tercer_lado:
        print("Tipo de triangulo: Equilatero")
        equilatero = equilatero + 1
    elif primer_lado == segundo_lado or primer_lado == tercer_lado or tercer_lado == segundo_lado:
        print("Tipo de triangulo: Isosceles")
        isosceles = isosceles + 1
    elif primer_lado != segundo_lado and segundo_lado != tercer_lado:
        print("Tipo de triangulo: Escaleno")
        escaleno = escaleno +1

print("Totales")
print(f"Equilateros: {equilatero}")
print(f"Isosceles: {isosceles}")
print(f"Escalenos: {escaleno}")