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