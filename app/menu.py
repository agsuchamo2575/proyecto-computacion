# Importa las clases necesarias para el juego
from models.juego import Juego
from models.personaje import Protagonista
from models.lugar import Lugar
from models.clase import Guerrero

# Crea una instancia del juego
juego = Juego()

# Ejemplo de creación de personaje y lugar (comentado porque era solo para pruebas)
# clase_guerrero = Guerrero("Guerrero", 100, 20, 5)
# personaje = Protagonista("Agus", 100, 20, 10, 5, clase_guerrero, ["espada", "escudo"], 150.0)
# lugar = Lugar("Bosque", "Un bosque misterioso", [], None)
# juego.personajes.append(personaje)
# juego.lugares.append(lugar)

# Función principal que muestra el menú y gestiona las opciones del usuario
def menu():
    while True:
        print('''
                1. Iniciar Partida
                2. Cargar Partida
                3. Guardar Partida
                4. Como Jugar
                5. Salir 
            ''')
        try:
            # Pide al usuario que elija una opción y la convierte a entero
            opcion = int(input("Elija una opción: "))
        except ValueError:
            # Si el usuario ingresa algo que no es un número, muestra un mensaje de error
            print("Entrada inválida, por favor seleccione una opción válida")
            continue

        if opcion == 1:
            # Opción para iniciar una nueva partida
            print("Inciando partida...")
        elif opcion == 2:
            # Opción para cargar una partida guardada
            print("Cargando partida: ")
            data = juego.cargar_partida()
            print("Datos de la partida cargados:")
            print(data.to_dict())
        elif opcion == 3:
            # Opción para guardar la partida actual
            print("Guardando partida...")
            juego.guardar_partida()
        elif opcion == 4:
            # Opción para mostrar instrucciones de cómo jugar
            print("Como Jugar")
        elif opcion == 5:
            # Opción para salir del juego
            print("Saliendo")
            break
        else:
            # Si el usuario ingresa un número fuera de las opciones válidas
            print("Entrada inválida, por favor seleccione una opcion válida")

# Ejecuta el menú solo si este archivo es el principal que se está ejecutando
if __name__== '__main__':
    menu()