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
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.__hauteur * self.getLongueur() * self.getLargeur()

rectangle=Rectangle(5, 10)
print(rectangle.perimetre())
print(rectangle.surface())
print(rectangle.getLongueur())
print(rectangle.getLargeur())

parallelepipede=Parallelepipede(5, 10, 15)

print(parallelepipede.volume())