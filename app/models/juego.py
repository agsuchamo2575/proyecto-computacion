import json 
from .personaje import Personaje, Protagonista, Enemigo
from .lugar import Lugar
import os 

class Juego:
    def __init__(self):
        self.__personajes = []
        self.__lugares = []
        
    def to_dict(self):
        return {
            "personajes": [pj.to_dict() for pj in self.personajes],
            "lugares": [l.to_dict() for l in self.lugares]
        }
    def guardar_partida(self, filename = "partidas_guardadas/partida.json"):
        try:
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open (filename, "w") as f:
                json.dump(self.to_dict(), f, indent=4)
                print("Partida guardada exitosamente.")
        except Exception as e:
            print(f"Error al guardar la partida: {e}")

    @classmethod
    def from_dict(cls, data):
        juego = cls()
        juego.personajes = [Protagonista.from_dict(p) for p in data ["personajes"] ]
        juego.lugares = [Lugar.from_dict(p) for p in data ["lugares"] ]
        return juego
    
    @classmethod
    def cargar_partida(cls, filename="partidas_guardadas/partida.json"):
        with open(filename, "r") as f:
            data = json.load(f)
        return cls.from_dict(data) 


    @property
    def personajes(self):
        return self.__personajes
    
    @personajes.setter
    def personajes(self):
        return self.__personajes
    
    @personajes.setter
    def personajes(self, lista): 
        self.__personajes = lista 
    
    @property
    def lugares(self):
        return self.__lugares 
    
    @lugares.setter
    def lugares(self, lista):
        self.__lugares = lista
        
    def iniciarBatalla(self):
        print("¡Empieza la batalla!")
    
    def avanzarLugar(self):
        print("Avanzás al siguiente lugar")
    
        