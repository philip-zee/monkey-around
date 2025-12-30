def rotate_matrix_90_clockwise(matrix):
    # Transpose, then reverse each row
    return [list(row) for row in zip(*matrix[::-1])]
