class Item:
    def __init__(self, nombre: str, tipo: str, efecto: float):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__efecto = efecto

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor
    
    @property
    def efecto(self):
        return self.__efecto
    
    @efecto.setter
    def efecto(self, valor):
        self.__efecto = valor

