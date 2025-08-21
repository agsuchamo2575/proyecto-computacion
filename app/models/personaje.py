class Personaje:
    def __init__(self, nombre: str, vida: float, daño: float, armadura: float, nivel: int, clase, items):
        self.__nombre = nombre
        self.__vida = vida
        self.__daño = daño
        self.__armadura = armadura
        self.__nivel = nivel
        self.__clase = clase
        self.__items = items

    # Get de nombre
    @property
    def nombre(self):
        return self.__nombre
    
    # Set de nombre
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    # Get de vida
    @property
    def vida(self):
        return self.__vida
    
    # Set de vida
    @vida.setter
    def vida(self, valor):
        self.__vida = valor
    
    # Get de daño
    @property
    def daño(self):
        return self.__daño
    
    # Set de daño
    @daño.setter
    def daño(self, valor):
        self.__daño = valor
    
    # Get de armadura
    @property
    def armadura(self):
       return self.__armadura
    
    # Set de armadura
    @armadura.setter
    def armadura(self, valor):
        self.__armadura = valor
    
    # Get de nivel
    @property
    def nivel(self):
        return self.__nivel
    
    # Set de nivel
    @nivel.setter
    def nivel(self, valor):
        self.__nivel = valor
 
    # Metodos
    def atacar(self):
        print("El personaje ataca")
    
    def recibir_daño(self):
        print("El personaje recibe daño")

    def defender(self):
        print("El personaje se defiende")
    
    def usar_item(self):
        print("El personaje usa un item")

    def usar_habilidad_especial(self):
        print("El personaje utiliza una hablidad especial")

class Protagonista(Personaje):
    def __init__(self, nombre, vida, daño, armadura, nivel, clase, items, experiencia):
        super().__init__(nombre, vida, daño, armadura, nivel, clase, items)
        self.__experiencia = experiencia

    #Get de experiencia
    @property
    def experiencia(self):
        return self.__experiencia

    #Set de experiencia
    @experiencia.setter
    def experiencia(self, valor):
        self.__experiencia = valor

class Enemigo(Personaje):
    def __init__(self, nombre, vida, daño, armadura, nivel, clase, items, es_jefe):
        super().__init__(nombre, vida, daño, armadura, nivel, clase, items)
        self.__es_jefe = es_jefe
    
    # Get de es_jefe
    @property
    def es_jefe(self):
        return self.__es_jefe
    
    # Set de es_jefe
    @es_jefe.setter
    def es_jefe(self, valor):
        self.__es_jefe = valor
    