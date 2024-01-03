class Voiture: # Création de la classe Voiture
    def __init__(self, marque, modele, année, killométrage, reservoir=50): # Création de la méthode __init__ avec les attributs marque, modele, année, killométrage et reservoir
        self.__marque = marque # Création de l'attribut marque
        self.__modele = modele # Création de l'attribut modele
        self.__année = année # Création de l'attribut année
        self.__killométrage = killométrage # Création de l'attribut killométrage
        self.__en_marche=False # Création de l'attribut en_marche
        self.__reservoir = reservoir # Création de l'attribut reservoir

    def _getMarque(self): # Création de la méthode __getMarque__
        return self.__marque # Retourne l'attribut marque
    
    def _getModele(self): # Création de la méthode __getModele__
        return self.__modele # Retourne l'attribut modele
    
    def _getAnnée(self): # Création de la méthode __getAnnée__
        return self.__année # Retourne l'attribut année
    
    def _getKillométrage(self): # Création de la méthode __getKillométrage__
        return self.__killométrage # Retourne l'attribut killométrage
    
    def _getEn_marche(self): # Création de la méthode __getEn_marche__
        return self.__en_marche # Retourne l'attribut en_marche
    
    def _setMarque(self, marque): # Création de la méthode __setMarque__ avec l'attribut marque
        self.__marque = marque # Création de l'attribut marque

    def _setModele(self, modele): # Création de la méthode __setModele__ avec l'attribut modele
        self.__modele = modele # Création de l'attribut modele
    
    def _setAnnée(self, année): # Création de la méthode __setAnnée__ avec l'attribut année
        self.__année = année # Création de l'attribut année
    
    def _setKillométrage(self, killométrage): # Création de la méthode __setKillométrage__ avec l'attribut killométrage
        self.__killométrage = killométrage # Création de l'attribut killométrage

    def _setEn_marche(self, en_marche): # Création de la méthode __setEn_marche__ avec l'attribut en_marche
        self.__en_marche = en_marche # Création de l'attribut en_marche

    def _demarrer(self): # Création de la méthode __demarrer__
        if self.__en_marche: # Si l'attribut en_marche est True
            print("La voiture est déjà en marche.") # Affiche un message d'erreur
        elif self.__reservoir > 5: # Si l'attribut reservoir est supérieur à 5
            self.__en_marche = True # Met à jour l'attribut en_marche
            print("La voiture a démarré.") # Affiche un message de confirmation
        else: # Si l'attribut reservoir est inférieur ou égal à 5
            print("La voiture n'a pas assez d'essence pour démarrer.") # Affiche un message d'erreur

    def _arreter(self): # Création de la méthode __arreter__
        if self.__en_marche: # Si l'attribut en_marche est True
            self.__en_marche = False # Met à jour l'attribut en_marche
            print("La voiture a été arrêtée.") # Affiche un message de confirmation
        else: # Si l'attribut en_marche est False
            print("La voiture est déjà arrêtée.") # Affiche un message d'erreur

    def _verifier_plein(self): # Création de la méthode __verifier_plein__
        return self.__reservoir # Retourne l'attribut reservoir
    
Cadillac = Voiture("Cadillac", "Escalade", 2009, 33000, 4) # Création de l'objet Cadillac avec les attributs marque, modele, année, killométrage et reservoir
print(Cadillac._getMarque()) # Affiche l'attribut marque
print(Cadillac._getModele()) # Affiche l'attribut modele
print(Cadillac._getAnnée()) # Affiche l'attribut année
print(Cadillac._getKillométrage()) # Affiche l'attribut killométrage
Cadillac._demarrer() # Met à jour l'attribut en_marche