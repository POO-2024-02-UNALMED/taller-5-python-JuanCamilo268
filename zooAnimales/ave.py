from animal import Animal

class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0
    def __init__(self, nombre = None, edad = None, habitat = None, genero = None, plumas = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._colorPlumas = plumas
        Ave._listado.append(self)
        Animal()

    def setColorPlumas(self, color):
        self._colorPlumas = color
    
    def getColorPlumas(self):
        return self._colorPlumas
    
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    