import time
import tkinter as tk


def create_board():
    board = []
    for _ in range(8):
        row = []
        for _ in range(8):
            row.append(' ')
        board.append(row)
    return board

# Initialize the board
board = [[' ' for _ in range(8)] for _ in range(8)]

# Display the Board
def print_board1(board):
    print("   ", end="")
    for i in range(8):
        print(f" {i} ", end="\t")
    print("\n  +" + "---+" * 8)

    for i in range(8):
        print(f"{i} |", end="")
        for j in range(8):
            print(f" {board[i][j]} |", end="")
        print("\n  +" + "---+" * 8)


# Function to get the next move from a player
def get_move(player):
    while True:
        try:
            row, col = map(int, input(
                f'Player {player}, enter the row and column (e.g., 2 3 for row 2 and column 3): ').split())
            if row >= 0 and row < 8 and col >= 0 and col < 8:
                if board[row][col] == ' ':
                    if col > 0 and board[row][col - 1] != ' ':
                        return row, col
                    elif col < 7 and board[row][col + 1] != ' ':
                        return row, col
                    elif col == 0 or col == 7:
                        return row, col
                    else:
                        print('Invalid move. You can only stack the brick next to the wall or another brick.')
                else:
                    print('Invalid move. The cell is already occupied.')
            else:
                print('Invalid move. Out of board bounds. Try again.')
        except ValueError:
            print('Invalid input. Try again.')

# Function to get the next move from a player on gui
def update_cell(row, col):
    global current_player, board

    if board[row][col] == ' ':
        if col > 0 and board[row][col - 1] != ' ':
            board[row][col] = current_player
            button = buttons[row][col]
            button.config(text=current_player)

            if check_win(board, current_player):
                message = f'Player {current_player} wins!'
                label.config(text=message)
                disable_buttons()
            elif is_board_full(board):
                message = 'It\'s a tie!'
                label.config(text=message)
                disable_buttons()
            else:
                current_player = '□' if current_player == '■' else '■'
                message = f'Current Player: {current_player}'
                label.config(text=message)

                if mode == "2" and current_player == '□':
                    row, col = find_best_move(board, current_player)
                    update_cell(row, col)
                elif mode == "3" and current_player == '■':
                    row, col = find_best_move(board, current_player)
                    update_cell(row, col)
        elif col < 7 and board[row][col + 1] != ' ':
            board[row][col] = current_player
            button = buttons[row][col]
            button.config(text=current_player)

            if check_win(board, current_player):
                message = f'Player {current_player} wins!'
                label.config(text=message)
                disable_buttons()
            elif is_board_full(board):
                message = 'It\'s a tie!'
                label.config(text=message)
                disable_buttons()
            else:
                current_player = '□' if current_player == '■' else '■'
                message = f'Current Player: {current_player}'
                label.config(text=message)

                if mode == "2" and current_player == '□':
                    row, col = find_best_move(board, current_player)
                    update_cell(row, col)
                elif mode == "3" and current_player == '■':
                    row, col = find_best_move(board, current_player)
                    update_cell(row, col)
        elif col == 0 or col == 7:
            board[row][col] = current_player
            button = buttons[row][col]
            button.config(text=current_player)

            if check_win(board, current_player):
                message = f'Player {current_player} wins!'
                label.config(text=message)
                disable_buttons()
            elif is_board_full(board):
                message = 'It\'s a tie!'
                label.config(text=message)
                disable_buttons()
            else:
                current_player = '□' if current_player == '■' else '■'
                message = f'Current Player: {current_player}'
                label.config(text=message)

                if mode == "2" and current_player == '□':
                    row, col = find_best_move(board, current_player)
                    update_cell(row, col)
                elif mode == "3" and current_player == '■':
                    row, col = find_best_move(board, current_player)
                    update_cell(row, col)

        else:
            message = f'Invalid move. You can only stack the brick next to the wall or another brick.'
            label.config(text=message)


def disable_buttons():
    for row in range(8):
        for col in range(8):
            buttons[row][col].config(state=tk.DISABLED)

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for i in range(8):
        for j in range(4):
            if all(board[i][j + k] == player for k in range(5)):
                return True
    # Check columns
    for i in range(4):
        for j in range(8):
            if all(board[i + k][j] == player for k in range(5)):
                return True
    # Check diagonals (top left to bottom right)
    for i in range(4):
        for j in range(4):
            if all(board[i + k][j + k] == player for k in range(5)):
                return True
    # Check diagonals (top right to bottom left)
    for i in range(4):
        for j in range(4, 8):
            if all(board[i + k][j - k] == player for k in range(5)):
                return True
    return False

# Function to evaluate the board state for the AI player
def evaluate_board(board, player):
    # Evaluate the board based on my own criteria
    ai_score = 0

    # Evaluate rows
    for i in range(8):
        for j in range(4):
            window = board[i][j:j + 5]
            ai_score += evaluate_window(window, player)

    # Evaluate columns
    for j in range(8):
        for i in range(4):
            window = [board[i + k][j] for k in range(5)]
            ai_score += evaluate_window(window, player)

    # Evaluate diagonals (top left to bottom right)
    for i in range(4):
        for j in range(4):
            window = [board[i + k][j + k] for k in range(5)]
            ai_score += evaluate_window(window, player)

    # Evaluate diagonals (top right to bottom left)
    for i in range(4):
        for j in range(4, 8):
            window = [board[i + k][j - k] for k in range(5)]
            ai_score += evaluate_window(window, player)

    return ai_score

