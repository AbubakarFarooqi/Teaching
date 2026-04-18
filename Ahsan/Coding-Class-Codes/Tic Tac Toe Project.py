import os
import time
player_x="X"
player_o="O"

board=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
   ]


WIN_PATTERNS = [
(0,1,2),(3,4,5),(6,7,8),
(0,3,6),(1,4,7),(2,5,8),
(0,4,8),(2,4,6)
]

def print_board():
    print (f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print (f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print (f"{board[2][0]} | {board[2][1]} | {board[2][2]}")

def turn(player):
    position=input("Enter position -> ")
    row=0
    col=0
    if position == "1":
        row=0
        col=0
    elif position == "2":
        row=0
        col=1
    elif position == "3":
        row=0
        col=2
    elif position == "4":
        row=1
        col=0
    elif position == "5":
        row=1
        col=1
    elif position == "6":
        row=1
        col=2
    elif position == "7":
        row=2
        col=0
    elif position == "8":
        row=2
        col=1
    elif position == "9":
        row=2
        col=2
    else:
        print ("Not a valid position")

    if board[row][col] != " ":
        print ("It's not a valid position!")
        time.sleep(1)
    else:
        board[row][col] = player

def change_turn(current_player):
    if current_player == player_x:
        return player_o
    return player_x

def get_cords(position):
    if position == "0":
        return (0,0)
    elif position == "1":
        return (0,1)
    elif position == "2":
        return (0,2)
    elif position == "3":
        return (1,0)
    elif position == "4":
        return (1,1)
    elif position == "5":
        return (1,2)
    elif position == "6":
        return (2,0)
    elif position == "7":
        return (2,1)
    elif position == "8":
        return (2,2)


def check_winner():
    for a,b,c in WIN_PATTERNS:
        row_a,col_a = get_cords(str(a))
        row_b,col_b = get_cords(str(b))
        row_c,col_c = get_cords (str(c))
        if board[row_a][col_a] == board[row_b][col_b] == board[row_c][col_c] and  board[row_a][col_a] != " ":
            return board[row_a][col_a]

    is_tie = True
    for row in range (3):
        for col in range (3):
            if board[row][col] == " ":
                is_tie = False
    if is_tie:
        return 'tie'
    return None



if __name__ == "__main__":
    player = player_x
    while True:
        os.system('cls')
        print_board()
        turn(player)
        player = change_turn(player)
        state = check_winner()
        if state=='tie':
            print("The game is a tie.")
            break
        if state == player_x:
            print (f"{player_x} wins!")
            break
        if state == player_o:
            print (f"{player_o} wins!")
            break


