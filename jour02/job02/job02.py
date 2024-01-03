class Livre: # Création de la classe Livre
    def __init__(self, titre, auteur, nbpages): # Création de la méthode __init__ avec les attributs titre, auteur et nbpages
        self.__titre = titre # Création de l'attribut titre
        self.__auteur = auteur # Création de l'attribut auteur
        self.__nbpages = nbpages # Création de l'attribut nbpages

    def __setTitre__(self, titre): # Création de la méthode __setTitre__ avec l'attribut titre
        self.__titre = titre # Création de l'attribut titre

    def __getTitre__(self): # Création de la méthode __getTitre__
        return self.__titre # Retourne l'attribut titre
    
    def __setAuteur__(self, auteur): # Création de la méthode __setAuteur__ avec l'attribut auteur
        self.__auteur = auteur # Création de l'attribut auteur

    def __getAuteur__(self): # Création de la méthode __getAuteur__
        return self.__auteur # Retourne l'attribut auteur
    
    def __setNbpages__(self, nbpages): # Création de la méthode __setNbpages__ avec l'attribut nbpages
        if int == type(nbpages) and nbpages > 0:
            self.__nbpages = nbpages
        else:
            print("Le nombre de pages doit être un entier.")
            exit(1)

    def __getNbpages__(self): # Création de la méthode __getNbpages__
        return self.__nbpages # Retourne l'attribut nbpages
    
Livre1 = Livre("Harry Potter", "J.K. Rowling", 300) # Création de l'objet Livre1 avec les attributs titre, auteur et nbpages
print(Livre1.__getTitre__()) # Affiche l'attribut titre
print(Livre1.__getAuteur__()) # Affiche l'attribut auteur
print(Livre1.__getNbpages__()) # Affiche l'attribut nbpages
(Livre1.__setTitre__("Le Seigneur des Anneaux")) # Modifie l'attribut titre
(Livre1.__setAuteur__("J.R.R. Tolkien")) # Modifie l'attribut auteur
(Livre1.__setNbpages__(250)) # Modifie l'attribut nbpages
print(Livre1.__getTitre__()) # Affiche l'attribut titre
print(Livre1.__getAuteur__()) # Affiche l'attribut auteur
print(Livre1.__getNbpages__()) # Affiche l'attribut nbpages