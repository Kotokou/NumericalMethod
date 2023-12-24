import numpy as np


def check_matrice(A, ligne):
    for i in range(ligne):
        for j in range(ligne):
            if abs(A[i, i]) > (sum(A[i]) - A[i, i]):
                return True
            else:
                return False


def Jacobi(A, B, x, n, ligne):
    D = np.diag(A)
    if check_matrice(np.copy(A), ligne):
        R = A - np.diagflat(D)
        for i in range(n):
            x = (B - np.dot(R, x)) / D
        print(x)
    else:
        print("Ne converge pas ")


A = np.array([
    [3, 0, 0],
    [1, 2, 0],
    [3, 2, 1]
])
b = [9, 7, 14]
x = [0, 0, 0]

# Si a est une matrice à diag sup dominante alors, pour tt choix de x exp b appart à N, converge
# matrice carree à coeff reel ou complexe est dite diag dominante lorsque la valeur absolue de chque terme est sup ou = à la somme des valeurs abs des termes de sa ligne
#
