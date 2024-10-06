def generate_pascals_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        previous_row = triangle[-1]
        current_row = [1]
        for j in range(1, len(previous_row)):
            current_row.append(previous_row[j-1] + previous_row[j])
        current_row.append(1)
        triangle.append(current_row)
    return triangle

n = 5
triangle = generate_pascals_triangle(n)
for row in triangle:
    print(row)

