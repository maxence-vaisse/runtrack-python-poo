class Joueur:
    def __init__ (self, nom, numero, position, nb_buts_marques, passe_decisive, cartons_jaune, cartons_rouge):
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__nb_buts_marques = nb_buts_marques = 0
        self.__passe_decisive = passe_decisive = 0
        self.__cartons_jaune = cartons_jaune = 0
        self.__cartons_rouge = cartons_rouge = 0

    def _getNom(self):
        return self.__nom
    
    def _getNumero(self):
        return self.__numero
    
    def _getPosition(self):
        return self.__position
    
    def _getNbButsMarques(self):
        return self.__nb_buts_marques
    
    def _getPasseDecisive(self):
        return self.__passe_decisive
    
    def _getCartonsJaune(self):
        return self.__cartons_jaune
    
    def _getCartonsRouge(self):
        return self.__cartons_rouge
    
    def _setNom(self, nom):
        self.__nom = nom

    def _setNumero(self, numero):
        self.__numero = numero

    def _setPosition(self, position):
        self.__position = position

    def _setNbButsMarques(self, nb_buts_marques):
        self.__nb_buts_marques = nb_buts_marques
        
    def _marquerUnBut(self):
        self.__nb_buts_marques += 1 

    def _setPasseDecisive(self, passe_decisive):
        self.__passe_decisive = passe_decisive
        
    def _effectuerUnePasseDecisive(self):
        self.__passe_decisive += 1

    def _setCartonsJaune(self, cartons_jaune):
        self.__cartons_jaune = cartons_jaune
        
    def _recevoirUnCartonJaune(self):
        self.__cartons_jaune += 1

    def _setCartonsRouge(self, cartons_rouge):
        self.__cartons_rouge = cartons_rouge

    def _recevoirUnCartonRouge(self):
        self.__cartons_rouge += 1

    def _afficherStatistiques(self):
        print(f'Nom: {self.__nom}')
        print(f'Numéro: {self.__numero}')
        print(f'Position: {self.__position}')
        print(f'Nombre de buts marqués: {self.__nb_buts_marques}')
        print(f'Nombre de passes décisives: {self.__passe_decisive}')
        print(f'Nombre de cartons jaunes: {self.__cartons_jaune}')
        print(f'Nombre de cartons rouges: {self.__cartons_rouge}')
        print(" ")

class Equipe:
    def __init__(self, nom):
        self.__nom = nom
        self.__liste_joueurs = []

    def _getNom(self):
        return self.__nom
    
    def _getListeJoueurs(self):
        return self.__liste_joueurs
    
    def _setNom(self, nom):
        self.__nom = nom

    def _setListeJoueurs(self, liste_joueurs):
        self.__liste_joueurs = liste_joueurs

    def _ajouterJoueur(self, joueur):
        self.__liste_joueurs.append(joueur)

    def _AfficherStatiquesJoueurs(self):
        print("Equipe:" , self.__nom)
        for joueur in self.__liste_joueurs:
            joueur._afficherStatistiques()

    def _mettreAJourStatistiquesJoueur(self, joueur, nb_buts_marques, passe_decisive, cartons_jaune, cartons_rouge):
                joueur._setNbButsMarques(nb_buts_marques)
                joueur._setPasseDecisive(passe_decisive)
                joueur._setCartonsJaune(cartons_jaune)
                joueur._setCartonsRouge(cartons_rouge)

joueur1 = Joueur("Youssef", 1, "Gardien", 0, 0, 0, 0)
joueur2 = Joueur("Manon", 2, "Défenseur", 0, 0, 0, 0)
joueur3 = Joueur("Jean", 3, "Millieu", 0, 0, 0, 0)
joueur4 = Joueur("Ibrahim", 4, "Attanquant", 0, 0, 0, 0)
equipe1 = Equipe("Marseille")
equipe1._ajouterJoueur(joueur1)
equipe1._ajouterJoueur(joueur2)
equipe1._ajouterJoueur(joueur3)
equipe1._ajouterJoueur(joueur4)

joueur5 = Joueur("Rheda", 5, "Gardien", 0, 0, 0, 0)
joueur6 = Joueur("Maxence", 6, "Défenseur", 0, 0, 0, 0)
joueur7 = Joueur("Rija", 7, "Milleu", 0, 0, 0, 0)
joueur8 = Joueur("Jordan", 8, "Attaquant", 0, 0, 0, 0)
equipe2 = Equipe("Paris")
equipe2._ajouterJoueur(joueur5)
equipe2._ajouterJoueur(joueur6)
equipe2._ajouterJoueur(joueur7)
equipe2._ajouterJoueur(joueur8)

equipe1._AfficherStatiquesJoueurs()
equipe2._AfficherStatiquesJoueurs()

joueur1._marquerUnBut()

joueur2._effectuerUnePasseDecisive()

joueur3._recevoirUnCartonJaune()

joueur4._recevoirUnCartonRouge()

equipe1._AfficherStatiquesJoueurs()
equipe2._AfficherStatiquesJoueurs()