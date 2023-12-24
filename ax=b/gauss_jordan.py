import numpy as np


def gauss_jordan(M, ligne, colonne):
    M = np.zeros((ligne, ligne + 1))
    # Entrée des données dans la matrice
    for i in range(ligne):
        for j in range(colonne + 1):
            elt = int(input(f"entrez l'élément M[{i + 1},{j + 1}]=".format()))
            M[i, j] = elt

    for i in range(ligne):
        for j in range(colonne):
            if i != j:
                div = M[j, i] / M[i, i]
                for k in range(ligne + 1):
                    M[j, k] = M[j, k] - div * M[i, k]
    x = np.zeros(ligne)
    # solution
    for i in range(ligne):
        x[i] = M[i, ligne] / M[i, i]

    for i in range(len(x)):
        print(f"x[{i}] = {x[i]}".format())


A = np.array([
    [1, 2, -1],
    [2, 1, 1],
    [1, 0, 2]
])
b = [5, 10, 0]
