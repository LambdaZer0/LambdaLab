from oop_exercices_new import Domino

liste_dom = []
for x in range(0, 7):
    for y in range(0, x+1):
        dom = Domino(y,x)
        liste_dom.append(dom)
for cpt, elem in enumerate(liste_dom):
    print(f"{cpt+1} => {elem} avec une somme des faces = {elem.sommeFaces()}")
    