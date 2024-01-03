class Livre: # Création de la classe Livre
    def __init__(self, titre, auteur, nbpages): # Création de la méthode __init__ avec les attributs titre, auteur et nbpages
        self.__titre = titre # Création de l'attribut titre
        self.__auteur = auteur # Création de l'attribut auteur
        self.__nbpages = nbpages # Création de l'attribut nbpages

    def _setTitre(self, titre): # Création de la méthode __setTitre__ avec l'attribut titre
        self.__titre = titre # Création de l'attribut titre

    def _getTitre(self): # Création de la méthode __getTitre__
        return self.__titre # Retourne l'attribut titre
    
    def _setAuteur(self, auteur): # Création de la méthode __setAuteur__ avec l'attribut auteur
        self.__auteur = auteur # Création de l'attribut auteur

    def _getAuteur(self): # Création de la méthode __getAuteur__
        return self.__auteur # Retourne l'attribut auteur
    
    def _setNbpages(self, nbpages): # Création de la méthode __setNbpages__ avec l'attribut nbpages
        if int == type(nbpages) and nbpages > 0:
            self.__nbpages = nbpages
        else:
            print("Le nombre de pages doit être un entier.")
            exit(1)

    def _getNbpages(self): # Création de la méthode __getNbpages__
        return self.__nbpages # Retourne l'attribut nbpages
    
Livre1 = Livre("Harry Potter", "J.K. Rowling", 300) # Création de l'objet Livre1 avec les attributs titre, auteur et nbpages
print(Livre1._getTitre()) # Affiche l'attribut titre
print(Livre1._getAuteur()) # Affiche l'attribut auteur
print(Livre1._getNbpages()) # Affiche l'attribut nbpages
(Livre1._setTitre("Le Seigneur des Anneaux")) # Modifie l'attribut titre
(Livre1._setAuteur("J.R.R. Tolkien")) # Modifie l'attribut auteur
(Livre1._setNbpages(250)) # Modifie l'attribut nbpages
print(Livre1._getTitre()) # Affiche l'attribut titre
print(Livre1._getAuteur()) # Affiche l'attribut auteur
print(Livre1._getNbpages()) # Affiche l'attribut nbpages