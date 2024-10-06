def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        # Create a row filled with 1's
        row = [1] * (i + 1)
        # Update the inner elements of the row (if applicable)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        # Add the row to the triangle
        triangle.append(row)
    
    return triangle

