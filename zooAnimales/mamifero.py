import animal

class Mamifero(animal.Animal):
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
    
    def getPelaje(self):
        return self._pelaje
    def getPatas(self):
        return self._patas
    
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)
    
    def crearCaballo(self, nombre, edad, genero):
        juan = Mamifero(nombre, edad, "pradera", genero, True, 4)
        Mamifero.caballos += 1
        return juan
    def crearLeon(self, nombre, edad, genero):
        simba = Mamifero(nombre, edad, "selva", genero, True, 4)
        Mamifero.leones += 1
        return simba
    