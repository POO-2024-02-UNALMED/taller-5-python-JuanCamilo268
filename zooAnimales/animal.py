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
    
    @classmethod
    def totalPorTipo(cls):
        from .mamifero import Mamifero
        from .ave import Ave
        from .reptil import Reptil
        from .pez import Pez
        from .anfibio import Anfibio
        return "Mamiferos : " + Mamifero.cantidadMamiferos() + "\nAves : " + Ave.cantidadAves() + "\nReptiles : " + Reptil.cantidadReptiles() + "\nPeces : " + Pez.cantidadPeces() + "\nAnfibios : " + Anfibio.cantidadAnfibios
    
    def __str__(self):
        if self._zona != None:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad + ", habito en " + self._habitat + " y mi genero es " + self._genero + "la zona en la que me ubico es " + self._zona + ", en el " + self._zona.getZoo()
        else:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + self._edad + ", habito en " + self._habitat + " y mi genero es " + self._genero  
    
    def movimiento(self):
        return "desplazarse"
    