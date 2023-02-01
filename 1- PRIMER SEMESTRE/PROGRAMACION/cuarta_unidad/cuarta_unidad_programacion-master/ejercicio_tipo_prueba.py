import os
os.system("clear")

a = [[3,0,-3],[2,0,1]]
b = [[-1,2,0],[-2,3,0]]

m = len(a)
n = len(a[0])
if len(a) == len(b):
    c = []
    for i in range(m):
        c.append([])
        for j in range(n):
            c[i].append(a[i][j]+b[i][j])
    print(c)
else:
    print("No se puede realizar la suma, pues las dimensiones de las matrices no coinciden")