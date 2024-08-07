from math import *
import random


"""Debutant"""

# Exercice 1:
class Biscuit:
    """classe définissant un biscuit et sa forme
    - nom
    - forme"""

    def __init__(self, nom, forme) -> None:
        """constructeur de la classe Biscuit"""
        self.nom = nom
        self.forme = forme

    def cuire(self) -> None:
        print("Ce {} a été cuit sous forme d'un(e) {}\nBonne dégustation".format(self.nom, self.forme))


# biscuit_1 = Biscuit("cookie pépite de chocolat", "étoile")
# biscuit_1.cuire()

# Exercice 2:
class Livre:
    """Classe définissant un livre
    - titre
    - auteur
    - prix"""
    
    def __init__(self, titre, auteur, prix) -> None:
        """constructeur de la classe livre"""
        self.titre = titre
        self.auteur = auteur
        self.prix = prix

    def afficher_informations(self) -> None:
        """methode permettant d'afficher les informations sur le livre """
        print("Le livre intitulé '{}', écrit par l'auteur '{}' se vend à {} euros.".format(self.titre, self.auteur, self.prix))

# livre1 = Livre("100 Exercices Python pour s'entrainer", "Laurentine K.Masson", 10.99)
# livre1.afficher_informations()

# Exercice 3:
class Note:
    """classe contenant le nom et la note d'un étudiant
    - nom
    - note"""

    def __init__(self, note, nomEtudiant) -> None:
        """constructeur de la classe note"""
        self.note = note
        self.nomEtudiant = nomEtudiant

    def a_reussi(self) -> None:
        if self.note > 75:
            print("{} a réussi".format(self.nomEtudiant))
        else:
            print("{} a échoué".format(self.nomEtudiant))

# Exercice 4:
class Cercle:
    """classe cercle permet d'identifier un cerle avec son rayon et les coordonnées de son centre
    - rayon r
    - abscisse x
    - ordonnée y"""
    
    def __init__(self, x, y, r) -> None:
        """ constructeur de classe cercle"""
        self.abscisse = x
        self.ordonnee = y
        self.rayon = r
    
    def surface(self) -> float:
        """cette methode permet de calculer la surface du cerle"""
        return pi*self.rayon**2
    
    def perimetre(self) -> float:
        """cette methode permet de calculer le périmètre du cercle"""
        return 2*pi*self.rayon
    
    def proprietes(self):
        """cette methode permet d'afficher les propriétés du cerle R, o(x, y)"""
        return "le cercle est de rayon {} cm et de centre O({}, {})".format(self.rayon, self.abscisse, self.ordonnee)

# cercle1 = Cercle(3, 4, 5)
# print(cercle1.surface())
# print(cercle1.perimetre())
# print(cercle1.proprietes())

# Exercice 5:
class Operation:
    """cette classe permet d'effectuer des opérations arithmétiques sur deux entiers
    - entier 1 : x
    - entier 2: y"""

    def __init__(self, x, y) -> None:
        """ Constructeur de classe """
        self.firstInt = x
        self.secondeInt = y
    
    def somme(self):
        """cette methode permet de calculer la somme des attribus"""
        return self.firstInt + self.secondeInt
    
    def multiplication(self):
        """cette methode permet de calculer la multiplication des attribus"""
        return self.firstInt * self.secondeInt
    
    def division(self):
        """cette methode permet de calculer la division et x/y"""
        if self.secondeInt != 0:
            return self.firstInt / self.secondeInt
        else:
            return "Division par 0 impossible!"

# operation1 = Operation(3, 2)
# print("l'operation somme donne :", operation1.somme())
# print("l'operation multiplication donne :", operation1.multiplication())
# print("l'operation multiplication donne :", operation1.division())
# operation1.secondeInt = 0
# print(operation1.division())

# Exercice 6:
class Personne:
    """cette classe permet de definir une personne par:
    -nom
    -age
    -sexe"""

    def __init__(self, nom: str, age: int, sexe: str) -> None:
        """construction d'une classe de type personne"""
        self.nom = nom
        self.age = age
        self.sexe = sexe
    
    def presenter(self) -> str:
        """cette methode permet de presenter la personne selon ces attribus"""
        return "Mon nom est {}, j'ai {} ans et je suis un(e) {}.".format(self.nom, self.age, self.sexe)
    
    def estAdulte(self) -> bool:
        """cette methode indique si une personne est adulte ou non!"""
        if self.age >= 18:
            return True
        else:
            return False
        
