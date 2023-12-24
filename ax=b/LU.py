import numpy as np
from fractions import Fraction


# methode_LU
def LU(M, ligne, B):
    colonne = ligne
    U = np.copy(M)
    L = np.identity(ligne)
    # decomposition de la matrice
    for i in range(ligne):
        if U[i, i] == 0:
            print("division par zero détectée")
            return 0
        for j in range(i + 1, ligne):
            L[j, i] = U[j, i] / U[i, i]
            U[j] = U[j] - L[j, i] * U[i]

    # determinatioN de Y
    y = np.zeros((ligne, 1))
    for i in range(ligne):
        y[i] = B[i]
        for j in range(i):
            y[i] = y[i] - L[i, j] * y[j]
    AffichY = np.copy(y)
    j = 0
    for i in AffichY.tolist():
        print("y[{}]=".format(j), Fraction(*i).limit_denominator(), end='  ')
        j += 1
    # détermination de X
    x = np.zeros((ligne, 1))
    for i in range(ligne - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, ligne):
            x[i] = x[i] - U[i, j] * x[j]
        x[i] = x[i] / U[i, i]
    AffichX = np.copy(x)
    j = 0
    print("\n")
    for i in AffichX.tolist():
        print("x[{}]=".format(j), Fraction(*i).limit_denominator(), end='  ')
        j += 1


"""A = np.array([[1,2,-1],[2,1,1],[1,0,2]])

x = [0,0,0]
b = [5,10,0]
LU(A,3,b)"""
