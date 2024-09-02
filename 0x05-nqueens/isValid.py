#!/usr/bin/env python3
"""A module to define the is valid function"""


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
