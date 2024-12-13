from animal import Animal

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
        Animal()