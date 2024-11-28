from random import randrange

li = []
inf = int(input("borne inf: "))
sup = int(input("borne sup: "))

nb_op= int(input("Nombre d'opérations: "))

for i in range(nb_op):
    li.append((randrange(inf, sup), randrange(inf, sup)))

lo = []
lc = []
for x in li:
    lo.append(x[0] + x[1])
    op = int(input(f"{x[0]} + {x[1]} = "))
    lc.append(op)


for x in li:
    lo.append(x[0] + x[1])

rep = input("Afficher le résultat ?")

compare = []
if rep :
    for i, x in enumerate(zip(li, lo, lc)):
        compare.append(x[1] == x[2])
        print(f"{i+1}){x[0][0]} + {x[0][1]} = {x[1]} = {x[2]} : {x[1] == x[2]}")

score = compare.count(True)*100/len(compare)
score = "{:.2f}".format(score)
print(f"Votre score : {score}%")