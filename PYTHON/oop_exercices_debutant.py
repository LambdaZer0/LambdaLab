"""série d'exercices du livre '30 exercices en programmation orientée objet en python'"""
from math import *
import random

#Exercice 1: création d'une classe simple, appel de méthodes
class Biscuit:
    """création d'une classe de type Biscuit avec deux attribus
    -nom 
    -forme"""
    def __init__(self, nom:str, forme:str)-> None:
        """constructeur de classe cookie"""
        self.nom = nom
        self.forme = forme
    def cuir(self) -> None:
        """afficher le nom et la forme du cookie dans un text"""
        print(f"""Ce {self.nom} a été cuit sous fourme d'une {self.forme}\nBonne dégustation""")

# biscuit_1 = Biscuit("cookie pépite de chocolat", "étoile")
# biscuit_1.cuir()

#Exercice 2: création d'une classe simple, appel de méthodes
class Livre:
    """classe livre 
    - attribus: 
    titre
    auteur
    prix
    - méthodes:
    afficher_informations
    """
    def __init__(self, titre:str, auteur:str, prix:float) -> None:
        """constructeur de class"""
        self.titre = titre
        self.auteur = auteur
        self.prix = prix
    def afficher_informations(self) -> None:
        """afficher les informations de la classe livre"""
        print(f"""Le livre intitulé '{self.titre}', écrit par l'autreur '{self.auteur}' se vend à {self.prix} euros.""")

# livre_1 = Livre("100 Exercices Python pour s'entrainer", "Laurentine K.Masson", 10.99)
# livre_1.afficher_informations()

# Exercice 3: création d'une classe, accès et modification des attributs
class Note:
    """*attribus:
    -nom de l'étudiant
    -note de l'étudiant"""
    def __init__(self, note:int, nomEtudiant:str) -> None:
        """initialisation des attribus"""
        self.note = note
        self.nomEtudiant = nomEtudiant
    def a_reussi(self) -> None:
        """vérifier si la note de l'étudiant dépasse le seuil (75)"""
        if self.note > 75:
            print(f"""l'étudiant(e) {self.nomEtudiant} a réussi(e)""")
        else:
            print(f"""l'étudiant(e) {self.nomEtudiant} a échoué(e)""")
    
# note_1 = Note(80, "Julien")
# note_1.a_reussi()
# note_2 = Note(35, "Amélie")
# print(f"La note obtenue par {note_2.nomEtudiant} lors de la première correction est : {note_2.note}")
# note_2.note = 70
# print(f"Après une deuxième correction, la note d'{note_2.nomEtudiant} est égale à : {note_2.note}")
# note_2.a_reussi()

# Exercice 4: Création d'une classe contenant plusieurs méthodes
class Cercle:
    """attribus
    -abscisse du centre x
    -ordonnée du centre y
    -rayon r"""
    def __init__(self, x:float, y:float, r:float) -> None:
        """initialistion des attribus"""
        self.x = x 
        self.y = y
        self.r = r
    def afficher_propriete(self) -> str:
        return f"Le cerle est de rayon {self.r}cm, et de centre O({self.x}, {self.y})" 
    def surface(self) -> float:
        """calcul de la surface du cerle"""
        return round(pi * self.r**2, 2)
    def perimetre(self) -> float:
        """calcul du périmètre du cerle"""
        return round(2*pi*self.r, 2)
    
# cercle_1 = Cercle(3, 4, 5)
# print(cercle_1.afficher_propriete())
# print(f"Le périmètre du cercle_1 est : {cercle_1.perimetre()}")
# print(f"La surface du cercle_1 est : {cercle_1.surface()}")

# Exercice 5: Création d'une classe contenant plusieurs méthodes
class Operation:
    def __init__(self, x:int, y: int) -> None:
        self.x = x
        self.y = y
    
    def somme(self) -> int:
        return self.x + self.y
    
    def multiplication(self) -> int:
        return self.x * self.y
    
    def division(self) -> float:
        if self.y != 0:
            return round(self.x/self.y, 2)
        else:
            print("Division de x par y est impossible!")
            return None
