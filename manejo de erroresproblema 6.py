import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "Está sobre el origen"
        elif self.x == 0:
            return "Está sobre el eje Y"
        elif self.y == 0:
            return "Está sobre el eje X"
        elif self.x > 0 and self.y > 0:
            return "Pertenece al primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Pertenece al segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Pertenece al tercer cuadrante"
        else:
            return "Pertenece al cuarto cuadrante"
    
    def vector(self, otro_punto):
        vector_resultante = (otro_punto.x - self.x, otro_punto.y - self.y)
        return vector_resultante
    
    def distancia(self, otro_punto):
        distancia = math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)
        return distancia

class Rectangulo:
    def __init__(self, punto_inicial=Punto(), punto_final=Punto()):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final
    
    def base(self):
        return abs(self.punto_final.x - self.punto_inicial.x)
    
    def altura(self):
        return abs(self.punto_final.y - self.punto_inicial.y)
    
    def area(self):
        return self.base() * self.altura()

# Crear puntos
A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto()

# Imprimir puntos
print("Punto A:", A)
print("Punto B:", B)
print("Punto C:", C)
print("Punto D:", D)

# Cuadrantes
print("Cuadrante Punto A:", A.cuadrante())
print("Cuadrante Punto C:", C.cuadrante())
print("Cuadrante Punto D:", D.cuadrante())

# Vectores
vector_AB = A.vector(B)
vector_BA = B.vector(A)
print("Vector AB:", vector_AB)
print("Vector BA:", vector_BA)

# Distancias
distancia_AB = A.distancia(B)
distancia_BA = B.distancia(A)
print("Distancia entre A y B:", distancia_AB)
print("Distancia entre B y A:", distancia_BA)

# Punto más lejano del origen
puntos = [A, B, C]
distancias_al_origen = [p.distancia(Punto()) for p in puntos]
indice_mas_lejano = distancias_al_origen.index(max(distancias_al_origen))
punto_mas_lejano = puntos[indice_mas_lejano]
print("Punto más lejano del origen:", punto_mas_lejano)

# Crear rectángulo
rectangulo = Rectangulo(A, B)
print("Rectángulo:", rectangulo)
print("Base del rectángulo:", rectangulo.base())
print("Altura del rectángulo:", rectangulo.altura())
print("Área del rectángulo:", rectangulo.area())
