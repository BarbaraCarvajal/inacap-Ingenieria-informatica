# multiples formas, adptación 

class Animal:
  
  def ONOMATOPEYA(self):
    pass
  
class Perro(Animal):
  def ONOMATOPEYA(self):
    print("guau guau!")

class Gato(Animal):
  def ONOMATOPEYA(self):
    print("miau miau!")

class Ornitorrinco(Animal):
  def ONOMATOPEYA(self):
    print("ggrr!")

print("El perro dice: ")
perro1 = Perro()
perro1.ONOMATOPEYA()
print()
print("El gato dice: ")
gato1 = Gato()
gato1.ONOMATOPEYA()
print()
print("El ornitorrinco dice")
ornitorrinco1 = Ornitorrinco()
ornitorrinco1.ONOMATOPEYA()
print()

for x in Perro(), Gato(), Ornitorrinco():
  x.ONOMATOPEYA()

