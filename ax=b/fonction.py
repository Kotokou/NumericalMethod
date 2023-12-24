import math


# récupéré la matrice et le second membre
def get_matrices():
    i = 1
    matrice = []

    taille = int(input("----->Quelle est la taille de la matrice : "))
    while i <= taille:
        print("-----Entrer les a{}k-------".format(i))
        j = 1
        lignes_matrices = []
        while j <= taille:
            a = float(input("a{}{} = ".format(i, j)))
            lignes_matrices.append(a)
            j += 1
        matrice.append(lignes_matrices)
        i += 1

    print("======MATRICE======\n{}\n".format(matrice))

    print("Entrer les élement du second membre")
    index = 1
    sencond_member = []
    while index <= taille:
        e = float(input("b{} = ".format(index)))
        sencond_member.append(e)
        index += 1
    print("======SECOND MEMBRE======\n{}\n".format(sencond_member))
    return matrice, sencond_member


# avoir la nature augmenté d'une matrice
def matrice_aug(matrice, second_memb):
    i = 0
    while i < len(matrice):
        matrice[i].append(second_memb[i])
        i += 1
    return matrice


# recupération de la matrice augmenté
def added_matrice():
    matrice, second_member = get_matrices()
    return matrice_aug(matrice, second_member)


# fonction pour la descente triangulaire
def triangular_descent(matrice):
    matrice_Y = [matrice[0][-1] / matrice[0][0]]
    matrice_lengh = len(matrice)
    i = 1
    while i < matrice_lengh:
        reducer = matrice[i][-1]
        k = 0
        while k <= i - 1:
            reducer -= matrice[i][k] * matrice_Y[k]
            k += 1
        matrice_Y.append(reducer / matrice[i][i])
        i += 1
    print(matrice_Y)
    return matrice_Y


# fonction pour la remontée triangulaire
def triangular_lift(matrice):
    matrice_X = [matrice[-1][-1] / matrice[-1][-2]]
    matrice_lengh = len(matrice)
    i = -2
    while matrice_lengh - 1 > 0:
        matrice_lengh -= 1
        j = -2
        k = 1
        reducer = matrice[i][-1]
        while k < abs(i):
            reducer -= matrice[i][j] * matrice_X[j + 1]
            j -= 1
            k += 1
        matrice_X.insert(i, reducer / matrice[i][i - 1])
        i += -1
    return matrice_X


# matrice identitée de taille N
def matrice_ident(N):
    matrice = []

    i = 0
    j = 0
    while i < N:
        temp_row = []
        while j < N:
            if j == i:
                temp_row.append(1)
                j += 1
            else:
                temp_row.append(0)
                j += 1
        matrice.append(temp_row)
        j = 0
        i += 1
    return matrice


# inverse d'une matrice
def inverse_matrice(matrice, N):
    l = 0
    while l < N:
        matrice[l].extend(matrice_ident(N)[l])
        l += 1
    # GAUSS JORDAN

    i = 0
    while i < N:
        j = i
        temp_tab = []
        while j < N:
            temp_tab.append(matrice[j][i])
            j += 1
        index = 0
        find_index = 0
        max = abs(temp_tab[0])
        for element in temp_tab:
            if max < abs(element):
                max = abs(element)
                find_index = index
                index += 1
                continue
            else:
                index += 1
        if max == abs(temp_tab[0]):
            find_index = 0
        matrice[i], matrice[i + find_index] = matrice[i + find_index], matrice[i]

        # méthode de gauss
        newline = []
        for element in matrice[i]:
            newline.append(element / matrice[i][i])
        matrice[i] = newline
        j = i + 1
        while j < N:
            index = 0
            temp_tab = []
            for element in newline:
                if index <= i:
                    temp_tab.append(0)
                    index += 1
                else:
                    temp_tab.append((-1) * matrice[j][i] * element + matrice[j][index])
                    index += 1
            matrice[j] = temp_tab
            j += 1
        i += 1

    i = -2

    while abs(i) - 1 <= N - 1:
        matrice_to_change = matrice[i]
        k = 1
        while k < abs(i):
            matrice_calcul = matrice[-k]

            numb = matrice_to_change[-N - k]
            matrice[i][-N - k] = 0
            j = N
            while j < 2 * N:
                matrice[i][j] += (-1) * numb * matrice_calcul[j]
                j += 1
            k += 1
        i += -1

    i = 0
    resultat = []
    while i < N:
        temp_tab = []
        j = N
        while j < 2 * N:
            temp_tab.append(matrice[i][j])
            j += 1
        resultat.append(temp_tab)
        i += 1
    return resultat


