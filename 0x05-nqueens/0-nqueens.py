#!/usr/bin/env python3
"""solves the N queens problem"""
import sys


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
