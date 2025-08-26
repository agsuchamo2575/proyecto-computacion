class Juego:
    def __init__(self, personajes, lugares):
        self.__personajes = personajes
        self.__lugares = lugares 
    
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
    
        