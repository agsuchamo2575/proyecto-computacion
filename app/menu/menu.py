def menu():
    while True:
        print('''
                1. Iniciar Partida
                2. Cargar Partida
                3. Guardar Partida
                4. Como Jugar
                5. Salir 
            ''')
        opcion = int(input("Elija una opción: "))
        
        if opcion == 1:
            print("Inciando partida...")
        elif opcion == 2:
            print("Cargando partida: ")
        elif opcion == 3:
            print("Guardar partida")
        elif opcion == 4:
            print("Como Jugar")
        elif opcion == 5:
            print("Saliendo")
            break
        else:
            print("Entrada inválida, por favor seleccione una opcion válida")

    
if __name__== '__main__':
    menu()