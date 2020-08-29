# ------ global variables ------

#  board game
board = ["_","_","_",
         "_","_","_",
         "_","_","_"]

#  if game is still going

game_still_on = True

# winner
winner = None
current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

display_board()

def handle_turn(player):
        position = input("Choose a number from 1-9: ")
        position = int(position) - 1

        board[position] = 'X'
        display_board()

def play_game():

    #display the board
    # display_board()
    def check_if_game_over():
        check_if_win()
        check_if_tie()

    def check_if_win():
        # check rows, columns and diagonals
        return
    def check_if_tie():
        return
    def flip_player():
        return

    while game_still_on:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

        if winner == "X" or winner == "O":
            print(winner + " won.")
        elif winner == None:
            print("It is a tie!!")




play_game()


