class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}  # Dictionnaire pour représenter les plats commandés
        self.__statut_commande = "En cours"  # Statut par défaut

    # Méthode pour ajouter un plat à la commande
    def ajouter_plat(self, nom_plat, prix_plat):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "En cours"}
            print(f"{nom_plat} ajouté à la commande.")
        else:
            print(f"{nom_plat} est déjà dans la commande.")

    # Méthode pour annuler une commande
    def annuler_commande(self):
        self.__plats_commandes.clear()
        self.__statut_commande = "Annulée"
        print("Commande annulée.")

    # Méthode privée pour calculer le total de la commande
    def __calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values())
        return total

    # Méthode pour afficher la commande avec son total à payer
    def afficher_commande(self):
        print(f"\nCommande n°{self.__numero_commande} - Statut : {self.__statut_commande}")
        for nom_plat, plat in self.__plats_commandes.items():
            print(f"{nom_plat}: {plat['prix']} € - Statut : {plat['statut']}")
        total = self.__calculer_total()
        print(f"Total à payer : {total} € (TVA incluse)")

    # Méthode pour calculer la TVA
    def calculer_tva(self):
        total = self.__calculer_total()
        tva = total * 0.2  # Taux de TVA de 20%
        return tva

# Exemple d'utilisation
ma_commande = Commande(123)

# Ajout de plats à la commande
ma_commande.ajouter_plat("Pizza", 12.5)
ma_commande.ajouter_plat("Burger", 8.75)

# Affichage de la commande
ma_commande.afficher_commande()

# Annulation de la commande
ma_commande.annuler_commande()

# Affichage de la commande après annulation
ma_commande.afficher_commande()