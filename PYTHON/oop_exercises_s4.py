import math
import random

class Cercle:
    """cette classe definit un cercle avec :
    un rayon r"""
    atc_pi = math.pi
    def __init__(self, rayon:float) -> None:
        """constructeur de classe cercle prend en attribu le rayon du cercle"""
        self._rayon = rayon
    
    def __repr__(self) -> str:
        """affichage personnalise de la classe"""
        ch = f"cercle de rayon = {self._rayon}"
        return ch
    
    def surface(self) -> float:
        """cette methode la surface du cercle"""
        sf = self.atc_pi * self._rayon**2
        return sf
    
    def circonference(self) -> float:
        """cette methode la circonference du cercle"""
        cf = 2 * self.atc_pi * self._rayon
        return cf
    
class CylindreDroit(Cercle):
    """Classe cylindre heritant de la classe Cercle"""

    def __init__(self, rayon_base:float, hauteur:float) -> None:
        """constructeur de la classe cylindre comprend le rayon de la basse pour la classe mere Cerle et la hauteur"""
        Cercle.__init__(self, rayon_base)
        self._hauteur = hauteur

    def __repr__(self) -> str:
        """affichage personnalise pour la fonction print"""
        nl = "\n"
        ch = f"la base est un cerle de rayon = {self._rayon}{nl}la hauteur est = {self._hauteur}"
        return ch
    
    def aireFaceLaterale(self) -> float:
        """aire de la face laterale du cylindre"""
        af = self.circonference() * self._hauteur
        return af
    
    def aireTotale(self) -> float:
        """surface totale du cylindre"""
        at = 2 * self.surface() + self.aireFaceLaterale()
        return at
    
    def volume(self) -> float:
        """volume du cylindre"""
        vol = self.surface() * self._hauteur
        return vol
    
class ConeRevolution(CylindreDroit):
    """Classe Cone heritant de la classe CylindreDroit"""

    def __init__(self, rayon_base: float, hauteur: float) -> None:
        CylindreDroit.__init__(self, rayon_base, hauteur)

    def __repr__(self) -> str:
        """affichage personnalise pour la fonction print"""
        nl = "\n"
        ch = f"la base est un cerle de rayon = {self._rayon}{nl}la hauteur est = {self._hauteur}"
        return ch
    
    def volume(self) -> float:
        return CylindreDroit.volume()/3

class JeuDeCartes:
    """classe qui gère un jeu de  52 cartes"""

    atc_couleur = ("pique", "coeur", "carreau", "trèfle")
    atc_valeur = (2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi", "as")
    
    def __init__(self) -> None:
        """constructeur des 52 cartes
        exemple : (4, 0) ->  4 de piques
        (14, 2) -> As de carreau"""
        self._listing = []
        for coul in range(4):
            for val in range(13):
                carte = (val+2, coul)
                self._listing.append(carte)

    def getListing(self) -> list:
        """listing des cartes"""
        return self._listing
    
    def nomCarte(self, ca:tuple) -> str:
        ch = f"carte {self.atc_valeur[ca[0] - 2]} de {self.atc_couleur[ca[1]]}"
        return ch
    
    def battreCartes(self) -> None:
        """Methode permettant de melanger le jeu des cartes"""
        # nombre de cartes restantes
        nb_res = len(self._listing)
        for x in range(nb_res):
            # tirage au hasard de 2 emplacements dans la liste
            h1, h2 = random.randrange(nb_res), random.randrange(nb_res)
            self._listing[h1], self._listing[h2] = self._listing[h2], self._listing[h1]

    def tirerCarte(self) -> tuple:
        """tirer une carte du jeu"""
        nb_res = len(self._listing)
        if nb_res > 0:
            # choisir la premiere carte du jeu
            ca = self._listing[0]
            # on retire la carte du jeu
            del(self._listing[0])
            return ca
        else:
            return None