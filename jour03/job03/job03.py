class Tache:
    def __init__(self, titre, description, statut="a faire" or "terminer"):
        self.__titre = titre
        self.__description = description
        self.__statut = statut

    def _getTitre(self):
        return self.__titre
    
    def _getDescription(self):
        return self.__description
    
    def _getStatut(self):
        return self.__statut
    
    def _setTitre(self, titre):
        self.__titre = titre

    def _setDescription(self, description):
        self.__description = description

    def _setStatut(self, statut):
        self.__statut = statut

class ListeDeTaches:
    def __init__(self, nom):
        self.__nom = nom
        self.__liste_taches = []

    __liste_taches = []

    def _getNom(self):
        return self.__nom
    
    def _getListeTaches(self):
        return self.__liste_taches
    
    def _setNom(self, nom):
        self.__nom = nom

    def _setListeTaches(self, liste_taches):
        self.__liste_taches = liste_taches

    def _ajouterTache(self, tache):
        self.__liste_taches.append(tache)

    def _supprimerTache(self, tache):
        self.__liste_taches.remove(tache)
        print(f'La tâche "{tache._getTitre()}" a été supprimée.')

    def _marquerCommeFinie(self, tache):
        tache._setStatut("Finie")
        print(f'La tâche "{tache._getTitre()}" a été marquée comme terminée.')

    def _afficherListe(self):
        print(f'Liste de tâches "{self.__nom}":')
        for tache in self.__liste_taches:
            print(f'- {tache._getTitre()} ({tache._getStatut()})')

    def _filtrerListe(self, statut):
        print(f'Liste de tâches "{self.__nom}":')
        for tache in self.__liste_taches:
            if tache._getStatut() == statut:
                print(f'- {tache._getTitre()} ({tache._getStatut()})')
            else:
                pass

tache1 = Tache("Faire les courses", "Acheter du pain, du lait et des oeufs")
tache2 = Tache("Faire la vaisselle", "Ne pas oublier les couverts")
tache3 = Tache("Faire la lessive", "Ne pas oublier la lessive")

_ListeDeTaches = ListeDeTaches("A ne surtout pas oublier")
_ListeDeTaches._ajouterTache(tache1)
_ListeDeTaches._ajouterTache(tache2)
_ListeDeTaches._ajouterTache(tache3)
_ListeDeTaches._afficherListe()
_ListeDeTaches._marquerCommeFinie(tache1)

print("\n")

_ListeDeTaches._afficherListe()
_ListeDeTaches._supprimerTache(tache2)

print("\n")

_ListeDeTaches._afficherListe()

print("\n")

_ListeDeTaches._filtrerListe("a faire")
