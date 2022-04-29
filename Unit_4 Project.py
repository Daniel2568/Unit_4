# Tic Tac Toe Revitalized

board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]  

def print_board():
    print(
        f"{board[0][0]} | {board[0][1]} | {board[0][2]}\n"
        "---------\n"
        f"{board[1][0]} | {board[1][1]} | {board[1][2]}\n"
        "---------\n"
        f"{board[2][0]} | {board[2][1]} | {board[2][2]}\n"
    )

def player_turn(name, symbol):
    valid_spot = False
    while not valid_spot:
        # choose row
        valid_row = False
        while not valid_row:
            row_choice = int(input(f"{name}, choose a row to place your {symbol}:")) -1
            if row_choice < 0 or row_choice > 2:
                print(f"Invalid choice {name}, try to use numbers that are in range.")
            else:
                valid_row = True
        #choose column
        valid_column = False
        while not valid_column:
            column_choice = int(input(f"{name}, choose a column to place your {symbol}:")) -1
            if column_choice < 0 or  column_choice > 2:
                print(f"Invalid column {name}, try a different column")
            else:
                valid_column = True

        # Place symbol at location
        if board[row_choice][column_choice] == " ":
            board[row_choice][column_choice] = symbol
            valid_spot = True
        else:
            print(f"That space is occupied {name}, try a different spot.")

def check_for_win():
    # check for row win
    for row in range(len(board)):
        if board[row][0] != " ":
            if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
                return True

    # check for column win 
    for column in range(len(board)):
        column_values = []
        for row in range(len(board)):
            column_values.append(board[row][column])
        if column_values[0] != " ":
            if column_values[0] == column_values[1] and column_values[1] == column_values[2]:
                print("Column Win!") 
                return True

    # Diagonal Win
    if board[0][0] != " ":
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            print("Diagonal Win!")
            return True
    #right to left
    if board[0][2] != " ":
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            print("Diagonal Win!")
            return True


# Player Info
p1_name = input("Player 1, What would you like your name to be?>")
p2_name = input("Player 2, What would you like your name to be?>")

current_player = p1_name
current_symbol = "X"

print_board()

# game loop
turns = 0
win = False
while turns < 9:
    # player turns
    player_turn(current_player, current_symbol)

    # update board
    print_board()

    if check_for_win():
        print(f"{current_player} wins the game!")
        win = True
        break 

    # switching players
    if current_player == p1_name:
        current_player = p2_name
        current_symbol = "O"
    else:
        current_player = p1_name
        current_symbol = 'X'
    #update turns
    turns += 1

if not win:
    print("Game ends in a tie!")  


