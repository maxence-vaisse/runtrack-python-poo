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

rectangle = Rectangle(5, 9)

print("L'aire du rectangle est :", rectangle.aire())