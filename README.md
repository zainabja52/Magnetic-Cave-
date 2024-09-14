# Magnetic Cave Game

## Overview
Magnetic Cave is a board game implemented using Python and Tkinter for the GUI. The game allows two players to place bricks on an 8x8 board, with the goal of forming a line of five consecutive bricks either horizontally, vertically, or diagonally. The game supports three modes:
1. Manual entry for both players.
2. Manual entry for '■' and automatic moves for '□'.
3. Manual entry for '□' and automatic moves for '■'.

## Features
- **Graphical User Interface**: Built using Tkinter.
- **AI Player**: Uses the Minimax algorithm with alpha-beta pruning for optimal moves.
- **Three Game Modes**: Supports different combinations of manual and automatic moves.
- **Win and Tie Detection**: Automatically detects when a player wins or when the game ends in a tie.

## How to Play
1. Run the game script.
2. Select the game mode:
   - Mode 1: Manual entry for both players.
   - Mode 2: Manual entry for '■' and automatic moves for '□'.
   - Mode 3: Manual entry for '□' and automatic moves for '■'.
3. Follow the on-screen instructions to place your bricks.
4. The game will display the current player and update the board after each move.
5. The game ends when a player forms a line of five consecutive bricks or when the board is full.

## Code Structure
- **create_board**: Initializes the 8x8 game board.
- **print_board1**: Displays the board in the console.
- **get_move**: Gets the next move from a player.
- **update_cell**: Updates the board and GUI based on the player's move.
- **check_win**: Checks if a player has won.
- **evaluate_board**: Evaluates the board state for the AI player.
- **evaluate_window**: Helper function to evaluate a window of 5 consecutive cells.
- **find_best_move**: Finds the best move using the Minimax algorithm with alpha-beta pruning.
- **minimax**: Performs the Minimax algorithm with alpha-beta pruning.
- **is_board_full**: Checks if the board is full.
- **create_gui**: Sets up the graphical user interface.
- **Game Loop**: Main loop to handle game flow and player interactions.

## Requirements
- Python 3.x
- Tkinter library

## Installation
1. Clone the repository:
   ```bash
   git clone (https://github.com/zainabja52/Magnetic-Cave-.git)
```

2. Run the game script:
 ```bash
python main.py
```


