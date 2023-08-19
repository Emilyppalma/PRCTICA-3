'pregunta 3 '
import math

class CIRCULO:
    def __init__(self, r):
        self.radio = r
    
    def calcular_area(self):
        area = math.pi * self.r ** 2
        return area

# Ejemplo de uso
if __name__ == "__main__":
    r = float(input("Ingrese el radio del círculo: "))
    circulo = CIRCULO(r)
    area = circulo.calcular_area()
    print(f"El área del círculo con radio {r} es: {area}")
