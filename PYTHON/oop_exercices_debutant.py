"""série d'exercices du livre '30 exercices en programmation orientée objet en python'"""

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
    
note_1 = Note(80, "Julien")
note_1.a_reussi()
note_2 = Note(35, "Amélie")
print(f"La note obtenue par {note_2.nomEtudiant} lors de la première correction est : {note_2.note}")
note_2.note = 70
print(f"Après une deuxième correction, la note d'{note_2.nomEtudiant} est égale à : {note_2.note}")
note_2.a_reussi()