# recupéré la matrice trianguaire inférieur
def inf_triangular_matrice(matrice, N):
    triangula_matrice = []
    i = 0
    while i < N:
        j = 0
        temp_tab = []
        while j < N:
            if j < i:
                temp_tab.append(matrice[i][j])
                j += 1
            else:
                temp_tab.append(0)
                j += 1
        triangula_matrice.append(temp_tab)
        i += 1
    return triangula_matrice


# recupéré la matrice trianguaire supérieur
def sup_triangular_matrice(matrice, N):
    triangula_matrice = []
    i = 0
    while i < N:
        j = 0
        temp_tab = []
        while j < N:
            if j <= i:
                temp_tab.append(0)
                j += 1
            else:
                temp_tab.append(matrice[i][j])
                j += 1
        triangula_matrice.append(temp_tab)
        i += 1
    return triangula_matrice


# récupéré la matrice diagonal
def diagonal_matrice(matrice, N):
    diag_matrice = []
    i = 0
    while i < N:
        temp_tab = []
        j = 0
        while j < N:
            if i == j:
                temp_tab.append(matrice[j][j])
                j += 1
            else:
                temp_tab.append(0)
                j += 1
        diag_matrice.append(temp_tab)
        i += 1
    return diag_matrice


def restart():
    answer = input("Voulez-vous recommencer? O/N : ")
    answer = answer.lower()
    if answer == "0":
        print("\n\n===========RESTART THE PROGRAM=========\n\n")
        return True
    else:
        print("\n\n===========END OF THE PROGRAM=========\n\n")
        return False


def transpose(matrice, N):
    i = 0
    matrice_trans = matrice_ident(N)
    while i < N:
        j = 0
        while j < N:
            matrice_trans[i][j] = matrice[j][i]
            matrice_trans[j][i] = matrice[i][j]
            j += 1
        i += 1
    return matrice_trans


def somme_matrice(matrice1, matrice2, N):
    resultat = matrice_ident(N)
    i = 0
    while i < N:
        j = 0
        while j < N:
            resultat[i][j] = matrice1[i][j] + matrice2[i][j]
            j += 1
        i += 1
    return resultat


def soustraction_matrice(matrice1, matrice2, N):
    resultat = matrice_ident(N)
    i = 0
    while i < N:
        j = 0
        while j < N:
            resultat[i][j] = matrice1[i][j] - matrice2[i][j]
            j += 1
        i += 1
    return resultat


def soustraction_matrice_ligne(matrice1, matrice2):
    i = 0
    result = []
    while i < len(matrice1):
        result.append(0)
        i += 1
    i = 0
    while i < len(matrice1):
        result[i] = matrice1[i] - matrice2[i]
        i += 1
    return result


def norme_matrice(matrice):  # matrice ligne ou colonne
    somme = 0
    for element in matrice:
        somme += element ** 2
    return math.sqrt(somme)


# Fonctions de vérification de la convergence des methodes de calculs

def diag_dominante(matrice):  # vérifié si la matrice est à diagonale dominante
    i = 0
    while i < len(matrice):
        j = 0
        somme = 0
        while j < len(matrice):
            if j != i:
                somme += abs(matrice[i][j])
                j += 1
            else:
                j += 1
        if abs(matrice[i][i]) <= somme:
            i += 1
        else:
            print("---------------La matrice n'est pas à diagonales dominante---------------\n")
            return False
        if i == len(matrice):
            print("-->La matrice est à diagonales dominante\n")
            return True


def symetrique(matrice):  # vérifier si la matrice est symétrique  CHECKED
    matrice_t = transpose(matrice, len(matrice))
    if matrice_t == matrice:
        print("--->La matrice est Symétrique\n")
        return True
    else:
        print("--->La matrice n'est pas Symétrique\n")
        return False

