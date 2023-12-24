import numpy as np

# gauss
lr = []


def gauss(ligne, M, B, x):
    m = np.append(M, B, axis=1)
    # methode Gauss
    # echelonnement
    for i in range(ligne):
        for j in range(i):
            if m[j, j] == 0 or M[j, j] == 0:
                print("division par zero ")
                return 0
            else:
                m[i] = m[i] - m[i, j] / m[j, j] * m[j]
                M[i] = M[i] - M[i, j] / M[j, j] * M[j]
    B = m[:, -1]
    x[ligne - 1] = B[ligne - 1] / M[ligne - 1, ligne - 1]
    # remontée
    k, S = 1, 0
    for i in range(ligne - 2, -1, -1):
        for j in range(k):
            S += M[i, j + i + 1] * x[j + i + 1]
        k += 1
        x[i] = (B[i] - S) / M[i, i]
        S = 0
    print("gauss:", end=" ")
    for i in range(ligne):
        print(f"x[{i + 1}]={x[i]}".format(), end="    ")
