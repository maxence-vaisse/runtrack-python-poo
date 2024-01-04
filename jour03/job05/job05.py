class Personnage:
    def __init__(self, nom=str(), vie=int()):
        self.__nom = nom
        self.__vie = vie

    def _getNom(self):
        return self.__nom
    
    def _setNom(self, nom):
        self.__nom = nom

    def _getVie(self):
        return self.__vie
    
    def _setVie(self, vie):
        self.__vie = vie

    def _attaquer(self, personnage):
        print(f'{self.__nom} attaque {personnage._getNom()}')
        personnage._setVie(personnage._getVie() - 5)
        print(f'{personnage._getNom()} a {personnage._getVie()} points de vie')
        print(" ")

class Jeu:

    def __init__(self):
        self.__niveau = 1

    def _choisirNiveau(self):
        self.__niveau = int(input("Choisissez un niveau de difficulté (1, 2, 3) : "))
        print(" ")

    def _lancerPartie(self):
        if self.__niveau == 1:
            joueur = Personnage("Maxence", 50)
            monstre = Personnage("Patrick", 30)
            self.__niveau = "facile"
        elif self.__niveau == 2:
            joueur = Personnage("Maxence", 50)
            monstre = Personnage("Patrick", 50)
            self.__niveau = "moyen"
        elif self.__niveau == 3:
            joueur = Personnage("Maxence", 50)
            monstre = Personnage("Patrick", 100)
            self.__niveau = "difficile"
        else:
            print("Erreur de saisie")
            print(" ")
            self._choisirNiveau()

        while joueur._getVie() > 0 and monstre._getVie() > 0:
            joueur._attaquer(monstre)
            monstre._attaquer(joueur)

            print(f'Le joueur a {joueur._getVie()} points de vie')
            print(f'Le monstre a {monstre._getVie()} points de vie')

        if joueur._getVie() <= 0:
            print("Vous avez perdu")
            print(" ")
        else:
            print("Vous avez gagné")
            print(" ")

jeu = Jeu()
jeu._choisirNiveau()
jeu._lancerPartie()