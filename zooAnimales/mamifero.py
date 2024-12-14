from .animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0
    def __init__(self, nombre = None, edad = None, habitat = None, genero = None, pelaje = None, patas = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)
        super()
    
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
    def setPatas(self, patas):
        self._patas = patas
    
    def isPelaje(self):
        return self._pelaje
    def getPatas(self):
        return self._patas
    
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)
    
    def crearCaballo(nombre, edad, genero):
        juan = Mamifero(nombre, edad, "pradera", genero, True, 4)
        Mamifero.caballos += 1
        return juan
    def crearLeon(nombre, edad, genero):
        simba = Mamifero(nombre, edad, "selva", genero, True, 4)
        Mamifero.leones += 1
        return simba
    
    def __str__(self):
        if self._zona != None:
            return "Mi nombre es {self._niombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero} la zona en la que me ubico es {self._zona}, en el " + str(self._zona.getZoo())
        else:
            return "Mi nombre es {self._niombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
