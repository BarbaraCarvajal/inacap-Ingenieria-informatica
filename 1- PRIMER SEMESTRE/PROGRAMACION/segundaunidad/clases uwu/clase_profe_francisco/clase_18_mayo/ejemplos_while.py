

c=0

while c<5:
    print("Programacion "+str(c+1))
    c+=1


i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i+=1
print("fin")


i = 0 
while i<6:
    i+=1
    if i == 3:
        continue
    print(i)


print("mostrar un mensaje cuando se acabe un while")
i = 1 
while i < 6:
    print(i)
    i+= 1
else:
    print(f"{i} no es menor que 6, es igual")
    