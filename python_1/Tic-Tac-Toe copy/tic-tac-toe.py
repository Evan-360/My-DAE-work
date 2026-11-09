def print_board(board):
    # Creates and sets up board
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(board, player):
    """Checks rows, columns, and diagonals for a win condition."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal Win
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical Win
        [0, 4, 8], [2, 4, 6]              # Diagnonal Win
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_board_full(board):
    """Returns True if there are no empty spaces left on the board."""
    return " " not in board

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    # Initialize a flat list of 9 empty spaces representing the grid
    board = [" "] * 9
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print("Positions are numbered 1 through 9 from top-left to bottom-right.")
    
    while True:
        print_board(board)
        
        # Obtain and Check player input
        try:
            move = int(input("Player {current_player}, choose a position (1-9): "))-1
            if move < 0 or move > 8:
                print("Invalid input! Please choose a number between 1 and 9.")
                continue
            if board[move] != " ":
                print("That position is already taken! Try again.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # Place the player's symbol
        board[move] = current_player
        
        # Check for a win
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
            
        # Check for a draw
        if is_board_full(board):
            print_board(board)
            print("Draw!")
            break
        
        # Switch turns between 'Player 1(X)' and 'Player 2(O)'
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()