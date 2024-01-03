class Livre:
    def __init__(self, titre, auteur, nbpages, disponible=True):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbpages = nbpages
        self.__disponible = disponible

    def __getTitre__(self):
        return self.__titre

    def __getAuteur__(self):
        return self.__auteur

    def __getNbpages__(self):
        return self.__nbpages

    def __verification__(self):
        return self.__disponible

    def __emprunter__(self):
        if self.__verification__():
            self.__disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    def __rendre__(self):
        if not self.__verification__():
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre est déjà disponible.")

# Exemple d'utilisation
print("Livre 1 :")
Livre1 = Livre("Harry Potter", "J.K. Rowling", 300)
print(Livre1.__getTitre__())
print(Livre1.__getAuteur__())
print(Livre1.__getNbpages__())
Livre1.__emprunter__()
Livre1.__verification__()
Livre1.__verification__()