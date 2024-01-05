class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
    
    def getLongueur(self):
        return self.__longueur
    
    def getLargeur(self):
        return self.__largeur
    
    def setLongueur(self, longueur):
        self.__longueur = longueur

    def setLargeur(self, largeur):
        self.__largeur = largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return self.__hauteur * self.__longueur * self.__largeur

rectangle=Rectangle(5, 10)
print(rectangle.perimetre())
print(rectangle.surface())
print(rectangle.getLongueur())
print(rectangle.getLargeur())