from oop_exercices_new import Domino, CompteBancaire

# liste_dom = []
# for x in range(0, 7):
#     for y in range(0, x+1):
#         dom = Domino(y,x)
#         liste_dom.append(dom)
# for cpt, elem in enumerate(liste_dom):
#     print(f"{cpt+1} => {elem} avec une somme des faces = {elem.sommeFaces()}")


compte1 = CompteBancaire("AZ123", "Aboubakr", 10000)
compte1.retirer(450)
compte1.verser(500)
compte1.verser(5000)
compte1.retirer(500)

print("=> listing des écritures ---")
listing = compte1.getListingEcriture()
for cpt, elem_tup in enumerate(listing):
    tab = "\t"
    type_ecr = elem_tup[0]
    ch = f"{cpt+1}:{tab}{type_ecr}"
    montant = elem_tup[1]
    if type_ecr == "solde initial":
        ch += f"{tab}+{montant}"
    elif type_ecr == "versement":
        ch += f"{tab}+{montant}"
    elif type_ecr == "retrait":
        ch += f"{tab}{tab}-{montant}"
    solde = elem_tup[2]
    if solde >= 0:
        ch += f"{tab}{tab}+{solde}"
    else:
        ch += f"{tab}{tab}-{solde}"
    print(ch)