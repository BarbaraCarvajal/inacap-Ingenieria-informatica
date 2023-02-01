
# hacer programa que arroje caracteres del 
# codigo ascii desde 97 al 110
# o sea : abc... hasta la n

"""print(ord("@"))
print(chr(64))"""

for x in range(97,111):
    print(chr(x), end=" ")
print()
i=97
while i<=110:
    print(chr(i),end=" ")
    i += 1

"""print (chr(97))"""