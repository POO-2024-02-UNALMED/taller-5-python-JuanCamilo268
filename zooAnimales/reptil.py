from .animal import Animal

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
        super()
    
    def setColorEscamas(self, color):
        self._colorEscamas = color
    def setLargoCola(self, largo):
        self._largoCola = largo
    
    def getColorEscamas(self):
        return self._colorEscamas
    def getLargoCola(self):
        return self._largoCola
    
    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "reptar"
    
    def crearIguana(nombre, edad, genero):
        mariajuana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        Reptil.iguanas += 1
        return mariajuana
    def crearSerpiente(nombre, edad, genero):
        morales = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        Reptil.serpientes += 1
        return morales
    
    def __str__(self):
        if self._zona != None:
            return "Mi nombre es {self._niombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero} la zona en la que me ubico es {self._zona}, en el " + str(self._zona.getZoo())
        else:
            return "Mi nombre es {self._niombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
