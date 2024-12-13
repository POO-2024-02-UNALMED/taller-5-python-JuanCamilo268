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
    
    def movimiento(self):
        return "volar"
    
    def crearHalcon(self, nombre, edad, genero):
        piyoto = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        Ave.halcones += 1
        return piyoto
    def crearAguila(self, nombre, edad, genero):
        murica = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        Ave.aguilas += 1
        return murica
    