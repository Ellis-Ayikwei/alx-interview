#!/usr/bin/python3
"""The Island perimeter module"""


def island_perimeter(grid):
    """
    This function defines and
    the perimeter of an island
    
    Args:
        - grid : a 2d list
    Returns (int): perimeter or the 2d list
    """
    rows = length of grid
    cols = length of grid[0]
    perimeter = 0
    shared_edges = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # Land cell
                perimeter += 4  # Each land cell starts with 4 sides
                # Check if there's a neighboring land cell
                if row > 0 and grid[row - 1][col] == 1:  # Above
                    shared_edges += 1
                if row < rows - 1 and grid[row + 1][col] == 1:  # Below
                    shared_edges += 1
                if col > 0 and grid[row][col - 1] == 1:  # Left
                    shared_edges += 1
                if col < cols - 1 and grid[row][col + 1] == 1:  # Right
                    shared_edges += 1
    return perimeter - shared_edges
