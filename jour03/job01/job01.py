class Ville: # Création de la classe Ville
    def __init__(self, nom, nb_habitants): # Constructeur de la classe Ville
        self.__nom = nom # Attribut privé de la classe Ville
        self.__nb_habitants = nb_habitants # Attribut privé de la classe Ville

    def _getNom(self): # Getter de l'attribut privé nom
        return self.__nom # Retourne l'attribut privé nom
    
    def _getNbHabitants(self): # Getter de l'attribut privé nb_habitants
        return self.__nb_habitants # Retourne l'attribut privé nb_habitants
    
    def _setNom(self, nom): # Setter de l'attribut privé nom
        self.__nom = nom # Attribut privé nom
    
    def _setNbHabitants(self, nb_habitants): # Setter de l'attribut privé nb_habitants
        self.__nb_habitants = nb_habitants # Attribut privé nb_habitants

    
class Personne: # Création de la classe Personne
    def __init__(self, nom, age, ville): # Constructeur de la classe Personne
        self.__nom = nom # Attribut privé de la classe Personne
        self.__age = age # Attribut privé de la classe Personne
        self.__ville = ville # Attribut privé de la classe Personne

    def _getNom(self): # Getter de l'attribut privé nom
        return self.__nom # Retourne l'attribut privé nom
    
    def _getAge(self): # Getter de l'attribut privé age
        return self.__age # Retourne l'attribut privé age
    
    def _getVille(self): # Getter de l'attribut privé ville
        return self.__ville # Retourne l'attribut privé ville
    
    def _setNom(self, nom): # Setter de l'attribut privé nom
        self.__nom = nom # Attribut privé nom

    def _setAge(self, age): # Setter de l'attribut privé age
        self.__age = age # Attribut privé age

    def _setVille(self, ville): # Setter de l'attribut privé ville
        self.__ville = ville # Attribut privé ville

    def _ajouterPopulation(self): # Méthode pour ajouter une personne à la population
        self.__ville._setNbHabitants(self.__ville._getNbHabitants() + 1) # Incrémentation de l'attribut privé nb_habitants de la classe Ville    

Paris = Ville("Paris", 1000000) # Création de l'objet Paris de la classe Ville
Marseille = Ville("Marseille", 861635) # Création de l'objet Marseille de la classe Ville

print(f'Population de la ville de Paris: {Paris._getNbHabitants()} habitants') # Affichage de la population de la ville de Paris
print(f'Population de la ville de Marseille: {Marseille._getNbHabitants()} habitants') # Affichage de la population de la ville de Marseille

gens1 = Personne("John", 45, Paris) # Création de l'objet gens1 de la classe Personne
gens2 = Personne("Myrtille", 4, Paris) # Création de l'objet gens2 de la classe Personne
gens3 = Personne("Chloé", 18, Marseille) # Création de l'objet gens3 de la classe Personne

gens1._ajouterPopulation() # Ajout de gens1 à la population de Paris
gens2._ajouterPopulation() # Ajout de gens2 à la population de Paris
gens3._ajouterPopulation() # Ajout de gens3 à la population de Marseille

print(f'Mise à jour de la population de la ville de Paris: {Paris._getNbHabitants()} habitants') # Affichage de la population de la ville de Paris
print(f'Mise à jour de la population de la ville de Marseille: {Marseille._getNbHabitants()} habitants') # Affichage de la population de la ville de Marseille
