class Animal: # Classe Animal
    def __init__(self, age=0, prenom=""): # Création de la méthode __init__ qui initialise les attributs de la classe
        self.age = age # Création de l'attribut age
        self.prenom = prenom # Création de l'attribut prenom
    def viellir(self): # Création de la méthode viellir
        self.age += 1 # Incrémentation de l'attribut age
        return self.age # Retourne l'age
    def nommer(self, prenom): # Création de la méthode nommer
        self.prenom = prenom # Affectation de l'attribut prenom
        return self.prenom # Retourne le prenom
Luna = Animal() # Création d'un objet Luna de la classe Animal

print("L'age de l'animal est",Luna.age,"ans") # Affiche l'age de l'animal
print("L'age de l'animal vieux",Animal(0, "Luna").viellir(),"ans") # Affiche l'age de l'animal vieux
print("L'animal s'apelle",Animal(0, "Luna").nommer("Luna")) # Affiche le prenom de l'animal