from oop_exercices_s5 import Matrice3x3

mat3x3_1 = Matrice3x3(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0)
print("affichage de l'instance")
print(mat3x3_1)
print("affichage 4 digites")
print(mat3x3_1.txt4chiffres())

mat3x3_2 = Matrice3x3(9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0)
print("affichage de l'instance")
print(mat3x3_2)
print("affichage 4 digites")
print(mat3x3_2.txt4chiffres())

print("on effectue le produit matriciel ----------")
mat3x3_1.multiplier(mat3x3_2)
print("affichage de l'instance")
print(mat3x3_1)
print("affichage 4 digites")
print(mat3x3_1.txt4chiffres())
