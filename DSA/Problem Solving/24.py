"""
Problem: Find the maximum sum of a contiguous subarray.
Input:
Array: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output:
6
Explanation: The subarray [4, -1, 2, 1] has the largest sum = 6
"""
def max_contiguous_sum(arr1):
    max_sum = 0
    for i in range(len(arr1)):
        temp = arr1[i]
        for j in range(i+1, len(arr1)):
            temp = temp + arr1[j]
            if max_sum < temp:
                max_sum = temp
    return max_sum

arra = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_contiguous_sum(arra))