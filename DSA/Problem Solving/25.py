"""
Problem: Find the intersection of two unsorted arrays.
Input:
Array 1: [1, 2, 2, 1]
Array 2: [2, 2]
Output:
[2]
Explanation: The common element between the arrays is 2
"""
def intersection(arr1, arr2):
    arr3= []
    for i in arr1:
        if i in arr2 and i not in arr3:
            arr3.append(i)
    return arr3

arr1 = [1, 2, 2, 1]
arr2 = [2, 2]
print(intersection(arr1, arr2))