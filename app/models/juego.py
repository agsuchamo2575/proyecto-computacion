import json 
from .personaje import Personaje, Protagonista, Enemigo
from .lugar import Lugar
class Juego:
    def __init__(self):
        self.__personajes = []
        self.__lugares = []
        
    def to_dic(self):
        return {
            "personajes": [personajes.to_dict() for p in self.personajes],
            "lugares": [lugar.to_dict() for l in self.lugares]
        }
    def save(self, filename = "./partidas_guardadas/partida.json"):
        with open (filename, "w") as f:
            json.dump(self.to_dict(), f, indent=4)
    
    @classmethod
    def from_dict(cls, data):
        juego = cls()
        juego.personajes = [Protagonista.from_dict(p) for p in data ["personajes"] ]
        juego.lugares = [Lugar.from_dict(p) for p in data ["lugares"] ]
        return juego
    
    @classmethod
    def loaf(cls, filename="partida.json"):
        with open(filaname, "r") as f:
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
        
    def guardarPartida(self):
        print("Partida Guardada")
        
    def cargarPartida(self):
        print("Partida cargada")
    
        