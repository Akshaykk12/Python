"""
Write the code to traverse a matrix in a spiral format.

Sample Input

Input
5   4
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16
17  18  19  20

Output
1  2  3  4  8  12  16  20  19  18  17  13  9  5  6  7  11  15  12  14 10

"""


def traverse_matrix(matrix, rows, cols):
    result = []
    
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1  

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1  

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1  

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1  

    return result

row, column = input().split()
row, column = int(row), int(column)
L = [[int(input()) for i in range(column)] for _ in range(row)]


print(traverse_matrix(L, row, column))