# operation_1 = Operation(3, 2)
# print(f"L'opération somme donne: {operation_1.somme()}")
# print(f"L'opération multiplication donne: {operation_1.multiplication()}")
# print(f"L'opération division donne: {operation_1.division()}")
# operation_1.y = 0
# operation_1.division()

# Exercice 6: Création d'une classe contenant plusieurs méthodes
class Personne:
    """cette classe permet de définir une personne par un nom, age et sexe"""
    def __init__(self, nom:str, age:int, sexe:str) -> None:
        self.nom = nom
        self.age = age
        self.sexe = sexe
    
    def presenter(self) -> None:
        print(f"Mon nom est {self.nom}, j'ai {self.age} ans et je suis un(e) {self.sexe}")
        return None
    
    def estAdulte(self) -> bool:
        if self.age >= 18:
            return True
        else:
            return False

# personne_1 = Personne('Aboubakr', 36, "homme")
# personne_1.presenter()
# print(personne_1.estAdulte())

# Exercice 7: Héritage d'une classe parent
class Etudiant(Personne):
    """sous classe étudiant hérite de la classe Personne ses attributs + un attribut niveau"""
    def __init__(self, nom:str, age:int, sexe:str, niveau:str) -> None:
        """constructeur de la classe etudiant utilise le constructeur de la classe Personne"""
        super().__init__(nom, age, sexe)
        self.niveau = niveau
    def inscription(self, etudiants_inscrits:list) -> None:
        """methode permet d'ajout un étudiant à une liste à chaque nouvelle inscription"""
        etudiants_inscrits.append((self.nom, self.age, self.sexe, self.niveau))

etudiants_inscrits = []
etudiant1 = Etudiant("Fabrice", 17, "homme", "seconde")
etudiant1.inscription(etudiants_inscrits)
etudiant2 = Etudiant("Julie", 8, "femme", "primaire")
etudiant2.inscription(etudiants_inscrits)
# print(f"Les étudiants inscrits aux cours sont: {etudiants_inscrits}")

# Exercice 8: Création d'une classe dé avec plusieurs méthodes
class De:
    def __init__(self, resultat=0) -> None:
        """constructeur de la classe dé avec le resultat obtenu à chaque lancé (par défaut 0)"""
        self.resultat = resultat

    def lancer_un_de(self) -> int:
        """methode simule le lancé d'un dé"""
        self.resultat = random.randint(1, 6)
        return self.resultat

    def affichage_points(self) -> None:
        """methode affich"""
        print(f"Le nombre de points obtenu est : {self.resultat}")

# lancement_1 = De()
# lancement_1.lancer_un_de()
# lancement_1.affichage_points()

# Exercice 9: Héritage - Création d'une classe parente et d'une classe enfant
class Vehicule:
    """ Classe parent """
    def __init__(self, marque:str, vitesse_i=0) -> None:
        """ constructeur de la classe véhicule """
        self.marque = marque
        self.vitesse = vitesse_i 
    
    def acceleration(self, v) -> None:
        """ methode pour augmenter la vitesse du véhicule """
        self.vitesse += v
    
    def deceleration(self, v) -> None:
        """ methode pour diminuer la vitesse du véhicule """
        self.vitesse -= v
    
    def afficher_vitesse(self) -> None:
        """ methode pour afficher la vitesse du véhicule """
        print(f"Votre vitesse actuelle est : {self.vitesse}km/h")
    
class Voiture(Vehicule):
    """ sous classe de la classe vehicule """
    def __init__(self, marque, vitesse_i=0):
        super().__init__(marque, vitesse_i)
    
    def klaxonner(self) -> None:
        """ methode pour afficher un message de klaxon """
        print("tuuut !")

