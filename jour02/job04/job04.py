class Student: # Création de la classe Student
    def __init__(self, nom, prenom, numetudiant, credit=0): # Création de la méthode __init__ avec les attributs nom, prenom, numetudiant et credit
        self.__nom = nom # Création de l'attribut nom
        self.__prenom = prenom # Création de l'attribut prenom
        self.__numetudiant = numetudiant # Création de l'attribut numetudiant
        self.__credit = credit # Création de l'attribut credit
        self.__level = self.__student_eval() # Création de l'attribut level

    def __add_credits__(self, credit): # Création de la méthode add_credits avec l'attribut credit
        if isinstance(credit, int) and credit > 0: # Vérifie que l'attribut credit est un entier positif
            self.__credit += credit # Ajoute l'attribut credit à l'attribut credit
            self.__level = self.__student_eval() # Met à jour l'attribut level
        else: # Si l'attribut credit n'est pas un entier positif
            print("Le nombre de crédits doit être un entier positif.") # Affiche un message d'erreur
            exit(1) # Arrête le programme

    def __get_credits__(self): # Création de la méthode get_credits
        return self.__credit # Retourne l'attribut credit

    def __student_eval(self): # Création de la méthode __student_eval
        if self.__credit >= 90: # Si l'attribut credit est supérieur ou égal à 90
            return "Excellent" # Retourne "Excellent"
        elif self.__credit >= 80: # Si l'attribut credit est supérieur ou égal à 80
            return "Très bien" # Retourne "Très bien"
        elif self.__credit >= 70: # Si l'attribut credit est supérieur ou égal à 70
            return "Bien" # Retourne "Bien"
        elif self.__credit >= 60: # Si l'attribut credit est supérieur ou égal à 60
            return "Passable" # Retourne "Passable"
        else: # Si l'attribut credit est inférieur à 60
            return "Insuffisant" # Retourne "Insuffisant"

    def __get_level__(self): # Création de la méthode get_level
        return self.__level # Retourne l'attribut level

    def student_info(self): # Création de la méthode student_info
        print(f"Nom: {self.__nom}") # Affiche l'attribut nom
        print(f"Prénom: {self.__prenom}") # Affiche l'attribut prenom
        print(f"Identifiant: {self.__numetudiant}") # Affiche l'attribut numetudiant
        print(f"Niveau: {self.__level}") # Affiche l'attribut level


Student1 = Student("Doe", "John", 145, 30) # Création de l'objet Student1 avec les attributs nom, prenom, numetudiant et credit
Student1.__add_credits__(10) # Ajoute 10 à l'attribut credit
Student1.__add_credits__(15) # Ajoute 15 à l'attribut credit
Student1.__add_credits__(5) # Ajoute 5 à l'attribut credit
print(f"Le nombre de crédits de John Doe est de {Student1.__get_credits__()} points") # Affiche l'attribut credit
print(f"La note de John Doe est {Student1.__get_level__()}") # Affiche l'attribut level
Student1.student_info() # Affiche les attributs nom, prenom, numetudiant et level