class Vehicule:
    def __init__(self, marque, modele, annee, prix):

        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__prix = prix


    def demarrer(self):
        print("Attention je roule .")    

    def informationVehicule(self):

        print("Marque :", self.__marque)
        print("Modèle :", self.__modele)
        print("Année :", self.__annee)
        print("Prix :", self.__prix, "€")

class Voiture(Vehicule):

    def __init__(self, marque, modele, annee, prix, portes=4):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.__portes = portes

    def informationVoiture(self):
        self.informationVehicule()
        print("Nombre de portes :", self.__portes)
    def demarrer(self):
        print("Je suis une voiture et je démarre")

class Moto(Vehicule):
    
        def __init__(self, marque, modele, annee, prix, roue=2):
            Vehicule.__init__(self, marque, modele, annee, prix)
            self.__roue = roue
    
        def informationMoto(self):
            self.informationVehicule()
            print("Nombre de roue :", self.__roue)
        def demarrer(self):
            print("Je suis une moto et je démarre")    

voiture = Voiture("Cadillac", "Escalade", 2009, 33000)
voiture.informationVoiture()
voiture.demarrer()
moto = Moto("Suzuki", "600 DR", 1987, 4500)
moto.informationMoto()
moto.demarrer()