"""
Problem: Merge two sorted arrays into a single sorted array.
Input:
Array 1: [1, 3, 5]
Array 2: [2, 4, 6]
Output:
[1, 2, 3, 4, 5, 6]
"""

def addnsort(arr1, arr2):
    arr3 = []
    for i in arr1:
        arr3.append(i)

    for i in arr2:
        arr3.append(i)

    arr3 = sorted(arr3)
    return arr3

arr1= [1,3,5]
arr2= [2,4,6]
print(addnsort(arr1, arr2))