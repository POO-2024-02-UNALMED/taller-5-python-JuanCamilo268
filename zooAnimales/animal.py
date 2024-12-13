class Animal:
    _totalAnimales = 0
    def __init__(self, nombre = None, edad = None, habitat = None, genero = None, zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales +=1

    def setNombre(self, nombre):
        self._nombre = nombre
    def setEdad(self, edad):
        self._edad = edad
    def setHabitat(self, habitat):
        self._habitat = habitat
    def setGenero(self, genero):
        self._genero = genero
    def setZona(self, zona):
        self._zona = zona

    def getNombre(self):
        return self._nombre
    def getEdad(self):
        return self._edad
    def getHabitat(self):
        return self._habitat
    def getGenero(self):
        return self._genero
    def getZona(self):
        return self._zona