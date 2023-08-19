"Manejo de errores"

'Problema 1'

# generando un programa que solicite al usuario una fracción
def get_fraction_input():
    while True:
        try:
            fraction = input("Ingrese una fracción en formato X/Y: ")
            x, y = map(int, fraction.split('/'))

#debe detectar estas excepciones y en caso esté mal, volver a preguntar
            if y == 0:
                raise ZeroDivisionError

            if x < y:
                raise ValueError

            return x, y

        except ValueError:
            print("Error: Asegúrese de ingresar números enteros y X >= Y.")
        except ZeroDivisionError:
            print("Error: El denominador (Y) no puede ser cero.")
            
# la respuesta nos debe mandar en %
def calculate_percentage(x, y):
    percentage = (x / y) * 100
#%<1
    if percentage < 1:
        return "E"
    elif percentage > 99:
        return "F"
    else:
        return f"{round(percentage)}%"

def main():
    while True:
        try:
            x, y = get_fraction_input()
            result = calculate_percentage(x, y)
            print("Cantidad de combustible en el tanque:", result)
            break  # tiene que terminar todo el ejercicio en caso no haya más problemas u observaciones
        except KeyboardInterrupt:
            print("\n¡Hasta luego!")
            break  

if __name__ == "__main__":
    main()

