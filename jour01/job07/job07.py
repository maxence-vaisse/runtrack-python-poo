class Personnage: # Création de la classe Personnage
    def __init__(self, x=0, y=0): # Création de la méthode __init__ qui initialise les attributs de la classe
        self.x = x # Création de l'attribut x
        self.y = y # Création de l'attribut y

    def gauche(self): # Création de la méthode gauche
        self.x -= 1 # Décrémentation de l'attribut x
        return (self.x, self.y) # Retourne les coordonnées du personnage
    def droite(self): # Création de la méthode droite
        self.x += 1 # Incrémentation de l'attribut x
        return (self.x, self.y) # Retourne les coordonnées du personnage
    def haut(self): # Création de la méthode haut
        self.y += 1 # Incrémentation de l'attribut y
        return (self.x, self.y) # Retourne les coordonnées du personnage
    def bas(self): # Création de la méthode bas
        self.y -= 1 # Décrémentation de l'attribut y
        return (self.x, self.y) # Retourne les coordonnées du personnage
    def position(self): # Création de la méthode position
        return "Personnage(" + str(self.x) + ", " + str(self.y) + ")" # Retourne les coordonnées du personnage
    
maxence = Personnage(13, -25) # Création d'un objet maxence de la classe Personnage
print (maxence.gauche()) # Affiche les coordonnées du personnage
print (maxence.droite()) # Affiche les coordonnées du personnage
print (maxence.haut()) # Affiche les coordonnées du personnage
print (maxence.bas()) # Affiche les coordonnées du personnage
print (maxence.position()) # Affiche les coordonnées du personnage²