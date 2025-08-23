class Clase:

    def __init__(self, descripcion: str, daño: float, armadura: float, vida: float):
        self.__descripcion = descripcion
        self.__daño = daño
        self.__armadura = armadura
        self.__vida = vida

    #Get de la descripción
    @property
    def descripcion(self):
        return self.__descripcion
    
    #Set de la descripcion
    @descripcion.setter
    def descripcion(self, valor): 
        self.__descripcion = valor

    #Get del daño
    @property
    def daño(self):
        return self.__daño
    
    #Set del daño
    @daño.setter
    def daño(self, valor):
        self.__daño = valor

    #Get de la armadura
    @property
    def armadura(self):
        return self.__armadura
    
    #Set de la armadura
    @armadura.setter
    def armadura(self, valor):
        self.__armadura = valor
    
    @property
    #Get de la vida
    def vida(self):
        return self.__vida
    
    #Set de la armadura
    @vida.setter
    def vida(self, valor):
        self.__vida = valor
    
#Creacion de clases hijas
class Arquero(Clase):
    def __init__(self, descripcion, daño, armadura, vida):
        super().__init__(descripcion, daño, armadura, vida)

    def tiro_certero(self):
        print("Este método usaría la habilidad 'Tiro Certero'. "
              "En el juego real, haría un ataque más fuerte que el normal a un enemigo seleccionado, "
              "ignorando parte de su armadura o aplicando daño crítico.")

class Guerrero(Clase):
    def __init__(self, descripcion, daño, armadura, vida):
        super().__init__(descripcion, daño, armadura, vida)
    
    def golpe_helado(self):
         print("Este método usaría la habilidad 'Golpe Helado'. "
              "En el juego real, haría daño a un enemigo y podría reducir temporalmente su velocidad o armadura.")

class MagoFuego(Clase):
    def __init__(self, descripcion, daño, armadura, vida, mana):
        super().__init__(descripcion, daño, armadura, vida)
        self.__mana = mana

    # Get del mana
    @property
    def mana(self):
        return self.__mana
    
    # Set del mana
    @mana.setter
    def mana(self, valor):
        self.__mana = valor

    def fuego_dragon(self):
        print("Este método usaría la habilidad 'Fuego Dragón'. "
              "En el juego real, lanzaría un ataque poderoso de fuego a todos los enemigos o a un objetivo principal, "
              "consumiendo mana y aplicando daño significativo.")

