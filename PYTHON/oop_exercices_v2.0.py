
""" Nouveau programme apprentissage OOP"""

# Exercice 1:
class Point2d:
    """cette class defini un point de dimension 2 dans un espace euclidien elle comprend 3 attribus
    -nom: intitule du point
    -x: absisse
    -y: ordonnee"""
    def __init__(self, nom: str, x: float, y:float) -> None:
        """constructeur de la classe Point2d"""
        self.nom = nom
        self.pos_x = x
        self.pos_y = y

# pt_a = Point2d("A", 2, 3)

# Exercice 2:
class Point2d:
    """cette class defini un point de dimension 2 dans un espace euclidien elle comprend 3 attribus
    -nom: intitule du point
    -x: absisse
    -y: ordonnee"""
    def __init__(self, nom: str, x: float, y:float) -> None:
        """constructeur de la classe Point2d"""
        self.nom = nom
        self.pos_x = x
        self.pos_y = y

    def typeEtAdressMemoire(self) -> str:
        ch = str(type(self))
        ch += " à l'adresse "
        ch += str(id(self))
        return ch
# pt_a = Point2d("A", 2, 3)
# print(pt_a.typeEtAdressMemoire())

# Exercice 3:
class Point2d:
    """cette class defini un point de dimension 2 dans un espace euclidien elle comprend 3 attribus
    -nom: intitule du point
    -x: absisse
    -y: ordonnee"""
    def __init__(self, nom: str, x: float, y:float) -> None:
        """constructeur de la classe Point2d"""
        self.nom = nom
        self.pos_x = x
        self.pos_y = y

    def typeEtAdressMemoire(self) -> str:
        ch = str(type(self))
        ch += " à l'adresse "
        ch += str(id(self))
        return ch
    
    def __repr__(self) -> str:
        ch = f"{self.nom}({self.pos_x}, {self.pos_y})"
        return ch

pt_a = Point2d("A", 2, 3)
print("format personnalisé pour pt_a", pt_a)
print(pt_a.typeEtAdressMemoire())