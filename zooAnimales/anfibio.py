from animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0
    def __init__(self, nombre = None, edad = None, habitat = None, genero = None, color = None, veneno = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._colorPiel = color
        self._venenoso = veneno
        Anfibio._listado.append(self)
        Animal()
    
    def setColorPiel(self, color):
        self._colorPiel = color
    def setVenenoso(self, veneno):
        self._venenoso = veneno

    def getColorPiel(self):
        return self._colorPiel
    def getVenenoso(self):
        return self._venenoso