"""
Problem: Write a program to check if two given matrices are identical.

Input:
Matrix A: [[1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4]]
Matrix B: [[1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4]]

Output: Matrices are identical

Explanation: The program checks each corresponding element in both 
matrices for equality.
"""

matrix_A= [[1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4]]
matrix_B= [[1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4]]

def check_iden(mat1, mat2):
    if ((len(mat1), len(mat1[0])) != ((len(mat2), len(mat2[0])))):
        return "Matrices are not identical"
    else:
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                if mat1[i][j] != mat2[i][j]:
                    return "Matrices are not identical"
    return "Matrices are identical"



print(check_iden(matrix_A, matrix_B))