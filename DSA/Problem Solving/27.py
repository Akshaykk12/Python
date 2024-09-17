"""
Problem: Rotate a 2D matrix by 90 degrees clockwise.
Input:
Matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output:
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
Explanation: The matrix is rotated 90 degrees clockwise.
"""
import numpy as np

def matrix_rotat(matrix):
    matrix = np.transpose(matrix)
    for i in range(len(matrix)):
        matrix[i][0], matrix[i][len(matrix[0])-1] = matrix[i][len(matrix[0])-1], matrix[i][0]

    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_rotat(matrix))
