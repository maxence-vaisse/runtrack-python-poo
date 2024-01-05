class Forme:
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
    def aire(self):
        return self.__longueur * self.__largeur
    
rectangle = Rectangle(7, 10)
print(rectangle.aire())