class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []
    
    def display(self):
        print("Información del estudiante:")
        print("Nombre:", self.nombre)
        print("Número de Registro:", self.numero_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        if self.notas:
            print("Notas:", ", ".join(map(str, self.notas)))
    
    def setAge(self, edad):
        self.edad = edad
    
    def setNota(self, notas):
        self.notas = notas

# ejemplo de uso
if __name__ == "__main__":
    nombre = input("Ingrese el nombre del estudiante: ")
    numero_registro = input("Ingrese el número de registro del estudiante: ")

    alumno = Alumno(nombre, numero_registro)

    edad = int(input("Ingrese la edad del estudiante: "))
    alumno.setAge(edad)

    num_notas = int(input("Ingrese el número de notas del estudiante: "))
    notas = []
    for i in range(num_notas):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        notas.append(nota)
    alumno.setNota(notas)

    alumno.display()
