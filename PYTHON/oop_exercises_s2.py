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