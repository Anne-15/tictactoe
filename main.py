board = ["_","_","_",
         "_","_","_",
         "_","_","_"]

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

display_board()

def play_game():

#display the board
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()


def handle_turn():
    position = input("Choose a number from 1-9: ")
    position = int(position) - 1

    board[position] = 'X'
    display_board()

    handle_turn()
play_game()


