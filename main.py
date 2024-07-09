def print_board(board):
    """
    Function to print the Sudoku board.
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty_location(board):
    """
    Function to find an empty location in the board that is not filled yet.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None


def is_valid(board, num, pos):
    """
    Function to check if it's valid to place 'num' in 'pos' of the board.
    """
    # Check row
    if num in board[pos[0]]:
        return False

    # Check column
    for i in range(9):
        if board[i][pos[1]] == num:
            return False

    # Check 3x3 box
    box_row_start = (pos[0] // 3) * 3
    box_col_start = (pos[1] // 3) * 3

    for i in range(box_row_start, box_row_start + 3):
        for j in range(box_col_start, box_col_start + 3):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board):
    """
    Function to solve the Sudoku using backtracking.
    """
    empty = find_empty_location(board)
    if not empty:
        return True
    else:
        row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


def main():
    print("Welcome to Sudoku Solver!")

    while True:
        board = []
        print("\nEnter your Sudoku board (9x9), use 0 or '.' for empty spaces:")
        
        # Input Sudoku board
        for i in range(9):
            while True:
                row_input = input(f"Enter row {i + 1} without spaces: ").strip()
                if len(row_input) == 9:
                    break
                else:
                    print("Error: Each row must contain exactly 9 numbers.")
            
            # Convert input row to integers or 0 for empty spaces
            row = [int(num) if num != '.' else 0 for num in row_input]
            board.append(row)

        print("\nYour Sudoku board:")
        print_board(board)

        if solve_sudoku(board):
            print("\nSolution....")
            print_board(board)
        else:
            print("\nNo solution exists.")

        # Ask user if they want to solve a new Sudoku or exit
        choice = input("\nDo you want to solve a new Sudoku? (yes/no): ").strip().lower()
        if choice != 'yes':
            break


if __name__ == "__main__":
    main()
