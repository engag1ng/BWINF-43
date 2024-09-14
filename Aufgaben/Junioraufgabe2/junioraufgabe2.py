def junioraufgabe2(filename):
    player1 = 0
    player2 = 1
    player1_sprünge = 0
    player2_sprünge = 0

    with open(filename, 'r') as file:
        array = list(file.read())

    for index, item in enumerate(array):
        if item not in letter_dict:
            player1 += 1
            player2 += 1

        if index == player1:
            player1 += letter_dict.get(item)
            player1_sprünge += 1
        if index == player2:
            player2 += letter_dict.get(item)
            player2_sprünge += 1

    if player1_sprünge < player2_sprünge:
        print(f"Player1 wins by {player2_sprünge-player1_sprünge} jumps!")
    elif player2_sprünge > player1_sprünge:
        print(f"Player2 wins by {player1_sprünge-player2_sprünge} jumps!")
    else:
        if player1 > player2:
            print("Player1 wins!")
        elif player1 < player2:
            print("Player2 wins!")
        else:
            print("It's a tie!")

letter_dict = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
    'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26,
    'Ä': 27, 'ä': 27, 'Ö': 28, 'ö': 28, 'Ü': 29, 'ü': 29, 'ß': 30, 
}

junioraufgabe2('hopsenX.txt')