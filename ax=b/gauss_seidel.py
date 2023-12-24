import fonction as fct


def gauss_seidel(matrice, b, X_0, nb_iter, epsi):
    k = 1
    X_n = X_0  # Xn
    X_n_1 = []  # Xn+1
    convergence = False
    while k <= nb_iter:
        temp = []
        i = 0
        while i < len(matrice):
            j = 0
            somme1 = 0
            while j <= i - 1:
                somme1 += (matrice[i][j] / matrice[i][i]) * temp[j]
                j += 1

            somme2 = 0
            j = i + 1
            while j < len(matrice):
                somme2 += (matrice[i][j] / matrice[i][i]) * X_n[j]
                j += 1
            somme = 0
            somme += (b[i] / matrice[i][i]) - (somme1 + somme2)
            temp.append(somme)
            i += 1
        X_n_1 = temp

        X_n_1_X_n = fct.soustraction_matrice_ligne(X_n_1, X_n)
        norme_X_n_1_X_n = fct.norme_matrice(X_n_1_X_n)
        norme_X_n_1 = fct.norme_matrice(X_n_1)

        if (norme_X_n_1_X_n / norme_X_n_1) < epsi:  # condition darrêt

            print("******************CONVERGENCE ATTEINTE******************\n")
            print("X = X_{} = {}\n".format(k, X_n_1))
            convergence = True
            break
        else:
            X_n = X_n_1
            k += 1
    if not convergence:
        print("xxxxxxxxxxxxxxxxxxx CONVERGENCE NON ATTEINTE AVEC {} INTERATIONS xxxxxxxxxxxxxxxxxxx\n".format(nb_iter))
