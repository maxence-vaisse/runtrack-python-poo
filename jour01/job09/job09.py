class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        return f"Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}%"

    def modifier_le_Nom(self, nouveauNom):
        self.nom = nouveauNom

    def modifier_le_Prix(self, nouveauPrix):
        self.prixHT = nouveauPrix

    def obtenir_le_Nom(self):
        return self.nom

    def obtenir_le_Prix(self):
        return self.prixHT

    def obtenir_la_TVA(self):
        return self.TVA

# Création de plusieurs produits
Banane = Produit("Banane", 2.45, 20)
Fraise = Produit("Fraise", 1.25, 20)
Pasteque = Produit("Pasteque", 4.7, 20)

# Affichage initial
print("Affichage initial des produits:")
print(Banane.afficher())
print(Fraise.afficher())
print(Pasteque.afficher())

# Calcul de la TVA pour chaque produit
print("\nCalcul de la TVA pour chaque produit:")
print(f"TVA Banane: {Banane.calculerPrixTTC() - Banane.prixHT}")
print(f"TVA Fraise: {Fraise.calculerPrixTTC() - Fraise.prixHT}")
print(f"TVA Pasteque: {Pasteque.calculerPrixTTC() - Pasteque.prixHT}")

# Modification du nom et du prix de chaque produit
Banane.modifier_le_Nom("Banane")
Banane.modifier_le_Prix(3.1)

Fraise.modifier_le_Nom("Fraise")
Fraise.modifier_le_Prix(1.73)

Pasteque.modifier_le_Nom("Pasteque")
Pasteque.modifier_le_Prix(5.3)

# Affichage des produits après modification
print("\nAffichage des produits après modification:")
print(Banane.afficher())
print(Fraise.afficher())
print(Pasteque.afficher())

# Nouveau calcul de la TVA pour chaque produit
print("\nNouveau calcul de la TVA pour chaque produit:")
print(f"TVA Banane: {Banane.calculerPrixTTC() - Banane.prixHT}")
print(f"TVA Fraise: {Fraise.calculerPrixTTC() - Fraise.prixHT}")
print(f"TVA Pasteque: {Pasteque.calculerPrixTTC() - Pasteque.prixHT}")
