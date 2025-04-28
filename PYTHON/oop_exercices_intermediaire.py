"""série d'exercices du livre '30 exercices en programmation orientée objet en python'"""
from math import *
import random

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
