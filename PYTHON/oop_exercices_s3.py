
""" Nouveau programme apprentissage OOP"""
import math

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
    
class AccelerationDistance:
    """"""
    def __init__(self, v_vit_fin:float=None, u_vit_ini:float=None, a_acc:float=None, s_dist:float=None) -> None:
        """constructeur de classe acceleration: initialiser les 4 composantes de la formules"""
        self._vitesse_finale_v = v_vit_fin
        self._vitesse_initiale_u = u_vit_ini
        self._acceleration_a = a_acc
        self._distance_s = s_dist
    
    def calculerVitesseFinale(self) -> tuple:
        """cette methode permet de calculer de la vitesse finale a partir de la formule
        V² = u² + 2as"""
        vit_vi = math.sqrt(self._vitesse_initiale_u **2 + 2*self._acceleration_a*self._distance_s)
        return ("vitesse finale v", vit_vi)
    
    def calculerAcceleration(self) -> tuple:
        """cette methode permet de calculer de l acceleration a partir de la formule
        V² = u² + 2as"""
        acc_a = (self._vitesse_finale_v**2 - self._vitesse_initiale_u**2) / (2*self._distance_s)
        return ("acceleration a", acc_a)
    
    def calculerVitesseInitiale(self) -> tuple:
        """cette methode permet de calculer de la vitess initiale a partir de la formule
        V² = u² + 2as"""
        vit_u = math.sqrt(self._vitesse_finale_v **2 - 2*self._acceleration_a*self._distance_s)
        return ("vitesse initiale u", vit_u)
    
    def calculerDistance(self) -> tuple:
        """cette methode permet de calculer de la vitess initiale a partir de la formule
        V² = u² + 2as"""
        dist_s = (self._vitesse_finale_v **2 - self._vitesse_initiale_u**2) / (2*self._acceleration_a)
        return ("distance s", dist_s)
    
    def calculerComposante(self) -> tuple:
        """cette methode permet de calculer la composante manquante parmi les 4 autres"""
        cpt_erreur = 0
        if self._vitesse_initiale_u == None:
            cpt_erreur += 1
        if self._acceleration_a == None:
            cpt_erreur += 1
        if self._distance_s == None:
            cpt_erreur += 1
        if self._vitesse_finale_v == None:
            cpt_erreur += 1
        if cpt_erreur > 1:
            raise Exception("au moins 3/4 des composantes doit etre renseignees")
        if self._vitesse_finale_v == None:
            return self.calculerVitesseFinale()
        if self._acceleration_a == None:
            return self.calculerAcceleration()
        if self._vitesse_initiale_u == None:
            return self.calculerVitesseInitiale()
        if self._distance_s== None:
            return self.calculerDistance()

class Satellite:
    """classe qui modelise la fiche technique d un satellite, elle comprend 3 attribus
    -identidiant
    -masse en kg
    vitesse en m/s"""

    def __init__(self, identifiant: str="nd", masse_kg: float=0, vitesse_ms: float=0) -> None:
        """constructeur de la classe satellite"""
        self._identifiant = identifiant
        self._masse_kg = masse_kg
        self._vitesse_ms = vitesse_ms
    
    def __repr__(self) -> str:
        """affichage personnalise de la classe"""
        nl = "\n"
        ch = f"identfiant: {self._identifiant}{nl}masse (kg): {self._masse_kg}{nl}vitesse (m/s): {self._vitesse_ms}"
        return ch
    
    def txtVitesseEnCours(self) -> str:
        """affichage de la vitesse a un moment donne"""
        ch = f"vitesse en cours = {self._vitesse_ms} m/s"
        return ch

    def appliquerImpulsion(self, f_newton:float, t_seconde:float) -> float:
        """appliquer une impulsion au satellite"""
        delta_v = (f_newton * t_seconde) / self._masse_kg
        self._vitesse_ms += delta_v
        return delta_v
    
    def energieCinetique(self) -> float:
        ec = (self._masse_kg * self._vitesse_ms**2)/2
        return ec
    