# personne1 = Personne("Aboubakr", 36, "homme")
# print(personne1.presenter())
# print(personne1.estAdulte())

# Exercice 7:
class Etudiant(Personne):
    """cette sous classe de la classe Personne permet de lister les etudiants inscrit
    et rajouter les nouveaux inscrits
    -nom
    -age
    -sexe
    -niveau"""

    def __init__(self, nom:str, age:int, sexe:str, niveau:str) -> None:
        """constructeur de la class etudiant"""
        Personne.__init__(self, nom, age, sexe)
        self.niveau = niveau

    def inscription(self, etudiants_inscrits: list) -> None:
        """cette methode permet de lister/ajouter des etudiants a la liste d inscription"""
        etudiants_inscrits.append((self.nom, self.age, self.sexe, self.niveau))

# etudiants_inscrits = []
# etudiant1 = Etudiant("Fabrice", 17, "homme", "3 eme")
# etudiant1.inscription(etudiants_inscrits)
# etudiant2 = Etudiant("Laila", 15, "femme", "1 ere")
# etudiant2.inscription(etudiants_inscrits)
# print("Les etudiants inscrits aux cours sont: \n", etudiants_inscrits)

# Exercice 8:
class De:
    """Cette classe permet créer un objet Dé et affiche le résultat de son lancé"""

    def __init__(self, resultat=0) -> None:
        """Constructeur de la class De avec une valeur par défaut = 0"""
        self.resultat = resultat

    def lancerDe(self) -> int:
        """Cette methode simule un lance de De en generant un nombre aléatoire entre 1 et 6"""
        self.resultat = random.randint(1, 6)
        return self.resultat
    
    def affichage_resultat(self) -> None:
        """Cette methode permet d'afficher le resultat obtenu"""
        print("Le nombre de points obtenus est : ", self.resultat)

# lancement1 = De()
# lancement1.lancerDe()
# lancement1.affichage_resultat()

"""Intermediare"""

# Exercice 9:
class Vehicule:
    """Cette class permet de definir un objet vehicule, elle comprend 2 attribus
    -marque
    -vitess initiale"""

    def __init__(self, marque, vitesse_initiale=0) -> None:
        """Constructeur de la classe vehicule"""
        self.marque = marque
        self.vitesse = vitesse_initiale

    
    def acceleration(self, v: float) -> None:
        """cette methode permet d augmenter la vitesse du vehicule en ajoutant V a la vitesse actuelle"""
        self.vitesse += v
    
    def deceleration(self, v: float) -> None:
        """cette methode permet de dimunuer la vitesse du vehicule en retirant V a la vitesse actuelle"""
        self.vitesse -= v
    
    def afficher_vitesse(self) -> None:
        """cette methode affiche la vitesse initiale et actuelle de la vitess"""
        print("Votre vitesse actuelle est : {} km/h".format(self.vitesse))

class Voiture(Vehicule):
    """sous classe de la classe vehicule, elle a un attribu supplementaire: klaxon"""

    def __init__(self, marque, vitesse_initiale=0) -> None:
        """constructeur de la classe voiture a partir de la classe vehicule"""
        Vehicule.__init__(self, marque, vitesse_initiale)
    
    def klaxonner(self) -> None:
        """cette methode simule un klaxon de voiture"""
        print("tuuut!")

# voiture1 = Voiture("Golf5", 10.5)
# print("La vitesse initiale de la voiture est : {} km/h".format(voiture1.vitesse))
# voiture1.acceleration(50)
# voiture1.deceleration(15)
# voiture1.afficher_vitesse()
# voiture1.klaxonner()

