board = [["#"] * 8 for _ in range(8)]
file = ["a", "b", "c", "d", "e", "f", "g", "h"]
selectable_types = ["pawn", "rook"]
row_dict = {1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1, 8: 0}
column_dict = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
white_type = []
white_coord = []
black_coord = []


def main():
    white_select()

    black_select()

    if "pawn" in white_type:
        check_pawn()

    if "rook" in white_type:
        check_rook()
    
    



#showing boards current state
def board_print(): 
    for x, y in zip(board, "87654321"):
        print(y, " ".join(x))
    print (" ", " ".join(file))

#select type of white piece and where to put it
def white_select():
    while True:
        white_piece = input("Please select the type of your white chess piece and the position (f.e. pawn a1): ")
        wpiece = white_piece.split(" ") # take type and coordinate
        white_type.append(wpiece[0]) # detects which type of piece was put (pawn or rook)
        try:
            row_num = int(wpiece[1][1]) #selects row f.e. 3
            column_num = wpiece[1][0].lower() #selects column f.e. d
        except (IndexError):
            print("Invalid input. Please try again")
            continue
        if len(wpiece) != 2 or len(wpiece[1]) !=2 or wpiece[0] not in selectable_types or wpiece[1][0] not in "abcdefgh" or wpiece[1][1] not in "12345678":
            print("Invalid move. Please doublecheck if you've chosen correct coordinate and piece type (f.e. pawn a1)") 
            continue
        
        row_index = row_dict[row_num] # indices for getting place of a white piece when checking which black piece can it take later
        col_index = column_dict[column_num]
        white_coord.append((row_index, col_index))
        board[row_dict[row_num]][column_dict[column_num]] = wpiece[0][0].upper()
        print(f"You've succesfully put white {wpiece[0]} on {wpiece[1]}.")
        return False




#select type of each black piece and where to put it
def black_select():
    counter = 0
    while True:
        while counter <= 16:
            black_piece = input("Please select the type of your black chess piece and the position (f.e. pawn a1): ")
            bpiece = black_piece.split(" ")
            if black_piece.lower() == "done":
                if counter == 0:
                    print("Too early! Please put at least one black piece!")
                    continue
                else:
                    return False
            if counter == 16:
                return False
            try: #check whether a person does not write a nonsense f.e. "asd"
                row_num = int(bpiece[1][1]) #selects row f.e. 3
                column_num = bpiece[1][0].lower() #selects column f.e. d
            except (IndexError):
                print("Invalid input. Please try again")
                continue

            if len(bpiece) != 2 or len(bpiece[1]) !=2 or bpiece[0] not in selectable_types or bpiece[1][0] not in "abcdefgh" or bpiece[1][1] not in "12345678" or board[row_dict[row_num]][column_dict[column_num]] != "#":
                board_print()
                print("Invalid move. Please doublecheck if you've chosen correct coordinate and piece type (f.e. pawn a1)") 
                continue
            board[row_dict[row_num]][column_dict[column_num]] = bpiece[0][0]
            
            row_index = row_dict[row_num] # indices for getting place of black pieces for later use
            col_index = column_dict[column_num]
            black_coord.append((row_index, col_index))
            print(f"You've succesfully put black {bpiece[0]} on {bpiece[1]}.")
            counter += 1

        

def check_pawn():
    row_index = white_coord[0][0] #where is white pawn located
    col_index = white_coord[0][1]
    move_left = [row_index - 1, col_index - 1]
    move_right = [row_index - 1, col_index + 1]
    takeable_pieces = []

    if row_index - 1 < 0: #pawn on the 8 row cannot do any valid takes
        print("No valid takes for your white pawn possible")
        return
    
    if 0 <= move_left[1] <= 7 and board[move_left[0]][move_left[1]] in "pr": #if white pawn on h file, then only check move to the up-left
        takeable_pieces.append(f"{file[move_left[1]]}{8 - move_left[0]}")
            
    
    if 0 <= move_right[1] <= 7 and board[move_right[0]][move_right[1]] in "pr": #if white pawn is on a file, then only check move to the up-right
        takeable_pieces.append(f"{file[move_right[1]]}{8 - move_right[0]}")
        
    if takeable_pieces:
        board_print()
        print(f"Your white pawn can take black piece(s) on {" and ".join(takeable_pieces)}.")
    else:
        board_print()
        print("No valid takes for your white pawn.")
    



def check_rook():
    row_index = white_coord[0][0] # where is white rook located
    col_index = white_coord[0][1]
    takeable_pieces = []

    for i in range(row_index - 1, -1, -1): #rook move up
        if board[i][col_index] in "pr": 
            takeable_pieces.append(f"{file[col_index]}{8 - i}")
            break
    
    for i in range(row_index + 1, 8): #rook move down
        if board[i][col_index] in "pr":
            takeable_pieces.append(f"{file[col_index]}{8 - i}")
            break
    
    for i in range(col_index - 1, -1, -1): #rook left
        if board[row_index][i] in "pr":
            takeable_pieces.append(f"{file[i]}{8 - row_index}")
            break
    
    for i in range(col_index + 1, 8): #rook right
        if board[row_index][i] in "pr":
            takeable_pieces.append(f"{file[i]}{8 - row_index}")
            break
    
    if takeable_pieces:
        board_print()
        print(f"Your white rook can take black piece(s) on {" and ".join(takeable_pieces)}.")
    else:
        board_print()
        print("No black pieces can be taken by your white rook.")

main()