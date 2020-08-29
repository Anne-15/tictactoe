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

# display board game of tictactoe
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# display_board()

# handle a single turn per player
def handle_turn(player):
        position = input("Choose a number from 1-9: ")
        position = int(position) - 1

        board[position] = 'X'
        # display_board()

# play game function
def play_game():

    #display the board
    display_board()
    # check if the game is over
    def check_if_game_over():
        check_for_winner()
        check_if_tie()

    # check if there is a winner between x and o
    def check_for_winner():
        global winner

        # check rows, columns and diagonals
        row_winner = check_rows()
        column_winner = check_columns()
        diagonal_winner = check_diagonals()

        # get the winner
        if row_winner:
            winner = row_winner
        elif column_winner:
            winner = column_winner
        elif diagonal_winner:
            winner = diagonal_winner
        else:
            winner = None
        return

    def check_rows():
        return

    def check_columns():
        return

    def check_diagonals():
        return

    # check whether there is a tie
    def check_if_tie():
        return
    # take turns for players to play
    def flip_player():
        return

    # while the game is still goin
    while game_still_on:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
    # game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("It is a tie!!")


play_game()


