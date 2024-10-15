#!/usr/bin/python3
"""
Pascal Triangle
"""

def pascal_triangle(n):

    """
    Generates Pascal's Triangle up to the nth row.
    
    Parameters:
    n (int): The number of rows of Pascal's Triangle to generate.
    
    Returns:
    list: A list of lists, where each inner list represents a row in Pascal's Triangle.
          If n <= 0, an empty list is returned.
    
    Description:
    Pascal's Triangle is a triangular array where each number is the sum of the two numbers directly above it.
    The first and last element of each row is always 1.
    
    Example:
    For n = 5, the function returns:
    [
      [1],
      [1, 1],
      [1, 2, 1],
      [1, 3, 3, 1],
      [1, 4, 6, 4, 1]
    ]
    
    """
    
    if n <= 0:
        return []
    
    triangle = [[1]]  
    
    for i in range(1, n):
        row = [1]  
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    
    return triangle
