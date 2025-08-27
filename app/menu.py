from models.juego import Juego
from models.personaje import Protagonista
from models.lugar import Lugar
from models.clase import Guerrero

juego = Juego()

clase_guerrero = Guerrero("Guerrero", 100, 20, 5)
personaje = Protagonista("Agus", 100, 20, 10, 5, clase_guerrero, ["espada", "escudo"], 150.0)
lugar = Lugar("Bosque", "Un bosque misterioso", [], None)

juego.personajes.append(personaje)
juego.lugares.append(lugar)

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
            data = juego.cargar_partida()
            print("Datos de la partida cargados:")
            print(data.to_dict())
        elif opcion == 3:
            print("Guardando partida...")
            juego.guardar_partida()
        elif opcion == 4:
            print("Como Jugar")
        elif opcion == 5:
            print("Saliendo")
            break
        else:
            print("Entrada inválida, por favor seleccione una opcion válida")

    
if __name__== '__main__':
    menu()