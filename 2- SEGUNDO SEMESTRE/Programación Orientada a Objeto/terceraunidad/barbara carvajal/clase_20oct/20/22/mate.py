
print(sum(list(range(1,10))))


num1 = 1
num2 = 1

for x in range(10):
  operacion1 = num1 + num2
  num2 += 1
  if operacion1 >=20:
    operacion1 = num1 + num2
    num2 += 1

  print(operacion1)
