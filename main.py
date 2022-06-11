import numpy as np


def display(matrix):
    for i in range(3):
        for j in range(3):
            print("|", matrix[i, j], end=" ")
        print("|\n-------------")


def gameOver(matrix):
    winner = ["NULL"]
    if line(matrix, winner):
        return True, winner
    if column(matrix, winner):
        return True, winner
    if diag(matrix, winner):
        return True, winner
    if complete(matrix):
        return True, winner
    return False, winner


def line(matrix, winner):
    for i in range(3):
        if matrix[i, :].tolist() == ["X"] * 3:
            winner[0] = "X"
            return True
        if matrix[i, :].tolist() == ["O"] * 3:
            winner[0] = "O"
            return True
    return False


def column(matrix, winner):
    for i in range(3):
        if matrix[:, i].tolist() == ["X"] * 3:
            winner[0] = "X"
            return True
        if matrix[:, i].tolist() == ["O"] * 3:
            winner[0] = "O"
            return True
    return False


def diag(matrix, winner):
    if matrix.diagonal().tolist() == ["X"] * 3 or matrix.diagonal(axis1=1, axis2=0).tolist() == ["X"] * 3:
        winner[0] = "X"
        return True
    if matrix.diagonal().tolist() == ["O"] * 3 or matrix.diagonal(axis1=1, axis2=0).tolist() == ["O"] * 3:
        winner[0] = "O"
        return True
    return False


def complete(matrix):
    for i in range(3):
        for j in range(3):
            if matrix[i, j] != "X" and matrix[i, j] != "O":
                return False
    return True


def validate(matrix, choix):
    if choix[0] < 0 or choix[1] < 0 or choix[0] > 2 or choix[1] > 2:
        print("--indice de case incorrecte, veuillez réessayer--")
        return False
    if matrix[choix[0], choix[1]] == "X" or matrix[choix[0], choix[1]] == "O":
        print("--cette case est déja marquée, choisir une autre--")
        return False
    return True


def play():
    matrix = np.chararray((3, 3), unicode=True)
    matrix[:] = "-"
    i = 0
    players = ["X", "O"]
    winner = ["NULL"]
    while not (gameOver(matrix)[0]):
        display(matrix)
        turn = players[i % 2]
        print(turn, end=" ")
        choix = input(" Quelle case voulez vous jouer ? ")
        choix = list(map(int, choix.split(" ")))
        print(choix)
        if validate(matrix, choix):
            matrix[choix[0], choix[1]] = turn
            i += 1

    winner = gameOver(matrix)[1]
    display(matrix)
    print("Le jeu est terminé !\nGagnant: ", winner)


play()
