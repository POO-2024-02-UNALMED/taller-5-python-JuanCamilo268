class Zoologico:  
    def __init__(self, nombre = None, ubicacion = None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []
    
    def setNombre(self, nombre):
        self._nombre = nombre
    def setUbicacion(self, ub):
        self._ubicacion = ub
    
    def getNombre(self):
        return self._nombre
    def getUbicacion(self):
        return self._ubicacion
    
    def cantidadTotalAnimales(self):
        for zona in self._zonas:
