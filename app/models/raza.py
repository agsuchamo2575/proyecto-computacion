class Raza:
    def __init__(self, descripcion: str):
        self.__descripcion = descripcion 
    
    #get de raza
    @property
    def descripcion(self):
        return self.__descripcion 
    
    #set de descripcion 
    @descripcion.setter
    def descripcion(self,valor):
        self.__descripcion = valor 
        
class Humano(Raza):
    def __init__(self):
        super().__init__(Humano) #llama al constructor de raza
    
    def determinacion(self): 
        print()

class NiñoBosque(Raza):
    def __init__(self):
        super().__init__(NiñoBosque)
    
    def determinacion(self):
        print()

class Gigante(Raza):
    def __init__(self):
        super().__init(Gigante)
        
    def determinacion(self):
        print()
    