# voiture_1 = Voiture("Peugeot 208", 10.5)
# print(f"La vitesse initiale de la voiture est : {voiture_1.vitesse}")
# voiture_1.acceleration(50)
# voiture_1.deceleration(15)
# voiture_1.afficher_vitesse()
# voiture_1.klaxonner()

# Exercice 10 : Création d'une classe contenant plusieurs méthodes (intermédiaire)
class Employe:
    """ classe employe 4 attribus
    nom, fonction, salaire et nombre d'heures """

    def __init__(self, nom:str, fonction:str, salaire:float, heures=0) -> None:
        """ constructeur de classe """
        self.nom = nom
        self.fonction = fonction
        self.salaire = salaire
        self.heures = heures

    def travailler(self, nombre_heures):
        """ methode pour ajouter des heures et afficher le nombre total des heures travaillées """
        self.heures += nombre_heures
        print(f"Le salarié {self.nom} a travaillé {self.heures} heures.")
    
    def info_salaire(self):
        """ methode pour afficher le salaire de l'employé """
        print(f"Le salarié {self.nom} touche un salaire de {self.salaire} euros.")
    
    def donner_augmentation(self, augmentation):
        """ methode pour donner une augmentation et afficher le nouveau salaire """
        self.salaire += augmentation
        print(f"Le salarié {self.nom} a reçu une augmentation de {augmentation} euros, ce qui lui fait un salaire de {self.salaire} euros.")
    
    def info_fonction(self):
        """ methode pour afficher la fonction de l'employer """
        print(f"Le salarié {self.nom} travaille en tant que {self.fonction}.")

employe_1 = Employe("Julien", "Ingénieur", 4000)
# employe_1.travailler(8)
# employe_1.info_salaire()
# employe_1.donner_augmentation(600)
# employe_1.info_fonction()

# Exercice 11: Création d'une classe contenant plusieurs méthodes
class Calcul_Numerique:
    """ classe permettant d'effectuer plusieurs opération numériques:
     attribut: nombre entier """
    def __init__(self, nombre:int) -> None:
        """ constructeur de la classe calcul_numerique """
        self.nombre = nombre
    
    def calcul_factoriel(self) -> int:
        """ calcul du factoriel du nombre """
        return factorial(self.nombre)
    
    def liste_diviseurs(self) -> list:
        """ calcul de la liste des diviseurs du nombre """
        list_div = []
        for i in range(1, self.nombre+1):
            if self.nombre % i == 0:
                list_div.append(i)
        return list_div
    
    def estPremier(self) -> None:
        """ methode pour vérifier si le nombre est premier """
        if len(self.liste_diviseurs()) == 2:
            print(f"Le nombre {self.nombre} est premier.")
        else:
            print(f"Le nombre {self.nombre} n'est pas premier.")
    
    def estPaire(self) -> None:
        """ methode pour vérifier si le nombre est paire """
        if self.nombre % 2 == 0:
            print(f"Le nombre {self.nombre} est paire.")
        else:
            print(f"Le nombre {self.nombre} est impaire.")
    
premier_calcul = Calcul_Numerique(5)
factoriel_5 = premier_calcul.calcul_factoriel()
diviseurs_5 = premier_calcul.liste_diviseurs()
print(f"Le factoriel du nombre {premier_calcul.nombre} est : {factoriel_5}")
print(f"La liste des diviseurs du nombre {premier_calcul.nombre} est : {diviseurs_5}")
premier_calcul.estPaire()
premier_calcul.estPremier()
print("\n")
deuxieme_calcul = Calcul_Numerique(14)
factoriel_5 = deuxieme_calcul.calcul_factoriel()
diviseurs_5 = deuxieme_calcul.liste_diviseurs()
print(f"Le factoriel du nombre {deuxieme_calcul.nombre} est : {factoriel_5}")
print(f"La liste des diviseurs du nombre {deuxieme_calcul.nombre} est : {diviseurs_5}")
deuxieme_calcul.estPaire()
deuxieme_calcul.estPremier()
