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
    
    @staticmethod
    def sm_multiplier(mat3x3, mat3x1):
        """multiplier 3x3 par 3x1 pour donner 3x1"""
        mat3x3_lig1 = mat3x3.ligMat(1)
        # print("mat3x3_lig1 = ", mat3x3_lig1)
        mat3x3_lig2 = mat3x3.ligMat(2)
        # print("mat3x3_lig2 = ", mat3x3_lig2)
        mat3x3_lig3 = mat3x3.ligMat(3)
        # print("mat3x3_lig3 = ", mat3x3_lig3)
        mat3x1_col = mat3x1.colMat()
        # print("mat3x1_col = ", mat3x1_col)
        res_mat3x1_c11 = Matrice3x3._produitListeParListe(mat3x3_lig1, mat3x1_col)
        # print("rest_mat3x1_c11 = ", res_mat3x1_c11)
        res_mat3x1_c12 = Matrice3x3._produitListeParListe(mat3x3_lig2, mat3x1_col)
        # print("rest_mat3x1_c12 = ", res_mat3x1_c12)
        res_mat3x1_c13 = Matrice3x3._produitListeParListe(mat3x3_lig3, mat3x1_col)
        # print("rest_mat3x1_c13 = ", res_mat3x1_c13)
        return Matrice3x1(res_mat3x1_c11, res_mat3x1_c12, res_mat3x1_c13)
    
    def ligMat(self, ind_1_3:int) -> list:
        """obtenir une ligne de la matrice"""
        return self._matrice[ind_1_3 - 1]
    
    def _produitListeParListe(liste1:list, liste2:list) -> float:
        """produit list1 par liste2 qui sont des listes une dimension"""
        # print(liste1)
        # print(liste2)
        produit = [x * y for x, y in zip(liste1, liste2)]
        # print(produit)
        cp = 0
        for xx in produit:
            cp += xx
        return cp
    

class Matrice3x1:
    """classe utilisée pour gérer une matrice de dimension 3 par 1"""
    
    def __init__(self, a11:float, a21:float, a31:float) -> None:
        """constructeur de la matrice 3x1"""
        self._matrice = []
        self._matrice.append([a11])
        self._matrice.append([a21])
        self._matrice.append([a31])

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
        ch_ret = f"{Txt4f.ftPerso(liste[0])}"
        return ch_ret

    def ligMat(self, ind_1_3:int) -> list:
        """obtenir un ligne de la matrice"""
        return self._matrice[ind_1_3 - 1]
    
    def colMat(self) -> list:
        """obtenir une colonne de la matrice 
        retournee sous forme d une liste unique"""
        liste_retour = []
        liste_retour.append(self.ligMat(1)[0])
        liste_retour.append(self.ligMat(2)[0])
        liste_retour.append(self.ligMat(3)[0])
        return liste_retour
    