# Exercise 10:
class Employe:
    """cette classe definit un employer avec 3 attribus:
    -nom
    -fonction
    -salaire"""
    
    def __init__(self, nom: str, fontion: str, salaire: int, nombre_heures=0) -> None:
        """constructeur de la classe employe avec 4 attribus dont nombre d'heures travaillées = 0 par defaut"""
        self.nom = nom
        self.fonction = fontion
        self.salaire = salaire
        self.nombre_heures = nombre_heures

    def travailler(self, nb_heures: int) -> None:
        """cette methode additionne le nombre d heures de travail de l employe"""
        self.nombre_heures += nb_heures
        print("Le salarié {} a travaillé {} heures.".format(self.nom, self.nombre_heures))
    
    def info_salaire(self) -> None:
        """cette methode permet d afficher le salaire de l employer"""
        print("Le salairié {} touche un salaire de {} euros.".format(self.nom, self.salaire))
    
    def donner_augmentation(self, augmentation:int) -> None:
        """cette methode permet d ajouter une augmentation au salaire initial de l employer"""
        self.salaire += augmentation
        print("Le salairié {} a reçu un augmentation de {} euros, ce qui lui fait un salaire de {} euros.".format(self.nom, augmentation, self.salaire))
    
    def info_fonction(self) -> None:
        """cette methode permet d afficher la fonction de l employe"""
        print("Le salairié {} travaille en tant que : {}.".format(self.nom, self.fonction))
    
# employe1 = Employe("Julien", "Ingénieur", 4000)
# employe1.travailler(8)
# employe1.info_salaire()
# employe1.donner_augmentation(600)
# employe1.info_fonction()

# Exercice 11: creation d une classe contenant plusieurs methodes
class Calcul_Numerique:
    """cette methode pemert d effectuer les operations suivantes sur un nombre entier:
    -factoriel n!
    -liste diviseurs
    -test nombre premier
    -test nombre paire"""

    def __init__(self, n: int) -> None:
        """constructeur de la classe calcul_numerique il prend un seul attribu"""
        self.nombre = n

    def factoriel(self) -> int:
        """cette methode calcul le factorien d un nombre entier"""
        if self.nombre == 0 or self.nombre == 1:
            return 1
        else:
            i = 1
            fact = i
            while i <= self.nombre:
                fact *= i
                i += 1
            return fact
    
    def liste_diviseurs(self) -> list:
        """pour charque i ente 1 et n(compris) si le reste de division de n/i = 0 alors i est diviseur --> ajouter a liste"""
        diviseurs = []
        if self.nombre == 0:
            return diviseurs
        else:
            for i in range(1, self.nombre + 1):
                if self.nombre % i == 0:
                    diviseurs.append(i)
                else:
                    continue
            return diviseurs
    
    def estPremier(self) -> None:
        """Si la liste des diviseurs contient seulement 1 et n alors n est premier """
        if len(self.liste_diviseurs()) == 2:
            print("Le nombre {} est premier".format(self.nombre))
        else:
            print("Le nombre {} n'est pas premier".format(self.nombre))
    
    def estPaire(self) -> None:
        """si le reste de la division de n/2 = 0 alors n est paire"""
        if self.nombre % 2 == 0:
            print("Le nombre {} est paire".format(self.nombre))
        else:
            print("Le nombre {} n'est pas paire".format(self.nombre))
                
    
# calcul1 = Calcul_Numerique(5)
# factoriel5 = calcul1.factoriel()
# diviseur5 = calcul1.liste_diviseurs()
# print("La factoriel de 5 est : {}".format(factoriel5))
# print("La liste des diviseur de 5 est : {}".format(diviseur5))
# calcul1.estPaire()
# calcul1.estPremier()
# calcul2 = Calcul_Numerique(14)
# factoriel14 = calcul2.factoriel()
# diviseur14 = calcul2.liste_diviseurs()
# print("La factoriel de 14 est : {}".format(factoriel14))
# print("La liste des diviseur de 14 est : {}".format(diviseur14))
# calcul2.estPaire()
# calcul2.estPremier()

# Exercice 12: heritage multiples
class Video:
    """classe definissant un objet video elle comprend 3 attribus
    -titre
    -duree en minute
    -categorie"""

    def __init__(self, titre: str, duree: int, categorie: str) -> None:
        self.titre = titre
        self.duree = duree
        self.categorie = categorie
    
    def regarder_video(self) -> None:
        print("Lancement de la vidéo...\nLa vidéo que vous regardez est intitulée '{}' de la catégorie '{}'\
               d'une durée de {} minutes".format(self.titre, self.categorie, self.duree))
    
    def stop_video(self) -> None:
        print("Arrêt de la lecture vidéo.")

