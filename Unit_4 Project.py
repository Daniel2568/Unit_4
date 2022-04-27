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












#switching players
if current_player == p1_name
    current_player = p2_name
    current_symbol = "0"

