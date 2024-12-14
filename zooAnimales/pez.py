from .animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0
    def __init__(self, nombre = None, edad = None, habitat = None, genero = None, color = None, cantidad = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._colorEscamas = color
        self._cantidadAletas = cantidad
        Pez._listado.append(self)
        super()
    
    def setColorEscamas(self, color):
        self._colorEscamas = color
    def setCantidadAletas(self, aletas):
        self._cantidadAletas = aletas

    def getColorEscamas(self):
        return self._colorEscamas
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
    
    def movimiento(self):
        return "nadar"
    
    def crearSalmon(nombre, edad, genero):
        laferte = Pez(nombre, edad, "oceano", genero, "rojo", 6)
        Pez.salmones += 1
        return laferte
    def crearBacalao(nombre, edad, genero):
        sheng = Pez(nombre, edad, "oceano", genero, "gris", 6)
        Pez.bacalaos += 1
        return sheng
    
    def __str__(self):
        if self._zona != None:
            return "Mi nombre es {self._niombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero} la zona en la que me ubico es {self._zona}, en el " + str(self._zona.getZoo())
        else:
            return "Mi nombre es {self._niombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
