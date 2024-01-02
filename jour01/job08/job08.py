class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon
        return self.rayon
    
    def afficherInfos(self):
        return "Cercle de rayon " + str(self.rayon) + " Cercle de diametre " + str(self.rayon * 2) + " Cercle de circonference " + str(2 * 3.14 * self.rayon) + " Cercle de aire " + str(3.14 * self.rayon * self.rayon)
    
    def circonference(self):
        return 2 * 3.14 * self.rayon
    
    def aire(self):
        return 3.14 * self.rayon * self.rayon
    
    def diametre(self):
        return 2 * self.rayon
    
cercle1 = Cercle(4)
cercle2 = Cercle(7)
print(cercle1.changerRayon(25))
print(cercle1.afficherInfos())
print(cercle1.circonference())
print(cercle1.aire())
print(cercle1.diametre())

print(cercle2.changerRayon(13))
print(cercle2.afficherInfos())
print(cercle2.circonference())
print(cercle2.aire())
print(cercle2.diametre())