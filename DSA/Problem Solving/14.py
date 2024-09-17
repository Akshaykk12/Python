"""
Problem: Implement a binary search algorithm to find a target value in a 
sorted array.

Input:
Array: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Target: 4

Output: 3
Explanation: The function returns the index of the target value in the 
array
"""
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = int((left + right) / 2)

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1

    return "ValueError"

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
index = binary_search(arr, target)
print(index)