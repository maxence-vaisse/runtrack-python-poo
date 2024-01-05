class Personne:
    def __init__(self, age=int(14)):
        self.age = age

    def afficherAge(self):
        print(self.age)

    def Bonjour(self):
        print("Hello")

    def modifierAge(self, age=int()):
        self.age = age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


personne1 = Personne()

eleve1 = Eleve()

eleve1.afficherAge()