class Audio:
    """classe definissant un objet Audio elle comprend 2 attribus
    -titre
    -artiste"""

    def __init__(self, titre: str, artiste: str) -> None:
        self.titre = titre
        self.artiste = artiste

    def ecouter_audio(self) -> None:
        print("Lancement de l'audio'...\nL'audio que vous écoutez est '{}' produit par l'artiste '{}'".format(self.titre, self.artiste))
    
    def stop_audio(self) -> None:
        print("Arrêt de la lecture audio.")

class Media(Video, Audio):
    """classe Media herite de la classe video et de la classe audio tout leur attribus"""
    def __init__(self, titre: str, duree: int, categorie: str, artiste: str) -> None:
        Video.__init__(self, titre, duree, categorie)   
        Audio.__init__(self, titre, artiste)

# media1 = Media("The hobbit", 180, "Fantasy", "Howard Shore")
# media1.ecouter_audio()
# media1.regarder_video()
# media1.stop_audio()
# media1.stop_video()

# Exercice 13: surcharge operateur
class Vecteur4D:
    """cette classe definit un vecteur de 4 dimensions elle offre la possibilite d additionner, multiplier, soustraire deux vecteurs
     ou diviser un vecteur par un scalaire"""
    
    def __init__(self, args: list) -> None:
        """constructeur de classe permet d extraire les coordonnees du vecteur d une liste"""
        self.x = args[0]
        self.y = args[1]
        self.u = args[2]
        self.v = args[3]
    
    def __add__(self, vect) -> list:
        """cette permet d additionner la classe vecteur avec un autre"""
        return [self.x + vect.x , self.y + vect.y, self.u + vect.u , self.v + vect.v]
    
    def __mul__(self, vect) -> list:
        """cette permet de multiplier la classe vecteur avec un autre"""
        return [self.x * vect.x , self.y * vect.y, self.u * vect.u , self.v * vect.v]
    
    def __sub__(self, vect) -> list:
        """cette permet de soustraire la classe vecteur avec un autre"""
        return [self.x - vect.x , self.y - vect.y, self.u - vect.u , self.v - vect.v]
    def __truediv__(self, scal) -> list:
        """cette permet de diviser la classe vecteur par un scalaire"""
        return [self.x / scal , self.y / scal, self.u / scal , self.v / scal]
    
# vecteur1 = Vecteur4D([2, 4, 6, 8])
# vecteur2 = Vecteur4D([1, 2, 3, 4])
# print("v1 + v2 = ", vecteur1 + vecteur2)
# print("v1 - v2 = ", vecteur1 - vecteur2)
# print("v1 * v2 = ", vecteur1 * vecteur2)
# print("V2 / 2 = ", vecteur2/2)

# Exercice 14: surcharge d operateur d une classe
class Carte:
    """cette classe permet de definir une carte de jeu de carte par deux attributs
    -symbol
    -rang"""

    def __init__(self, rang, symbole) -> None:
        """constructeur de classe prend 2 parametres"""
        self.rang = rang
        self.symbole = symbole
    
    def __eq__(self, carte) -> bool:
        """cette methode permet de comparer deux carte de part leurs symboles et leurs valeurs"""
        if self.rang == carte.rang and self.symbole == carte.symbole:
            return True
        return False

    def __lt__(self, carte) -> bool:
        """cette methode permet de determiner l inegalite de deux cartes"""
        if self.rang == carte.rang:
            return self.symbole < carte.symbole
        return self.rang < carte.rang
    
    def __str__(self) -> str:
        return f"La carte est de rang {self.rang} et de symbole {self.symbole}"
    
enseignes = [chr(9824), chr(9825), chr(9826), chr(9827)]
rangs = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q":12, "K": 13, "A": 14}
trefle1, rang1 = enseignes[3], rangs["8"]
coeur2, rang2 = enseignes[1], rangs["3"]
pique3, rang3 = enseignes[0], rangs["8"]
carte1 = Carte(rang1, trefle1)
carte2 = Carte(rang2, coeur2)
carte3 = Carte(rang3, pique3)
print(carte1)
print(carte2)
print(carte3)
print(carte1 > carte2)
print(carte1 == carte3)

