
""" Nouveau programme apprentissage OOP"""

# serie 1:
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
        """cette methode permer d afficher le type (type) et l adresse physique de la classe (id)"""
        ch = str(type(self))
        ch += " à l'adresse "
        ch += str(id(self))
        return ch
    
    def __repr__(self) -> str:
        """methode speciale pour un affichage personnalise de la classe"""
        ch = f"{self.nom}({self.pos_x}, {self.pos_y})"
        return ch
    
    def getPosX(self) -> float:
        """getter de la coordonnee x"""
        return self.pos_x
    
    def setPosX(self, val) -> None:
        """setter de la coordonnee x"""
        if type(val) is not float:
            raise TypeError("la coordonnee x doit etre de type float")
        self.pos_x = val

    def getPosY(self) -> float:
        """getter de la coordonnee y"""
        return self.pos_y
    
    def setPosY(self, val) -> None:
        """setter de la coordonnee y"""
        if type(val) is not float:
            raise TypeError("la coordonnee y doit etre de type float")
        self.pos_y = val

    def getIntitule(self) -> str:
        """getter du nom du point"""
        return self.nom
    
    def setIntitule(self, val) -> None:
        """setter du nom du point"""
        if type(val) is not str:
            raise TypeError("la coordonnee y doit etre de type string")
        self.nom = val

pt_a = Point2d("A", 2, 3)
print("format personnalisé pour pt_a", pt_a)
print(pt_a.typeEtAdressMemoire())