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

display_board()

# play game function
def play_game():

    # handle a single turn per player
    def handle_turn(player):

        print( player + "'s turn")

        position = input("Choose a number from 1-9: ")

        valid = False
        while not valid:
            while position not in ["1","2","3","4","5","6","7","8","9"]:
                position = input("Choose a number from 1-9: ")

            position = int(position) - 1

            if board[position] == "_":
                valid = True
            else:
                print("You can't go there, sorry try again!")

        board[position] = player
        display_board()


    # take turns for players to play
    def flip_player():
        global current_player
        # check if player is x, change to o
        if current_player == "X":
            current_player = "O"
        #check if player is o, change to x
        elif current_player == "O":
            current_player = "X"
        return

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
        global game_still_on
        # check if all the rows are filled and not empty
        row_1 = board[0] == board[1] == board[2] != "_"
        row_2 = board[3] == board[4] == board[5] != "_"
        row_3 = board[6] == board[7] == board[8] != "_"

        # if any row has a match, flag that there is a winner
        if row_1 or row_2 or row_3:
            game_still_on = False

        # return the winner
        if row_1:
            return board[0]
        elif row_2:
            return board[3]
        elif row_3:
            return board[6]
        return

    def check_columns():
        global game_still_on
        # check if all columns are filled
        column_1 = board[0] == board[3] == board[6] != "_"
        column_2 = board[1] == board[4] == board[7] != "_"
        column_3 = board[2] == board[5] == board[8] != "_"

        # if any of the columns has a match, flag that there is a winner
        if column_1 or column_2 or column_3:
            game_still_on = False

        # return winner
        if column_1:
            return board[0]
        elif column_2:
            return board[1]
        elif column_3:
            return board[2]
        return

    def check_diagonals():
        global game_still_on
        # check if all columns are filled
        diagonal_1 = board[0] == board[4] == board[8] != "_"
        diagonal_2 = board[2] == board[4] == board[6] != "_"

        # if any of the columns has a match, flag that there is a winner
        if diagonal_1 or diagonal_2:
            game_still_on = False

        # return winner
        if diagonal_1:
            return board[0]
        elif diagonal_2:
            return board[2]
        return

    # check if the game is over
    def check_if_game_over():
        check_for_winner()
        check_if_tie()

    # check whether there is a tie
    def check_if_tie():
        global game_still_on
        if "_" not in board:
            game_still_on = False
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


