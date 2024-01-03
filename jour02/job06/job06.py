class Commande: # Création de la classe Commande
    
    menu = { # Création du dictionnaire menu
        "Big-Mac": 4.95, "Coca-Cola": 1.90, "Pates Carbonnara": 12.50, "McChicken": 4.50, "McFlurry": 4.0, "Eau": 0.5, "Café": 1.0, "Cookie": 1.30, # Création des clés et des valeurs du dictionnaire menu
    }

    def __init__(self, numero_de_commande): # Création de la méthode __init__ avec les attributs numero_de_commande, plats_commandes et statut
        self.__numero_commande = numero_de_commande # Création de l'attribut numero_commande
        self.__plats_commandes = {} # Création de l'attribut plats_commandes
        self.__statut = "en cours" # Création de l'attribut statut
    
    def ajouter_plat(self, nom_plat, quantite=1): # Création de la méthode ajouter_plat avec les attributs nom_plat et quantite
        if nom_plat in Commande.menu: # Si nom_plat est dans le dictionnaire menu
            if nom_plat not in self.__plats_commandes: # Si nom_plat n'est pas dans l'attribut plats_commandes
                self.__plats_commandes[nom_plat] = quantite # Ajouter nom_plat et quantite dans l'attribut plats_commandes
            else: # Sinon
                self.__plats_commandes[nom_plat] += quantite # Ajouter quantite à nom_plat dans l'attribut plats_commandes
        else: # Sinon
            print(f"Le plat '{nom_plat}' n'est pas disponible dans le menu.") # Afficher le message d'erreur

    def annuler_commande(self): # Création de la méthode annuler_commande
        self.__statut = "annulée" # Modifier l'attribut statut
        self.__plats_commandes.clear() # Vider l'attribut plats_commandes
    
    def payer(self): # Création de la méthode payer
        self.__statut = "terminée" # Modifier l'attribut statut
        self.__plats_commandes.clear() # Vider l'attribut plats_commandes

    def __calculer_total(self): # Création de la méthode __calculer_total
        return sum(Commande.menu[plat] * quantite for plat, quantite in self.__plats_commandes.items()) # Retourner la somme des prix des plats multipliés par leur quantité

    def __calculer_TVA(self, taux_tva): # Création de la méthode __calculer_TVA avec l'attribut taux_tva
        total = self.__calculer_total() # Création de la variable total
        return total * taux_tva / 100 # Retourner le total multiplié par le taux de TVA divisé par 100

    def afficher_commande(self): # Création de la méthode afficher_commande
        total = self.__calculer_total() # Création de la variable total
        print(f"Commande N°{self.__numero_commande}") # Afficher le numéro de la commande
        print(f"Statut de la commande: {self.__statut}") # Afficher le statut de la commande
        for plat, quantite in self.__plats_commandes.items(): # Pour chaque plat et quantité dans l'attribut plats_commandes
            prix = Commande.menu[plat] # Création de la variable prix
            print(f"{plat}: {prix}€ x {quantite}") # Afficher le plat, son prix et sa quantité
        print(f"Total à payer: {total}€") # Afficher le total à payer
        tva = self.__calculer_TVA(10) # Création de la variable tva
        print(f"TVA : {tva}€") # Afficher la TVA
    

commande1 = Commande(1) # Création de l'objet commande1
commande1.ajouter_plat("Big-Mac", 1) # Ajouter un plat à la commande1
commande1.ajouter_plat("Coca-Cola", 2) # Ajouter un plat à la commande1
commande1.ajouter_plat("Pates Carbonnara", 2) # Ajouter un plat à la commande1
commande1.ajouter_plat("McChicken", 1) # Ajouter un plat à la commande1
commande1.afficher_commande() # Afficher la commande1
commande1.payer() # Payer la commande1
commande1.afficher_commande() # Afficher la commande1
commande2 = Commande(2) # Création de l'objet commande2
commande2.ajouter_plat("Café", 2) # Ajouter un plat à la commande2
commande2.ajouter_plat("Cookie", 3) # Ajouter un plat à la commande2
commande2.afficher_commande() # Afficher la commande2
commande2.annuler_commande() # Annuler la commande2
commande2.afficher_commande() # Afficher la commande2