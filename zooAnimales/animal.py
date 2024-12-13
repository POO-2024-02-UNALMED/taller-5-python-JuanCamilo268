class Animal:
    _totalAnimales = 0
    def __init__(self, nombre = None, edad = None, habitat = None, genero = None, zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self.zona = zona
        Animal._totalAnimales +=1