# Helper function to evaluate a window of 5 consecutive cells
def evaluate_window(window, player):
    ai_count = window.count(player)
    opponent_count = window.count('■' if player == '□' else '□')

    if ai_count == 5:
        return 1000
    elif ai_count == 4 and opponent_count == 0:
        return 30
    elif ai_count == 3 and opponent_count == 0:
        return 10
    elif ai_count == 2 and opponent_count == 0:
        return 2
    elif opponent_count == 4 and ai_count == 0:
        return -90
    elif opponent_count == 3 and ai_count == 0:
        return -30
    return 0

# Function to find the best move using the minimax algorithm with alpha-beta pruning
def find_best_move(board, player):
    print("AI IS THINKING ... ")
    best_score = float('-inf')
    best_move = None
    start_time = time.time()

    for row in range(8):
        for col in range(8):
            if board[row][col] == ' ':
                if col > 0 and board[row][col - 1] != ' ':
                    # Stack the brick next to the left wall
                    board[row][col] = player
                    if check_win(board, player):
                        board[row][col] = ' '
                        return row, col  # Complete the bridge with the 5th brick

                    score = minimax(board, 2, False, float('-inf'), float('inf'), player)
                    board[row][col] = ' '

                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
                elif col < 7 and board[row][col + 1] != ' ':
                    # Stack the brick next to the right wall
                    board[row][col] = player
                    if check_win(board, player):
                        board[row][col] = ' '
                        return row, col  # Complete the bridge with the 5th brick

                    score = minimax(board, 2, False, float('-inf'), float('inf'), player)
                    board[row][col] = ' '

                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
                elif col == 0 or col == 7:
                    # Stack the brick on either side of the cave
                    board[row][col] = player
                    if check_win(board, player):
                        board[row][col] = ' '
                        return row, col  # Complete the bridge with the 5th brick

                    score = minimax(board, 2, False, float('-inf'), float('inf'), player)
                    board[row][col] = ' '

                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Time taken: {time_taken} seconds")

    return best_move

# Function to perform minimax algorithm with alpha-beta pruning
def minimax(board, depth, maximizing_player, alpha, beta, player):
    # Check if the game is over or maximum depth is reached
    if depth == 0 or check_win(board, player) or check_win(board, '□' if player == '■' else '■'):
        if check_win(board, player):
            return evaluate_board(board, player) + 100  # AI wins
        elif check_win(board, '□' if player == '■' else '■'):
            return evaluate_board(board, player) - 100  # Opponent wins
        else:
            return evaluate_board(board, player)  # Game is a draw

    if maximizing_player:
        max_eval = float('-inf')
        for row in range(8):
            for col in range(8):
                if board[row][col] == ' ':
                    board[row][col] = player
                    eval = minimax(board, depth - 1, False, alpha, beta, player)
                    board[row][col] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(8):
            for col in range(8):
                if board[row][col] == ' ':
                    board[row][col] = '□' if player == '■' else '■'
                    eval = minimax(board, depth - 1, True, alpha, beta, player)
                    board[row][col] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return min_eval

# Function to check if the board is full
def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def create_gui():
    global buttons, current_player, board, label

    root = tk.Tk()
    root.title("Magnetic Cave")
    root.configure(bg="light pink")  # Set root window background color to baby blue

    # Configure rows and columns to resize properly
    for i in range(8):
        root.grid_rowconfigure(i, weight=1, minsize=50)
        root.grid_columnconfigure(i, weight=1, minsize=50)
    root.grid_rowconfigure(8, weight=1, minsize=30)

    buttons = []
    for row in range(8):
        button_row = []
        for col in range(8):
            button = tk.Button(root, text=' ', width=5, height=2, command=lambda r=row, c=col: update_cell(r, c),
                               bg="light pink", font=("Arial", 14))  # Increase font size to 14
            button.grid(row=row, column=col, sticky="nsew")  # Use sticky option to fill the available space
            button_row.append(button)
        buttons.append(button_row)

    board = create_board()
    current_player = '■'

    label = tk.Label(root, text=f'Current Player: {current_player}', bg="light pink", font=("Arial", 16))  # Increase font size to 16
    label.grid(row=8, columnspan=8, sticky="nsew")  # Use sticky option to fill the available space

    if mode == "3" and current_player == '■':
        row, col = find_best_move(board, current_player)
        update_cell(row, col)

    root.mainloop()


# Game loop
current_player = '■'
FLAG = True
while FLAG:
    mode = input("Enter the mode \n1. Manual entry for both ■’s moves and □’s moves\n2. Manual entry for ■’s moves & "
                 "automatic moves for □ \n3. Manual entry for □’s moves & automatic moves for ■): \n")
    create_gui()
    print_board1(board)

    if mode == "1":
        if current_player == '■':
            row, col = get_move(current_player)
        else:
            row, col = get_move(current_player)
    elif mode == "2":
        if current_player == '■':
            row, col = get_move(current_player)
        else:
            row, col = find_best_move(board, current_player)
    elif mode == "3":
        if current_player == '■':
            row, col = find_best_move(board, current_player)
        else:
            row, col = get_move(current_player)
    else:
        print("Invalid mode. Please choose 1, 2, or 3.")
        break

    board[row][col] = current_player

    if check_win(board, current_player):
        print_board1(board)
        print(f'Player {current_player} wins!')
        FLAG = False

    if is_board_full(board):
        print_board1(board)
        print('It\'s a tie!')
        FLAG = False

    LOOP = input("Do you want to play again? y/n")
    if LOOP == 'y' or LOOP == 'Y':
        FLAG = True
    elif LOOP == 'n' or LOOP == 'N':
        FLAG = False
    else:
        print("Invalid , If you want to play again enter y or n")
        FLAG = True


current_player = '□' if current_player=='■'else'■'
