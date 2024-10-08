#!/usr/bin/python3
"""
0-pascal_triangle - function that returns a list of lists
of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the
    Pascal's triangle of size n.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1] + [triangle[i-1][j-1] + triangle[i-1][j]
                     for j in range(1, i)] + [1]
        triangle.append(row)

    return triangle
