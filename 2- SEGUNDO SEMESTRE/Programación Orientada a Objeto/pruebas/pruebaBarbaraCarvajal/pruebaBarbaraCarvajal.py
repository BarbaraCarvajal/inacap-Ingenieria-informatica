
#Clase padre:
class Persona():
    def __init__(self,nombre,apellido,edad,id):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.id = id

    def imprimirDatos(self):
        print(f"""
Nombre: {self.nombre}
Apellido: {self.apellido}
Edad: {self.edad}
ID: {self.id}""")
    
    def saludar(self):
        print(f"{self.nombre} esta saludando :D")
    
    def despedirse(self):
        print(f"{self.nombre} esta despidiendose :D")

#Clases hijos:
class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, id, especialidad, jornada):
        super().__init__(nombre, apellido, edad, id)
        self.especialidad = especialidad
        self.jornada = jornada
    
    def imprimirDatos(self):
        super().imprimirDatos()
        print(f"Especialidad: {self.especialidad}")
        print(f"Jornada: {self.jornada}")

    def darClases(self):
        print(f"{self.nombre} esta dando clases de {self.especialidad}")
    
    def pasarLista(self):
        print(f"{self.nombre} esta pasando la lista de la clase {self.especialidad}")

    def evaluar(self):
        print(f"{self.nombre} esta evaluando a sus alumnos de la materia {self.especialidad}")    

class Funcionario(Persona):
    def __init__(self, nombre, apellido, edad, id, salaEncargada, antiguedad):
        super().__init__(nombre, apellido, edad, id)
        self.salaEncargada = salaEncargada
        self.antiguedad = antiguedad

    def imprimirDatos(self):
        super().imprimirDatos()
        print(f"Sala encargada: {self.salaEncargada}")
        print(f"Antiguedad: {self.antiguedad}")

    def ordenarSala(self):
        print(f"{self.nombre} Esta ordenando la sala {self.salaEncargada}")
    
    def cerrarSala(self):
        print(f"{self.nombre} esta cerrado la sala {self.salaEncargada}")
    
    def abrirSala(self):
        print(f"{self.nombre} esta abriendo la sala {self.salaEncargada}")

class Alumno(Persona):
    def __init__(self, nombre, apellido, edad, id, sala, curso):
        super().__init__(nombre, apellido, edad, id)
        self.sala = sala
        self.curso = curso
    
    def imprimirDatos(self):
        super().imprimirDatos()
        print(f"Sala: {self.sala}")
        print(f"Curso: {self.curso}")

    def rendirPrueba(self):
        print(f"Alumno {self.nombre} esta rindiendo una prueba.")

    def salirRecreo(self):
        print(f"Alumno {self.nombre} esta saliendo a recreo :D")
    
    def estudiar(self):
        print(f"Alumno {self.nombre} esta estudiando en {self.curso} :D")

#main        

profesor1 = Profesor("Pedro", "Gutierrez", 45, 2023655, "Matematicas", "Diurno")
print("Primer profesor")
profesor1.imprimirDatos()
print("Metodos:")
profesor1.saludar()
profesor1.despedirse()
profesor1.darClases()
profesor1.pasarLista()
profesor1.evaluar()
print()

profesor2 = Profesor("Marcela", "Paz", 55, 2044455, "Lenguaje", "Vespertino")
print("Segundo profesor")
profesor2.imprimirDatos()
print("Metodos:")
profesor2.saludar()
profesor2.despedirse()
profesor2.darClases()
profesor2.pasarLista()
profesor2.evaluar()
print()

funcionario1 = Funcionario("Francisco", "Saez", 27, 1823641, "a45", 5)
print("Primer funcionario")
funcionario1.imprimirDatos()
print("Metodos")
funcionario1.saludar()
funcionario1.despedirse()
funcionario1.ordenarSala()
funcionario1.cerrarSala()
funcionario1.abrirSala()
print()

funcionario2 = Funcionario("Romina", "Perez", 35, 1825566, "a50", 10)
print("Segundo funcionario")
funcionario2.imprimirDatos()
funcionario2.saludar()
funcionario2.despedirse()
funcionario2.ordenarSala()
funcionario2.cerrarSala()
funcionario2.abrirSala()
print()

alumno1 = Alumno("Camilo", "Monsalves", 15, 2036456, "a45", "Segundo Medio")
print("Primer Alumno")
alumno1.imprimirDatos()
print("Metodos")
alumno1.saludar()
alumno1.despedirse()
alumno1.rendirPrueba()
alumno1.salirRecreo()
alumno1.estudiar()
print()

alumno2 = Alumno("Maria", "Alvarado", 18, 2036333, "a50", "Cuarto Medio")
print("Segundo Alumno")
alumno2.imprimirDatos()
print("Metodos")
alumno2.saludar()
alumno2.despedirse()
alumno2.rendirPrueba()
alumno2.salirRecreo()
alumno2.estudiar()
