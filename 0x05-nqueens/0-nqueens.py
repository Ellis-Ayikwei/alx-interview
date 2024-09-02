#!/usr/bin/python3
"""solves the N queens problem"""
import sys


def print_solution(board):
    """Prints a solution in the format required:
    list of [row, col] for each queen."""
    solution = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]:
                solution.append([row, col])
    print(solution)


def is_valid(board, row, col):
    """
    Check if it's valid to place a queen at board[row][col].

    This method checks if the current position is valid for
    placing a queen by
    looking at all the positions above the current position.
    If there is a queen
    in the same column or on the same diagonal, the position is not valid.
    """
    # Check the same column
    for i in range(row):
        if board[i][col]:
            return False

    # Check the upper-left diagonal
    for i in range(row):
        if col - (row - i) >= 0 and board[i][col - (row - i)]:
            return False

    # Check the upper-right diagonal
    for i in range(row):
        if col + (row - i) < len(board) and board[i][col + (row - i)]:
            return False

    return True


def solve_nqueens(board, row):
    """Use backtracking to solve the N-Queens problem."""
    n = len(board)
    if row >= n:
        print_solution(board)
        return

    for col in range(n):
        if is_valid(board, row, col):
            board[row][col] = True
            solve_nqueens(board, row + 1)
            board[row][col] = False


def main():
    """Main function to handle command-line arguments and
    initiate the N-Queens solver."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [[False] * N for _ in range(N)]

    # Start solving the N-Queens problem
    solve_nqueens(board, 0)


if __name__ == "__main__":
    main()
