
""" Nouveau programme apprentissage OOP"""
import math

# serie 1:
class Point2d:
    """cette class defini un point de dimension 2 dans un espace euclidien elle comprend 3 attribus
    -nom: intitule du point
    -x: absisse
    -y: ordonnee"""

    def __init__(self, ch: str, x: float, y:float) -> None:
        """constructeur de la classe Point2d"""
        self._intitule = ch
        self._pos_x = x
        self._pos_y = y

    def typeEtAdressMemoire(self) -> str:
        """cette methode permer d afficher le type (type) et l adresse physique de la classe (id)"""
        ch = str(type(self))
        ch += " à l'adresse "
        ch += str(id(self))
        return ch
    
    def __repr__(self) -> str:
        """methode speciale pour un affichage personnalise de la classe avec la fonction print"""
        ch = f"{self._intitule}({self._pos_x}, {self._pos_y})"
        return ch
    
    def getPosX(self) -> float:
        """getter de la coordonnee x"""
        return self._pos_x
    
    def setPosX(self, val) -> None:
        """setter de la coordonnee x"""
        if type(val) is not float:
            raise TypeError("la coordonnee x doit etre de type float")
        self._pos_x = val

    def getPosY(self) -> float:
        """getter de la coordonnee y"""
        return self._pos_y
    
    def setPosY(self, val) -> None:
        """setter de la coordonnee y"""
        if type(val) is not float:
            raise TypeError("la coordonnee y doit etre de type float")
        self._pos_y = val

    def getIntitule(self) -> str:
        """getter du nom du point"""
        return self._intitule
     
    def setIntitule(self, val) -> None:
        """setter du nom du point"""
        if type(val) is not str:
            raise TypeError("l'intitulé du point doit etre de type string")
        self._intitule = val
    
    coordonnee_x = property(getPosX, setPosX) # modifier les valeurs de x a travers l accesseur coordonnee_x
    coordonnee_y = property(getPosY, setPosY) # modifier les valeurs de y a travers l accesseur coordonnee_y
    intitule = property(getIntitule, setIntitule) # modifier l intitule du point a travers l accesseur intitule

    @staticmethod
    def pointOrigine():
        """methode statique qui permet d initialiser le point a l origine"""
        return Point2d("Ori", 0.0, 0.0)
    
    @staticmethod
    def distancePoint(pt1, pt2) -> float:
        """cette methode permet de calculer la distance entre de points
        d = sqrt((Ax -Bx)^2 + (Ay - By)^2)"""
        if isinstance(pt1, Point2d) == False:
            raise TypeError("pt1 doit être de type Point2d")
        if isinstance(pt2, Point2d) == False:
            raise TypeError("pt2 doit être de type Point2d")
        dx = abs(pt1.coordonnee_x - pt2.coordonnee_x)
        dy = abs(pt1.coordonnee_y - pt2.coordonnee_y)
        return math.sqrt(dx**2 + dy**2)
    
    def deplacement(self, tx: float, ty:float) -> None:
        """cette methode permet de deplacer le point suivant les axes du plan en ajoutant des valeurs positives ou negatives
        aux deux coordonnees du point:
        tx pour un deplacement horizontal
        ty pour un deplacement vertical"""
        self.coordonnee_x += tx
        self.coordonnee_y += ty 

# serie 2:
class Domino:
    """classe qui formalise un dominoau travers de ses deux faces A et B"""
    def __init__(self, val_a: int, val_b:int) -> None:
        """constructeur avec paramètre"""
        if val_a < 0 or val_a > 6:
            raise ValueError("la face A doit être de valeur comprise entre 0 et 6")
        if isinstance(val_a, int) == False:
            raise TypeError("la valeur de la face A doit être de type entier")
        if val_b < 0 or val_b > 6:
            raise ValueError("la face B doit être de valeur comprise entre 0 et 6")
        if isinstance(val_b, int) == False:
            raise TypeError("la valeur de la face B doit être de type entier")
        self._face_a = val_a
        self._face_b = val_b
    
    def __repr__(self) -> str:
        """redefinition pour un affichage personnalise avec print"""
        ch = f"(A: {self._face_a}) | (B: {self._face_b})"
        return ch
    
    def sommeFaces(self) -> int:
        """calcule de la somme des deux faces A et B du domino"""
        return self._face_a + self._face_b

# serie 3:
class CompteBancaire:
    """cette classe definit un compte bancaire d une personne avec les attribus:
    -numero de compte
    -nom du titulaire du compte
    -le solde initial
    -solde en cours
    -listing comptable liste de tuples"""

    def __init__(self, ch_num: str, ch_nom: str, solde_ini: float) -> None:
        """contructeur de classe compte bancaire"""
        self._numero = ch_num
        self._titulaire = ch_nom
        self._solde_ini = solde_ini
        self._solde_en_cours = self._solde_ini
        self._listing = []
        self._listing.append(("solde initial", self._solde_ini, self._solde_en_cours))
    
    def __repr__(self) -> str:
        """methode pour affichage personnalise avec print"""
        nl = '\n'
        ch = f"numéro de compte : {self._numero}{nl}titulaire : {self._titulaire}{nl}solde en cours : {self._solde_en_cours}"
        return ch
    
    def verser(self, montant:float) -> None:
        """"cette methode permet d ajouter un montant au solde en cours"""
        self._solde_en_cours += montant
        self._listing.append(("versement", montant, self._solde_en_cours))

    def retirer(self, montant:float) -> None:
        """cette methode permet de retirer un montant du solde en cours"""
        self._solde_en_cours -= montant
        self._listing.append(("retrait", montant, self._solde_en_cours))
    
    def getListingEcriture(self) -> list:
        """cette methode renvoie la liste des ecritures comptables"""
        return self._listing