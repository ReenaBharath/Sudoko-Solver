# Sudoku Solver

This Python script allows you to solve Sudoku puzzles using a backtracking algorithm. Sudoku is a logic-based combinatorial number-placement puzzle where the objective is to fill a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids that compose the grid contain all of the digits from 1 to 9.

## Features

- **Input**: Enter your Sudoku board (9x9) using numbers from 1-9 and use 0 or '.' for empty spaces.
- **Output**: The script outputs the solved Sudoku board or informs if no solution exists.
- **Validation**: Validates if a move is valid before placing a number.
- **Backtracking**: Uses a backtracking algorithm to efficiently solve the Sudoku puzzle.

## How to Use

1. **Input**: Enter your Sudoku board row by row when prompted. Each row should be entered as a continuous string of numbers (e.g., "530070000" for the first row) and use '.' or '0' for empty spaces.
2. **Output**: After inputting the board, the script will display your initial board and then attempt to solve it.
3. **Solution**: If a solution is found, it will display the solved Sudoku board; otherwise, it will notify you that no solution exists.
4. **Repeat**: You can solve multiple Sudoku puzzles consecutively until you choose to exit.

## Requirements

- Python 3.x

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sudoku-solver.git
   ```
   
2. Navigate into the project directory:
   ```bash
   cd sudoku-solver
   ```

3. Run the script:
   ```bash
   python sudoku_solver.py
   ```

## Example

Here's an example of how the Sudoku Solver works:

```
Welcome to Sudoku Solver!

Enter your Sudoku board (9x9), use 0 or '.' for empty spaces:
Enter row 1 without spaces: 530070000
Enter row 2 without spaces: 600195000
Enter row 3 without spaces: 098000060
Enter row 4 without spaces: 800060003
Enter row 5 without spaces: 400803001
Enter row 6 without spaces: 700020006
Enter row 7 without spaces: 060000280
Enter row 8 without spaces: 000419005
Enter row 9 without spaces: 000080079

Your Sudoku board:
5 3 0  | 0 7 0  | 0 0 0
6 0 0  | 1 9 5  | 0 0 0
0 9 8  | 0 0 0  | 0 6 0
- - - - - - - - - - - -
8 0 0  | 0 6 0  | 0 0 3
4 0 0  | 8 0 3  | 0 0 1
7 0 0  | 0 2 0  | 0 0 6
- - - - - - - - - - - -
0 6 0  | 0 0 0  | 2 8 0
0 0 0  | 4 1 9  | 0 0 5
0 0 0  | 0 8 0  | 0 7 9

Solution....
5 3 4  | 6 7 8  | 9 1 2
6 7 2  | 1 9 5  | 3 4 8
1 9 8  | 3 4 2  | 5 6 7
- - - - - - - - - - - -
8 5 9  | 7 6 1  | 4 2 3
4 2 6  | 8 5 3  | 7 9 1
7 1 3  | 9 2 4  | 8 5 6
- - - - - - - - - - - -
9 6 1  | 5 3 7  | 2 8 4
2 8 7  | 4 1 9  | 6 3 5
3 4 5  | 2 8 6  | 1 7 9

Do you want to solve a new Sudoku? (yes/no): no

```

