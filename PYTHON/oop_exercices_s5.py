class Txt4f:
    """classe statique pour formater une valeur float
    pour un rendu texte"""

    @staticmethod
    def ftPerso(val:float) -> str:
        if isinstance(val, float) == False:
            raise TypeError("il faut passer un float")
        if val == 0.0:
            return "00000.0000"
        if val > 0:
            ch = str(format(val, ".4f"))
            chg = ch.split(".")[0]
            chg = chg.zfill(4)
            chd = ch.split(".")[1]
            return f"+{chg}.{chd}"
        if val < 0:
            ch = str(format(val, ".4f"))
            chg = ch.split(".")[0]
            chg = chg.zfill(5)
            chd = ch.split(".")[1]
            return f"{chg}.{chd}"
        return None
    
class Matrice3x3:
    """classe utilisée pour gérer une matrice de dimension 3 par 3"""
    
    def __init__(self, a11:float, a12:float, a13:float,
                 a21:float, a22:float, a23:float,
                 a31:float, a32:float, a33:float) -> None:
        """constructeur de la matrice 3x3"""
        self._matrice = []
        self._matrice.append([a11, a12, a13])
        self._matrice.append([a21, a22, a23])
        self._matrice.append([a31, a32, a33])

    def __repr__(self) -> str:
        """affichage personnalise de la classe"""
        nl = "\n"
        ch = f"[{self._matrice[0]}{nl}{self._matrice[1]}{nl}{self._matrice[2]}]"
        return ch
    
    def txt4chiffres(self):
        """affichage format 4 digites"""
        nl = "\n"
        ch = f"[{self._formatage(self._matrice[0])}{nl}{self._formatage(self._matrice[1])}{nl}{self._formatage(self._matrice[2])}]"
        return ch
    
    def _formatage(self, liste:list) -> str:
        ch_ret = f"{Txt4f.ftPerso(liste[0])} {Txt4f.ftPerso(liste[1])} {Txt4f.ftPerso(liste[2])}"
        return ch_ret
    
    @staticmethod
    def sm_idendite():
        return Matrice3x3(1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0)