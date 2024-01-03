class Livre:
    def __init__(self, titre, auteur, nbpages, disponible=True):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbpages = nbpages
        self.__disponible = disponible

    def _getTitre(self):
        return self.__titre

    def _getAuteur(self):
        return self.__auteur

    def _getNbpages(self):
        return self.__nbpages

    def _verification(self):
        return self.__disponible

    def _emprunter(self):
        if self._verification():
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    def __rendre__(self):
        if not self._verification():
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre est déjà disponible.")

# Exemple d'utilisation
print("Livre 1 :")
Livre1 = Livre("Harry Potter", "J.K. Rowling", 300)
print(Livre1._getTitre())
print(Livre1._getAuteur())
print(Livre1._getNbpages())
Livre1._emprunter()
Livre1._verification()
Livre1._verification()