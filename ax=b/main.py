import numpy as np
import pyfiglet
import gauss
import LU
from jacobi import Jacobi
import gauss_seidel
import gauss_jordan
import cholesky

# Code à prendre en compte et à personnalisé pour le devoir 2023-2024 Ax=b
text = 'AX = B'
print((pyfiglet.figlet_format(text, font="slant")))

# Ligne et colonnes de la matrice
ligne = int(input("Entrez le nombre de lignes:"))
colonne = int(input("Entrez le nombre de colonnes:"))
#
while ligne != colonne:
    print("La matrice n'est pas carree. Veuillez ressaisir les donnees s'il vous plait")
    colonne = int(input("Entrez le nombre de colonnes de la matrice: "))
    ligne = int(input("Entrez le nombre de lignes de la matrice: "))

# entrer les éléments dans la matrice
# initialiser la matrice
M = np.zeros((ligne, colonne))
print("*******************************Entrée des donneés de la matrice *****************************")
# Entrée des données dans la matrice
for i in range(ligne):
    for j in range(colonne):
        elt = int(input(f"entrez l'élément M[{i + 1},{j + 1}]=".format()))
        M[i, j] = elt
m = np.copy(M)
print("********* Elements de B ********")
# entrée des coordonnées de B
B = np.zeros((ligne, 1))
bb = []
for i in range(ligne):
    b = int(input(f"Entrez les coordonnées de B[{i + 1}]=".format()))
    B[i] = b
    bb.append(b)

X_0 = np.zeros(ligne - 1)
x = np.zeros(ligne)
print(
    ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> SOLUTIONS DES DIFFERENTES METHODES <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

# gauss
print("\n @@@@@@@@@@@@@@@@@@@@@@ GAUSS @@@@@@@@@@@@@@@@@@@@@")
gauss.gauss(ligne, np.copy(M), B, x)
# Lu9
print("\n @@@@@@@@@@@@@@@@@@@@@@ LU @@@@@@@@@@@@@@@@@@@@@")
LU.LU(np.copy(M), ligne, B)
# cholesky
print("\n @@@@@@@@@@@@@@@@@@@@@@ CHOLESKY @@@@@@@@@@@@@@@@@@@@@")
cholesky.cholesky(np.copy(M), ligne, colonne, B)
# Jacobi
print("\n @@@@@@@@@@@@@@@@@@@@@@ JACOBI @@@@@@@@@@@@@@@@@@@@@")
Jacobi(np.copy(M), bb, x, 5, ligne)
# gauss_seidel
print("\n @@@@@@@@@@@@@@@@@@@@@@ GAUSS-SEIDEL @@@@@@@@@@@@@@@@@@@@@")
x = np.zeros(ligne)
gauss_seidel.gauss_seidel(np.copy(M), B, x, 100, 0.00000001)
# gauss_jordan
print("\n @@@@@@@@@@@@@@@@@@@@@@ GAUSS-JORDAN @@@@@@@@@@@@@@@@@@@@@")
gauss_jordan.gauss_jordan(np.copy(M), ligne, colonne)
