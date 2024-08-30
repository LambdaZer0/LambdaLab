import math

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