'Problema 2'

def main():
    while True:
        try:
            input_string = input("Ingrese las calificaciones separadas por comas: ")
            calificaciones = input_string.split(',')
            calificaciones_enteros = []

            for calificacion in calificaciones:
                calificacion = calificacion.strip()  # Eliminar todos los espacios en blanco que hay
                calificacion_entero = int(calificacion)
                calificaciones_enteros.append(calificacion_entero)

            print("Calificaciones en entero:", calificaciones_enteros)
            break  # Terminar todo el ejercicio en caso no haya observaciones

        except ValueError:
            print("Error: Asegúrese de ingresar solo números enteros separados por comas.")

if __name__ == "__main__":
    main()
