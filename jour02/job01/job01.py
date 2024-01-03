class Rectangle: # Création de la classe Rectangle
    def __init__(self, longeur, largeur): # Création de la méthode __init__ avec les attributs longeur et largeur
        self.__longeur = longeur # Création de l'attribut longeur
        self.__largeur = largeur # Création de l'attribut largeur

    def _setLongeur(self, longeur): # Création de la méthode __setLongeur__ avec l'attribut longeur
        self.__longeur = longeur # Création de l'attribut longeur

    def _getLongeur(self): # Création de la méthode __getLongeur__
        return self.__longeur # Retourne l'attribut longeur
    
    def _setLargeur(self, largeur): # Création de la méthode __setLargeur__ avec l'attribut largeur
        self.__largeur = largeur # Création de l'attribut largeur

    def _getLargeur(self): # Création de la méthode __getLargeur__
        return self.__largeur # Retourne l'attribut largeur
    
Rectangle1 = Rectangle(10, 5) # Création de l'objet Rectangle1 avec les attributs longeur et largeur
print(Rectangle1._getLongeur()) # Affiche l'attribut longeur
print(Rectangle1._getLargeur()) # Affiche l'attribut largeur
(Rectangle1._setLongeur(7)) # Modifie l'attribut longeur
(Rectangle1._setLargeur(3)) # Modifie l'attribut largeur
print(Rectangle1._getLongeur()) # Affiche l'attribut longeur
print(Rectangle1._getLargeur()) # Affiche l'attribut largeur