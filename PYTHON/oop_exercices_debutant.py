"""série d'exercices du livre '30 exercices en programmation orientée objet en python'"""
from math import *

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
print(f"Les étudiants inscrits aux cours sont: {etudiants_inscrits}")