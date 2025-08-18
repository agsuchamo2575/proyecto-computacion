class Raza: 
    def __init__(self, nombre:str, descripcion: str, estadisticas):
        self.__nombre = nombre
        self.__descripcion = descripcion 
        self.__estadisticas = estadisticas
    
    @property
    def nombre(self):   
        return self.__nombre
    
    @nombre.setter 
    def nombre(self, nombre):
       self.__nombre = nombre  