from animal import Animal

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
        Animal()