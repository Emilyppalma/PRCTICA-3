import mimodulo

if __name__ == "__main__":
    numeros_aleatorios = mimodulo.generar_numeros_aleatorios()
    
    print("Lista de números aleatorios generados:")
    mimodulo.mostrar_lista(numeros_aleatorios)
    
    print("Lista ordenada:")
    mimodulo.ordenar_y_mostrar(numeros_aleatorios)
