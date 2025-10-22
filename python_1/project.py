# Tic Tac Toe Game
# Purpose: A simple two-player Tic Tac Toe game played in the console.

# ---------- Functions ----------

def print_board(board):
    """Display the current Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    """Check if there is a winner on the board."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '.':
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '.':
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '.':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '.':
        return board[0][2]
    return None


def check_tie(board):
    """Check if the game board is full with no winner."""
    for row in board:
        if '.' in row:
            return False
    return True


def player_move(board, player_symbol):
    """Ask the current player to choose a row and column for their move."""
    valid_move = False
    while not valid_move:
        try:
            col = int(input(f"Player {player_symbol}, enter column (0-2): "))
            row = int(input(f"Player {player_symbol}, enter row (0-2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == '.':
                board[row][col] = player_symbol
                valid_move = True
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Please enter a valid number.")



# Create the board 
game_board = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]

# Variables of different data types
current_player = "X"          # string
turn_count = 0                # integer
game_active = True            # boolean

print("Welcome to Tic Tac Toe Game!")
print_board(game_board)

# Loop for repeated turns
while game_active:
    player_move(game_board, current_player)
    print_board(game_board)
    winner = check_winner(game_board)

    if winner:
        print(f"🎉 Player {winner} wins the game!")
        game_active = False
    elif check_tie(game_board):
        print("It's a tie!")
        game_active = False
    else:
        # Decision-making structure to switch players
        current_player = "O" if current_player == "X" else "X"
        turn_count += 1

def main():
    """Main loop that restarts the game automatically."""
    while True:
        play_game()
        print("\nRestarting game automatically...\n")