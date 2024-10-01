#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing Pascal's Triangle of n rows.
    Returns an empty list if n <= 0.
    """
    triangle = []
    
    if n <= 0:
        return triangle
    
    # First row is always [1]
    triangle = [[1]]
    
    # Build subsequent rows
    for i in range(1, n):
        row = [1]  # Every row starts with 1
        # Compute the values in the middle of the row
        for j in range(len(triangle[i - 1]) - 1):
            row.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        row.append(1)  # Every row ends with 1
        triangle.append(row)
    
    return triangle

