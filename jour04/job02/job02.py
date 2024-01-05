class Personne:
    def __init__(self, age=int(14)):
        self.age = age

    def afficherAge(self):
        print("J'ai", self.age, "ans")

    def bonjour(self):
        print("Bonjour")

    def modifierAge(self, age=int):
        self.age = age    

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print("J'ai", self.age, "ans")

class Professeur(Personne):        
    def __init__(self, age, matiereEnseignee):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


# Instanciation d'une classe Personne et d'une classe Eleve
personne = Personne()
eleve = Eleve()

eleve.bonjour()
eleve.allerEnCours()
eleve.modifierAge(15)
eleve.afficherAge()

professeur = Professeur(40, "python")
professeur.bonjour()
professeur.enseigner()