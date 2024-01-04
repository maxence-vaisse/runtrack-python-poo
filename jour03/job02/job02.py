class CompteBancaire: # Création de la classe CompteBancaire
    def __init__(self, numero_compte, nom, prenom, solde,): # Constructeur de la classe CompteBancaire
        self.__numero_compte = numero_compte # Attribut privé de la classe CompteBancaire
        self.__nom = nom # Attribut privé de la classe CompteBancaire
        self.__prenom = prenom # Attribut privé de la classe CompteBancaire
        self.__solde = solde # Attribut privé de la classe CompteBancaire
        self.__decouvert = True # Attribut privé de la classe CompteBancaire

    def _getNumeroCompte(self): # Getter de l'attribut privé numero_compte
        return self.__numero_compte # Retourne l'attribut privé numero_compte
    
    def _getNom(self): # Getter de l'attribut privé nom
        return self.__nom # Retourne l'attribut privé nom
    
    def _getPrenom(self): # Getter de l'attribut privé prenom
        return self.__prenom # Retourne l'attribut privé prenom
    
    def _getSolde(self): # Getter de l'attribut privé solde
        return self.__solde # Retourne l'attribut privé solde
    
    def _setNumeroCompte(self, numero_compte): # Setter de l'attribut privé numero_compte
        self.__numero_compte = numero_compte # Attribut privé numero_compte

    def _setNom(self, nom): # Setter de l'attribut privé nom
        self.__nom = nom # Attribut privé nom

    def _setPrenom(self, prenom): # Setter de l'attribut privé prenom
        self.__prenom = prenom # Attribut privé prenom

    def _setSolde(self, solde): # Setter de l'attribut privé solde
        self.__solde = solde # Attribut privé solde

    def _afficher(self): # Méthode pour afficher les informations du compte
        print(f'Le compte numéro {self.__numero_compte} appartient à {self.__prenom} {self.__nom}.') # Affichage des informations du compte

    def _afficherSolde(self): # Méthode pour afficher le solde du compte
        print(f'Le solde du compte numéro {self.__numero_compte} est de {self.__solde} euros') # Affichage du solde du compte

    def _versement(self, montant): # Méthode pour effectuer un versement sur le compte
        self.__solde += montant # Incrémentation de l'attribut privé solde

    def _retrait(self, somme): # Méthode pour effectuer un retrait sur le compte
        if self.__solde - somme < 0 and self.__decouvert==False: # Si le solde du compte est inférieur à 0 et que le découvert est désactivé
            print("Erreur : Le solde du compte ne peut pas être négatif.") # Affichage d'une erreur
        elif somme > 0: # Si le montant du retrait est supérieur à 0
            self.__solde -= somme # Décrémentation de l'attribut privé solde
            self._afficherSolde() # Affichage du solde du compte
        else: # Sinon
            print("Erreur : Le montant doit être supérieur à 0.") # Affichage d'une erreur

    def _agios(self, taux): # Méthode pour appliquer des agios sur le compte
        self.__solde -= self.__solde * taux / 100 # Décrémentation de l'attribut privé solde
        self._afficherSolde() # Affichage du solde du compte

    def _virement(self, compte_destinataire, montant): # Méthode pour effectuer un virement vers un autre compte
        if self.__solde - montant < 0 and not self.__decouvert: # Si le solde du compte est inférieur à 0 et que le découvert est désactivé
            print("Opération impossible, le solde ne peut pas être négatif.") # Affichage d'une erreur
        else: # Sinon
            self.__solde -= montant # Décrémentation de l'attribut privé solde  
            compte_destinataire._versement(montant) # Incrémentation du solde du compte destinataire
            print("Virement effectué avec succès.") # Affichage d'un message de succès
            self._afficherSolde() # Affichage du solde du compte
            compte_destinataire._afficherSolde() # Affichage du solde du compte destinataire

compte1 = CompteBancaire(25, "Dupont", "Jean", 250000) # Création de l'objet compte1 de la classe CompteBancaire
compte2 = CompteBancaire(13, "Vaisse", "Maxence", -10000) # Création de l'objet compte2 de la classe CompteBancaire
compte1._afficher() # Affichage des informations du compte1
compte2._afficher() # Affichage des informations du compte2

print("\n") # Saut de ligne

compte1._afficherSolde() # Affichage du solde du compte1
compte1._versement(500) # Versement de 500 euros sur le compte1
compte1._afficherSolde() # Affichage du solde du compte1
compte1._retrait(1500) # Retrait de 1500 euros sur le compte1
compte1._afficherSolde() # Affichage du solde du compte1

print("\n") # Saut de ligne

compte2._afficherSolde() # Affichage du solde du compte2
compte1._virement(compte2, 1000) # Virement de 1000 euros du compte1 vers le compte2
compte2._agios(5) # Application d'agios de 5% sur le compte2