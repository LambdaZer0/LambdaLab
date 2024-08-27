from oop_exercises_s2 import Domino
from oop_exercices_s3 import CompteBancaire, AccelerationDistance, Satellite
from oop_exercises_s4 import Cercle

# liste_dom = []
# for x in range(0, 7):
#     for y in range(0, x+1):
#         dom = Domino(y,x)
#         liste_dom.append(dom)
# for cpt, elem in enumerate(liste_dom):
#     print(f"{cpt+1} => {elem} avec une somme des faces = {elem.sommeFaces()}")


# compte1 = CompteBancaire("AZ123", "Aboubakr", 10000)

# compte1.retirer(450)
# compte1.verser(500)
# compte1.verser(5000)
# compte1.retirer(500)

# print("=> listing des écritures ---")
# listing = compte1.getListingEcriture()
# for cpt, elem_tup in enumerate(listing):
#     tab = "\t"
#     type_ecr = elem_tup[0]
#     ch = f"{cpt+1}:{tab}{type_ecr}"
#     montant = elem_tup[1]
#     if type_ecr == "solde initial":
#         ch += f"{tab}+{montant}"
#     elif type_ecr == "versement":
#         ch += f"{tab}+{montant}"
#     elif type_ecr == "retrait":
#         ch += f"{tab}{tab}-{montant}"
#     solde = elem_tup[2]
#     if solde >= 0:
#         ch += f"{tab}{tab}+{solde}"
#     else:
#         ch += f"{tab}{tab}-{solde}"
#     print(ch)

# print("=> calculer la vitesse finale ----")
# val_vit_ini = 0
# val_acc = 2
# val_dist = 9
# formu = AccelerationDistance(u_vit_ini=val_vit_ini, a_acc=val_acc, s_dist=val_dist)
# print("valeur des attribus = ", formu.__dict__)
# tup_res = formu.calculerComposante()
# print(tup_res)
# print("la vitesse finale est de ", tup_res[1], "m/s")

# print("=> calculer l'accéleration' ----")
# val_vit_ini = 0
# val_vit_finale = 12
# val_dist = 8
# formu = AccelerationDistance(v_vit_fin=val_vit_finale, u_vit_ini=val_vit_ini, s_dist=val_dist)
# print("valeur des attribus = ", formu.__dict__)
# tup_res = formu.calculerComposante()
# print(tup_res)
# print("l'accéleration est de ", tup_res[1], "m/s²")

# print("=> calculer la vitesse initiale' ----")
# val_acc = 5
# val_vit_finale = 14
# val_dist = 17.1
# formu = AccelerationDistance(v_vit_fin=val_vit_finale, a_acc=val_acc, s_dist=val_dist)
# print("valeur des attribus = ", formu.__dict__)
# tup_res = formu.calculerComposante()
# print(tup_res)
# print("la vitesse initiale est de ", tup_res[1], "m/s")

# print("=> calculer la distance' ----")
# val_vit_ini = 0
# val_acc = 1.65
# val_vit_finale = 5.745
# formu = AccelerationDistance(u_vit_ini=val_vit_ini, v_vit_fin=val_vit_finale, a_acc=val_acc)
# print("valeur des attribus = ", formu.__dict__)
# tup_res = formu.calculerComposante()
# print(tup_res)
# print("la distance est de ", tup_res[1], "m")

# print("=> calculer la distance' ----")
# val_vit_ini = 30
# val_acc = -10
# val_vit_finale = 0
# formu = AccelerationDistance(u_vit_ini=val_vit_ini, v_vit_fin=val_vit_finale, a_acc=val_acc)
# print("valeur des attribus = ", formu.__dict__)
# tup_res = formu.calculerComposante()
# print(tup_res)
# print("la distance est de ", tup_res[1], "m")

# sat_zoe = Satellite(identifiant="zoe456", masse_kg=450, vitesse_ms=30)
# print(sat_zoe)
# print(sat_zoe.__dict__)
# print(sat_zoe.txtVitesseEnCours())
# varia = sat_zoe.appliquerImpulsion(500, 15)
# print(f"variation = {varia} m/s")
# print(sat_zoe.txtVitesseEnCours())
# print(f"énergie cinétique = {sat_zoe.energieCinetique()} joules")

cc = Cercle(5)
print(cc)
print(cc.__dict__)
sf_cc = cc.surface()
print(f"la surface du cerle = {sf_cc}")
cf_cc = cc.circonference()
print(f"la circonférence du cercle = {cf_cc}")