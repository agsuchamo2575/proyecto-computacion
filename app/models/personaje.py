class Personaje:
    def __init__(self, nombre: str, vida: float, daño: float, armadura: float, nivel: int, clase, items):
        self.__nombre = nombre
        self.__vida = vida
        self.__daño = daño
        self.__armadura = armadura
        self.__nivel = nivel
        self.__clase = clase
        self.__items = []

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

    # Get de clase
    @property
    def clase(self):
        return self.__clase

    # Set de clase
    @clase.setter
    def clase(self, valor):
        self.__clase = valor

    # Get de items
    @property
    def items(self):
        return self.__items

    # Set de items
    @items.setter
    def items(self, valor):
        self.__items = valor

    # Metodos
    def atacar(self):
        print("El personaje ataca")
    
    def recibir_daño(self):
        print("El personaje recibe daño, descontando armadura y efectos de defensa")

    def defender(self):
        print("El personaje se defiende, reduciendo daño de enemigos este turno")
    
    def usar_item(self, item):
        print("El personaje usa un item"
              "por ejemplo, curar vida o mejorar atributos temporalmente")

    def usar_habilidad_especial(self):
        print("El personaje utiliza una hablidad especial segun su clase"
              "por ejemplo, 'Tiro Certero', 'Golpe Helado' o 'Fuego Dragón'")


# Clase Protagonista
class Protagonista(Personaje):
    def __init__(self, nombre, vida, daño, armadura, nivel, clase, items, experiencia: float):
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
    
    def ganar_experiencia(self, cantidad):
        print("Aquí se sumaría a la experiencia actual del protagonista."
              "Si la experiencia alcanza el límite para subir de nivel, se llamaría al método 'subir_nivel'.")
    
    def subir_nivel(self):
        print("El protagonista sube de nivel."
              "Se incrementarían los atributos: vida, daño, armadura y posiblemente desbloqueo de habilidades."
              "También se podría reiniciar la experiencia acumulada para el siguiente nivel.")


    def to_dict(self):
        return{
            "nombre": self.nombre,
            "vida": self.vida,
            "daño": self.daño,
            "armadura": self.armadura,
            "nivel": self.nivel,
            "clase": self.clase.to_dict() if hasattr(self.clase, "to_dict") else self.clase,
            "items": self.items, 
            "experiencia": self.__experiencia 
        }
    
    @classmethod
    def from_dict(cls, data: dict): 
        return cls(
            nombre = data["nombre"],
            vida =data ["vida"],
            daño = data ["daño"],
            armadura = data ["armadura"],
            nivel = data ["nivel"],
            clase = data ["clase"], 
            items = data ["items"], 
            experiencia = data ["experiencia"]
        )
        
# Clase enemigo
class Enemigo(Personaje):
    def __init__(self, nombre, vida, daño, armadura, nivel, clase, items, es_jefe: bool, drop: list, recompensaExp: float):
        super().__init__(nombre, vida, daño, armadura, nivel, clase, items)
        self.__es_jefe = es_jefe
        self.__drop = drop   # Lista de Items que puede soltar
        self.__recompensaExp = recompensaExp   # Experiencia otorgada al morir
    
    # Get de es_jefe
    @property
    def es_jefe(self):
        return self.__es_jefe
    
    # Set de es_jefe
    @es_jefe.setter
    def es_jefe(self, valor):
        self.__es_jefe = valor
    
    # Get de drop
    @property
    def drop(self):
        return self.__drop

    #Set de drop
    @drop.setter
    def drop(self, valor):
        self.__drop = valor

    # Get de recompensaExp
    @property
    def recompensaExp(self):
        return self.__recompensaExp

    # Set de recompensaExp
    @recompensaExp.setter
    def recompensaExp(self, valor):
        self.__recompensaExp = valor
        
    def to_dict(self):
        return{
            "nombre": self.nombre,
            "vida": self.vida,
            "daño": self.daño,
            "armadura": self.armadura,
            "nivel": self.nivel,
            "clase": self.clase, 
            "items": self.items, 
            "es_jefe": self.es_jefe,
            "recompensaExp": self.recompensaExp, 
            "drop": self.drop
        }
    
    @classmethod
    def from_dict(cls, data: dict): 
        return cls(
            nombre = data["nombre"],
            vida =data ["vida"],
            daño = data ["daño"],
            armadura = data ["armadura"],
            nivel = data ["nivel"],
            clase = data ["clase"], 
            items = data ["items"], 
            es_jefe= data ["es_jefe"], 
            recompensaExp= data ["recompensaExp"], 
            drop = data ["drop"]
        )
prota = Protagonista("Agus", 100, 20, 10, 5, "Guerrera", ["espada", "escudo"], 150.0)
prota_dict = prota.to_dict()
print(prota_dict)

nuevo_prota = Protagonista.from_dict(prota_dict)
print(nuevo_prota.nombre, nuevo_prota.experiencia)


