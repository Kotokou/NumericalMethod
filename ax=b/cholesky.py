import numpy as np


def cholesky(M, ligne, colonne, B):
    #
    if np.array_equal(M, M.T) and np.all(np.linalg.eigvals(M) > 0):
        L = np.linalg.cholesky(M)
        T = L.T

        # Détermination de y
        y = np.zeros(ligne)
        S = 0
        y[0] = B[0] / L[0, 0]

        for i in range(1, ligne):
            for j in range(i):
                S += L[i, j] * y[j]
            y[i] = (B[i] - S) / L[i, i]
            S = 0

        # détermination de x
        x = np.zeros(ligne)
        x[ligne - 1] = y[ligne - 1] / T[ligne - 1, ligne - 1]

        # remontée
        k, S = 1, 0
        print("cholesky :", end=" ")
        for i in range(ligne - 2, -1, -1):
            for j in range(k):
                S += T[i, j + i + 1] * x[j + i + 1]
            k += 1
            x[i] = (y[i] - S) / T[i, i]
            S = 0
        for i in range(len(x)):
            print(f"x[{i + 1}]={x[i]}".format(), end="")
    else:
        print("La matrice n'est pas symétrique ou/et n'est pas definie positive ")

