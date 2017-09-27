def checkio(game_result):
    row1 = ''.join(game_result[0])
    row2 = ''.join(game_result[1])
    row3 = ''.join(game_result[2])

    if  (row1[0] == row2[0] == row3[0] and row1[0] == 'X' or
        row1[1] == row2[1] == row3[1] and row1[1] == 'X' or
        row1[2] == row2[2] == row3[2] and row1[2] == 'X' or
        row1[0] == row2[1] == row3[2] and row1[0] == 'X' or
        row1[2] == row2[1] == row3[0] and row3[0] == 'X' or
        row1[0] == row1[1] == row1[2] and row1[2] == 'X' or
        row2[0] == row2[1] == row2[2] and row2[2] == 'X' or
        row3[0] == row3[1] == row3[2] and row3[2] == 'X'):
        return "X"

    elif (row1[0] == row2[0] == row3[0] and row1[0] == 'O' or
        row1[1] == row2[1] == row3[1] and row1[1] == 'O' or
        row1[2] == row2[2] == row3[2] and row1[2] == 'O' or
        row1[0] == row2[1] == row3[2] and row1[0] == 'O' or
        row1[2] == row2[1] == row3[0] and row3[0] == 'O' or
        row1[0] == row1[1] == row1[2] and row1[2] == 'O' or
        row2[0] == row2[1] == row2[2] and row2[2] == 'O' or
        row3[0] == row3[1] == row3[2] and row3[2] == 'O'):
        return "O"
    else:
        return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
