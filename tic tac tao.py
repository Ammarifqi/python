"""
    |     |  x
----------------
    |     |
----------------
    |     |  o
"""

current_postions = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def display_board(positions):
    for x in range(3):
        print(" " + positions[x*3] + " | " + positions[(x*3) + 1] + " | " + positions[(x*3) +2] + " ")
        if x != 2:
           print("-----------")


def insert_symbol(player, positions):

    coordinate = int(input())
    if player == "x":
        positions[coordinate-1] = "x"
    elif player == "o":
        positions[coordinate-1] = "o"

def is_win(player, positions):

    #Horizontal
    for x in range(3):
        if positions[x*3] == player:
            if positions[x*3 + 1] == player and positions[x*3 + 2] == player:
                return True

    #VERTICAL
    for x in range(3):
        if positions[x] == player:
            if positions[x + 3] == player and positions[x + 6] == player:
                return True

    # Diagonal
    if positions[0] == player:
        if positions[4] == player and positions[8] == player:
            return True
    if positions[6] == player:
        if positions[4] == player and positions[2] == player:
            return True


    return False

def is_draw(positions):
    for symbol in positions:
        if symbol == " ":
            return False

    return True


def start_game(player, initial_position ):

    turn = player
    won = False
    curr_postion = initial_position

    while not won:
        display_board(curr_postion)

        print(turn + " please enter you coordinate:")
        insert_symbol(turn, curr_postion)

        if is_win(turn, curr_postion):
            display_board(curr_postion)
            print(turn + " won the game")
            won = True
            break
        elif is_draw(curr_postion):
            display_board(curr_postion)
            print(" it ts draw ")
            won = True
            break
        else:
            if turn == "x":
                turn = "o"
            else:
                turn = "x"





current_postions = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


start_game("x", current_postions)