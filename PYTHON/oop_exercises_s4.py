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
    