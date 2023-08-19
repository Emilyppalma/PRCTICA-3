# calculos.py
import operaciones

def main():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    
    print("Suma:", operaciones.suma(num1, num2))
    print("Resta:", operaciones.resta(num1, num2))
    print("Producto:", operaciones.producto(num1, num2))
    print("División:", operaciones.division(num1, num2))

if __name__ == "__main__":
    main()
