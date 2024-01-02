class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print(f'Je suis {self.prenom} {self.nom}')

gens = Personne('Dupont', 'Jean').SePresenter()
gens1 = Personne('Vaisse', 'Maxence').SePresenter()
gens2 = Personne('Girard', 'Pierre').SePresenter()
