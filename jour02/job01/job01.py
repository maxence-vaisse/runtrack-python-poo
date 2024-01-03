class Rectangle: # Création de la classe Rectangle
    def __init__(self, longeur, largeur): # Création de la méthode __init__ avec les attributs longeur et largeur
        self.__longeur = longeur # Création de l'attribut longeur
        self.__largeur = largeur # Création de l'attribut largeur

    def __setLongeur__(self, longeur): # Création de la méthode __setLongeur__ avec l'attribut longeur
        self.__longeur = longeur # Création de l'attribut longeur

    def __getLongeur__(self): # Création de la méthode __getLongeur__
        return self.__longeur # Retourne l'attribut longeur
    
    def __setLargeur__(self, largeur): # Création de la méthode __setLargeur__ avec l'attribut largeur
        self.__largeur = largeur # Création de l'attribut largeur

    def __getLargeur__(self): # Création de la méthode __getLargeur__
        return self.__largeur # Retourne l'attribut largeur
    
Rectangle1 = Rectangle(10, 5) # Création de l'objet Rectangle1 avec les attributs longeur et largeur
print(Rectangle1.__getLongeur__()) # Affiche l'attribut longeur
print(Rectangle1.__getLargeur__()) # Affiche l'attribut largeur
(Rectangle1.__setLongeur__(7)) # Modifie l'attribut longeur
(Rectangle1.__setLargeur__(3)) # Modifie l'attribut largeur
print(Rectangle1.__getLongeur__()) # Affiche l'attribut longeur
print(Rectangle1.__getLargeur__()) # Affiche l'attribut largeur