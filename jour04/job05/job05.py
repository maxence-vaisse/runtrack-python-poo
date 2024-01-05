class Forme:
    def aire(self):
        self.__aire = 0
        return self.__aire
    
class Rectangle(Forme):
    def __init__(self, longueur, hauteur):
        self.__longueur = longueur
        self.__hauteur = hauteur

    def aire(self):
        aire = self.__hauteur * self.__longueur
        return aire
    
    def getLongueur(self):
        return self.__longueur
    
    def getHauteur(self):
        return self.__hauteur
    
    def setLongueur(self, longueur):
        self.__longueur = longueur

    def setHauteur(self, hauteur):
        self.__hauteur = hauteur

class Cercle(Forme):
    def __init__(self, rayon):
        self.__rayon = rayon

    def aire(self):
        aire = 3.14 * self.__rayon * self.__rayon
        return aire
    
    def getRayon(self):
        return self.__rayon
    
    def setRayon(self, rayon):
        self.__rayon = rayon
        
rectangle = Rectangle(13, 25)
cercle = Cercle(10)

print("L'aire du rectangle est :", rectangle.aire())

print("L'aire du cercle est :", cercle.aire())