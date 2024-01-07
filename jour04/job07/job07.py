import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class CarteBlackjack(Carte):
    def __init__(self, valeur, couleur):
        super().__init__(valeur, couleur)

    def valeur_blackjack(self):
        if self.valeur.isdigit():
            return int(self.valeur)
        elif self.valeur in ['Valet', 'Dame', 'Roi']:
            return 10
        elif self.valeur == 'As':
            return 11  # Supposons d'abord que l'As vaut 11 points

class Jeu:
    def __init__(self):
        self.paquet = []
        couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        for couleur in couleurs:
            for valeur in range(2, 11):
                self.paquet.append(CarteBlackjack(str(valeur), couleur))
            self.paquet.append(CarteBlackjack('Valet', couleur))
            self.paquet.append(CarteBlackjack('Dame', couleur))
            self.paquet.append(CarteBlackjack('Roi', couleur))
            self.paquet.append(CarteBlackjack('As', couleur))

    def melanger(self):
        random.shuffle(self.paquet)

    def donner_carte(self):
        return self.paquet.pop(0)

class Blackjack:
    def __init__(self):
        self.jeu = Jeu()
        self.jeu.melanger()
        self.main_joueur = []
        self.main_croupier = []

    def distribuer_cartes(self):
        self.main_joueur = [self.jeu.donner_carte(), self.jeu.donner_carte()]
        self.main_croupier = [self.jeu.donner_carte(), self.jeu.donner_carte()]

    def calculer_points(self, main):
        total = 0
        as_present = False
        for carte in main:
            total += carte.valeur_blackjack()
            if carte.valeur == 'As':
                as_present = True

        # Si l'As est présent dans la main et le total dépasse 21, changez la valeur de l'As à 1
        if as_present and total > 21:
            total -= 10

        return total

    def joueur_tour(self):
        while True:
            print("Votre main :")
            for carte in self.main_joueur:
                print(carte)
            points_joueur = self.calculer_points(self.main_joueur)
            print(f"Total des points : {points_joueur}")

            if points_joueur > 21:
                print("Vous avez dépassé 21. Vous avez perdu.")
                return -1

            choix = input("Prendre une carte ? (p/passer) : ").lower()
            if choix == 'p':
                return points_joueur
            elif choix != 'p' and choix != 'passer':
                nouvelle_carte = self.jeu.donner_carte()
                self.main_joueur.append(nouvelle_carte)

    def croupier_tour(self):
        while self.calculer_points(self.main_croupier) < 17:
            nouvelle_carte = self.jeu.donner_carte()
            self.main_croupier.append(nouvelle_carte)

    def jouer(self):
        self.distribuer_cartes()
        points_joueur = self.joueur_tour()

        if points_joueur != -1:
            self.croupier_tour()
            points_croupier = self.calculer_points(self.main_croupier)

            print("\nMain du croupier :")
            for carte in self.main_croupier:
                print(carte)
            print(f"Total des points du croupier : {points_croupier}")

            if points_croupier > 21 or points_joueur > points_croupier:
                print("Félicitations, vous avez gagné!")
            elif points_croupier > points_joueur:
                print("Le croupier a gagné.")
            else:
                print("Égalité.")

# Pour jouer une partie :
partie = Blackjack()
partie.jouer()