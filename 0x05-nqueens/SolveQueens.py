from isValid import is_valid

"""a Module to define the print solution and the solve queens functions"""


def print_solution(board):
    """Prints a solution in the format required:
    list of [row, col] for each queen."""
    solution = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]:
                solution.append([row, col])
    print(solution)


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
