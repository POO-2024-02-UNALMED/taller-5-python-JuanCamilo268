from animal import Animal

class Reptil(Animal):
    _listado = []
    serpientes = 0
    iguanas = 0
    def __init__(self, nombre = None, edad = None, habitat = None, genero = None, color = None, largo = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._colorEscamas = color
        self._largoCola = largo
        Reptil._listado.append(self)
        Animal()