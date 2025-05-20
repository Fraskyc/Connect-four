ROWS = 6
COLUMNS = 7
EMPTY = "."

def create_board():
    return [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    print("\n  " + " ".join(str(i) for i in range(COLUMNS)))
    for row in board:
        print(" |" + "|".join(row) + "|")
    print("  " + "--" * COLUMNS)

def is_valid_column(board, col):
    return 0 <= col < COLUMNS and board[0][col] == EMPTY

def get_next_open_row(board, col):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == EMPTY:
            return r
    return None

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    
    for r in range(ROWS):
        for c in range(COLUMNS - 3):
            if all(board[r][c + i] == piece for i in range(4)):
                return True
    
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if all(board[r + i][c] == piece for i in range(4)):
                return True
    
    for r in range(ROWS - 3):
        for c in range(COLUMNS - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True
   
    for r in range(3, ROWS):
        for c in range(COLUMNS - 3):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True
    return False

def board_full(board):
    return all(board[0][c] != EMPTY for c in range(COLUMNS))

def get_player_move(board, player):
    while True:
        try:
            col = int(input(f"Hráč {player} - zvol sloupec (0-{COLUMNS - 1}): "))
            if is_valid_column(board, col):
                return col
            else:
                print("⚠️ Neplatný sloupec, zkus to znovu.")
        except ValueError:
            print("⚠️ Zadej číslo.")

def play_game():
    board = create_board()
    game_over = False
    current_player = 1

    while not game_over:
        print_board(board)
        piece = "X" if current_player == 1 else "O"

        col = get_player_move(board, current_player)

        row = get_next_open_row(board, col)
        drop_piece(board, row, col, piece)

        if winning_move(board, piece):
            print_board(board)
            print(f"🎉 Hráč {current_player} ({piece}) vyhrál!")
            game_over = True
        elif board_full(board):
            print_board(board)
            print("🤝 Remíza!")
            game_over = True
        else:
            current_player = 2 if current_player == 1 else 1

if __name__ == "__main__":
    play_game()
