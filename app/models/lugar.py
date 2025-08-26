class Lugar:
    def __init__(self,nombre: str, descripcion: str, enemigos, jefe: "enemigos"):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__enemigos = enemigos
        self.__jefe = jefe 
        
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor
    
    @property
    def descripcion (self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, valor):
        self.__descripcion = valor
        
    @property
    def enemigos(self):
        return self.__enemigos 
    
    @enemigos.setter
    def enemigos(self, lista): 
        self.__enemigos = lista
        
    @property
    def jefe (self):
        return self.__jefe
    
    @jefe.setter
    def jefe(self, valor):
        self.__jefe = valor