class Operation: # Création de la classe Operation
    def __init__(self, nombre1, nombre2): # Création de la méthode __init__ qui initialise les attributs de la classe
        self.nombre1 = nombre1 # Création de l'attribut nombre1
        self.nombre2 = nombre2 # Création de l'attribut nombre2

    def addition(self): # Création de la méthode addition
        return self.nombre1 + self.nombre2 # Retourne la somme des deux nombres

operateur = Operation(10, 5) # Création d'un objet operateur de la classe Operation
print (operateur.addition()) # Affiche la somme des deux nombres